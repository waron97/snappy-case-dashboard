import logging
import threading

from ado import fetch_open_prs
from config import (
    POLL_INTERVAL,
    POLLER_LOCK_KEY,
    QUEUE_KEY,
    STATE_TTL,
    WORKER_ID,
    WORKERS_KEY,
    rdb,
)
from runner import result_exists, vacuum

log = logging.getLogger(__name__)

_poll_lock = threading.Lock()


def _is_running(commit_hash):
    return any(
        (v.decode() if isinstance(v, bytes) else v) == commit_hash
        for v in rdb.hvals(WORKERS_KEY)
    )


def enqueue(commit_hash):
    if result_exists(commit_hash):
        return
    if _is_running(commit_hash):
        return
    if rdb.lpos(QUEUE_KEY, commit_hash) is not None:
        return
    rdb.rpush(QUEUE_KEY, commit_hash)
    log.info(f"Enqueued {commit_hash}")


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
        queued = [c.decode() if isinstance(c, bytes) else c for c in rdb.lrange(QUEUE_KEY, 0, -1)]
        for commit in queued:
            if commit not in active:
                count = rdb.lrem(QUEUE_KEY, 0, commit)
                if count:
                    log.info(f"Removed stale commit {commit[:8]} from queue")
        enqueued = []
        for commit in active:
            before = rdb.llen(QUEUE_KEY)
            enqueue(commit)
            if rdb.llen(QUEUE_KEY) > before:
                enqueued.append(commit)
        return len(prs), enqueued
