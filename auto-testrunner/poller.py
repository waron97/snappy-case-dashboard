import logging
import threading

from ado import fetch_open_prs
from config import (
    ENABLE_TEST01_INIT_TEST,
    FAST_QUEUE_KEY,
    POLL_INTERVAL,
    POLLER_LOCK_KEY,
    QUEUE_KEY,
    STATE_TTL,
    TASKS,
    WORKER_ID,
    rdb,
)
from runner import task_result_exists, vacuum
from tasks import decode_job, encode_job, live_jobs, mark_task, queue_for, reset_tasks

log = logging.getLogger(__name__)

_poll_lock = threading.Lock()


def enabled_tasks():
    """The task set a commit must complete. `init` drops out when the feature flag is
    off (dev compose) so the messenger still sees a complete set and reports."""
    return [t for t in TASKS if t != "init" or ENABLE_TEST01_INIT_TEST]


def _is_running(commit_hash, task=None):
    for job in live_jobs().values():
        if job.get("commit") != commit_hash:
            continue
        if task is None or job.get("task") == task:
            return True
    return False


def enqueue_task(commit_hash, task, force=False, front=False):
    """Queue one task of one commit. Returns True if it was actually pushed.
    `front` (LPUSH) is for manual rechecks, which should not wait behind the backlog."""
    if not force and task_result_exists(commit_hash, task):
        return False
    if _is_running(commit_hash, task):
        return False
    q = queue_for(task)
    item = encode_job(commit_hash, task)
    if rdb.lpos(q, item) is not None:
        return False
    if front:
        rdb.lpush(q, item)
    else:
        rdb.rpush(q, item)
    mark_task(commit_hash, task, "queued")
    log.info(f"Enqueued {commit_hash[:8]} {task}")
    return True


def enqueue_all(commit_hash, **kwargs):
    """Queue every enabled task of a commit. Returns the tasks actually pushed."""
    return [t for t in enabled_tasks() if enqueue_task(commit_hash, t, **kwargs)]


def drop_commit(commit_hash):
    """Forget a commit that no open PR points at any more: pull its jobs out of both
    queues and clear its task state, so the messenger stops tracking it."""
    for task in TASKS:
        rdb.lrem(queue_for(task), 0, encode_job(commit_hash, task))
    reset_tasks(commit_hash)


def do_poll():
    with _poll_lock:
        lock_acquired = rdb.set(POLLER_LOCK_KEY, WORKER_ID, nx=True, ex=POLL_INTERVAL)
        if not lock_acquired:
            return None, []
        prs = fetch_open_prs()
        log.info(f"Found {len(prs)} open PRs")
        active = {pr.get("lastMergeSourceCommit", {}).get("commitId") for pr in prs} - {None}
        vacuum(active)
        for pr in prs:
            commit = pr.get("lastMergeSourceCommit", {}).get("commitId")
            pr_id = pr.get("pullRequestId")
            if commit and pr_id:
                rdb.setex(f"test:pr_id:{commit}", STATE_TTL, str(pr_id))
                rdb.setex(f"test:pr_desc:{commit}", STATE_TTL, (pr.get("description") or ""))
        # Purge jobs for commits that are no longer any open PR's head, across both queues.
        stale = set()
        for q in (FAST_QUEUE_KEY, QUEUE_KEY):
            for raw in rdb.lrange(q, 0, -1):
                commit, _ = decode_job(raw)
                if commit not in active:
                    stale.add(commit)
        for commit in stale:
            drop_commit(commit)
            log.info(f"Removed stale commit {commit[:8]} from queues")
        enqueued = []
        for commit in active:
            enqueued += [{"commit": commit, "task": t} for t in enqueue_all(commit)]
        return len(prs), enqueued
