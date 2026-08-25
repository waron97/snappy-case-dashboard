"""Queue encoding, per-commit task state, and per-worker live status.

A commit's work is three independently-queued tasks (config.TASKS). This module owns the
Redis bookkeeping that lets workers claim one task at a time, lets the control plane know
when a commit's whole set is finished, and lets the UI show what each worker is doing.

Imports only `config` — `runner` and `poller` both import this, so it must stay a leaf.
"""

import json
import logging
import time

from config import (
    FAST_QUEUE_KEY,
    FAST_TASKS,
    HEARTBEAT_INTERVAL,
    HEARTBEAT_PREFIX,
    HEARTBEAT_TTL,
    QUEUE_KEY,
    STATE_TTL,
    TASK_STATE_PREFIX,
    WORKER_ID,
    WORKERS_KEY,
    rdb,
)

log = logging.getLogger(__name__)


def _decode(v):
    return v.decode() if isinstance(v, bytes) else v


# --- queue encoding ---------------------------------------------------------------
# A job is "<commit>:<task>". The commit is 40 hex chars and the task a fixed alnum
# token, so partitioning on the first ":" is unambiguous.


def encode_job(commit_hash, task):
    return f"{commit_hash}:{task}"


def decode_job(raw):
    """Returns (commit_hash, task), or (value, None) for anything unparseable."""
    s = _decode(raw)
    commit_hash, sep, task = s.partition(":")
    if not sep or not task:
        return s, None
    return commit_hash, task


def queue_for(task):
    return FAST_QUEUE_KEY if task in FAST_TASKS else QUEUE_KEY


# --- per-commit task state --------------------------------------------------------


def _state_key(commit_hash):
    return f"{TASK_STATE_PREFIX}{commit_hash}"


def mark_task(commit_hash, task, state):
    key = _state_key(commit_hash)
    rdb.hset(key, task, state)
    rdb.expire(key, STATE_TTL)


def task_states(commit_hash):
    """{task: 'queued'|'running'|'done'} for the commit; empty dict if unknown.
    Bookkeeping fields (`<task>:attempts`) live in the same hash and are filtered out."""
    return {
        _decode(k): _decode(v)
        for k, v in rdb.hgetall(_state_key(commit_hash)).items()
        if ":" not in _decode(k)
    }


def bump_attempts(commit_hash, task):
    """Count how many times this task has been requeued after a worker died."""
    key = _state_key(commit_hash)
    n = rdb.hincrby(key, f"{task}:attempts", 1)
    rdb.expire(key, STATE_TTL)
    return n


def reset_tasks(commit_hash):
    rdb.delete(_state_key(commit_hash))


def iter_task_commits():
    for key in rdb.scan_iter(f"{TASK_STATE_PREFIX}*"):
        yield _decode(key)[len(TASK_STATE_PREFIX) :]


# --- per-worker live status -------------------------------------------------------
# WORKERS_KEY holds one JSON payload per worker hostname: what commit, which task, the
# stage inside that task, and when it started. Read by /status for the control panel.

_CURRENT = {}


def _publish():
    rdb.hset(WORKERS_KEY, WORKER_ID, json.dumps(_CURRENT))


def begin_job(commit_hash, task, started):
    _CURRENT.clear()
    _CURRENT.update(commit=commit_hash, task=task, stage="starting", started=started)
    _publish()


def set_stage(stage):
    """Publish the current step for the UI, and mirror it into the container log."""
    if not _CURRENT:
        return
    _CURRENT["stage"] = stage
    log.info(f"[{_CURRENT['commit'][:8]}/{_CURRENT['task']}] {stage}")
    _publish()


def end_job():
    _CURRENT.clear()
    rdb.hdel(WORKERS_KEY, WORKER_ID)


def heartbeat():
    rdb.setex(f"{HEARTBEAT_PREFIX}{WORKER_ID}", HEARTBEAT_TTL, "1")
    # Re-publish the job too, so the entry is self-healing. Without this, a worker that
    # stalls past HEARTBEAT_TTL (host freeze, SIGSTOP) has its entry reaped and never
    # restores it until the next set_stage — and the reaper, seeing a 'running' task
    # held by nobody, would requeue it while the original is still going.
    if _CURRENT:
        _publish()


def heartbeat_loop():
    while True:
        try:
            heartbeat()
        except Exception as e:
            log.error(f"Heartbeat error: {e}")
        time.sleep(HEARTBEAT_INTERVAL)


def live_jobs():
    """{worker_id: job} for workers whose heartbeat is still alive. Entries left behind
    by a SIGKILLed worker (no heartbeat, or unparseable) are reaped as we go, so the UI
    stops showing dead runs and reap_dead_tasks can requeue their tasks."""
    live = {}
    for raw_wid, raw_job in rdb.hgetall(WORKERS_KEY).items():
        wid = _decode(raw_wid)
        if not rdb.exists(f"{HEARTBEAT_PREFIX}{wid}"):
            rdb.hdel(WORKERS_KEY, wid)
            log.info(f"Reaped worker entry {wid} (heartbeat lapsed)")
            continue
        try:
            job = json.loads(_decode(raw_job))
        except ValueError:
            rdb.hdel(WORKERS_KEY, wid)
            continue
        job["worker"] = wid
        live[wid] = job
    return live
