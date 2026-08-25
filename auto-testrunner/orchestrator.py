import logging
import threading
import time

import instances
from api import app
from base_db import (
    cleanup_orphan_test_dbs,
    reconcile_copies_on_boot,
    reconcile_pool_on_boot,
    warm_pool,
)
from config import (
    ENABLE_TEST01_INIT_TEST,
    FAST_QUEUE_KEY,
    MESSENGER_INTERVAL,
    POLL_INTERVAL,
    POOL_WARM_INTERVAL,
    QUEUE_KEY,
    RESULTS_DIR,
    ROLE,
    rdb,
)
from notifier import dispatch_ready, reap_dead_tasks
from poller import do_poll
from runner import TASK_RUNNERS, task_result_exists
from tasks import (
    begin_job,
    decode_job,
    end_job,
    heartbeat,
    heartbeat_loop,
    mark_task,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


def poller():
    while True:
        try:
            do_poll()
        except Exception as e:
            log.error(f"Poller error: {e}")
        time.sleep(POLL_INTERVAL)


def warmer():
    while True:
        try:
            if ENABLE_TEST01_INIT_TEST:
                warm_pool()
        except Exception as e:
            log.error(f"Pool warmer error: {e}")
        time.sleep(POOL_WARM_INTERVAL)


def messenger():
    """Collects finished task sets and dispatches the PR comments. Lives on control so
    there is a single writer, and so a worker can move on to its next task immediately."""
    while True:
        try:
            reap_dead_tasks()
            dispatch_ready()
        except Exception as e:
            log.error(f"Messenger error: {e}")
        time.sleep(MESSENGER_INTERVAL)


def worker():
    """Claim and run exactly ONE task per iteration. Parallelism across a commit's tasks
    comes from the replica count; keeping it to one task at a time is what lets every
    replica share a single private /opt/repo and /opt/odoo/addons."""
    heartbeat()  # publish liveness before the first claim, not 30s later
    threading.Thread(target=heartbeat_loop, daemon=True, name="heartbeat").start()
    while True:
        try:
            # Fast queue first: pre-commit is minutes and must not wait behind test runs.
            item = rdb.blpop([FAST_QUEUE_KEY, QUEUE_KEY], timeout=30)
            if item is None:
                continue
            _, raw = item
            commit_hash, task = decode_job(raw)
            if task not in TASK_RUNNERS:
                log.warning(f"Dropping unknown job {commit_hash[:8]!r}/{task!r}")
                continue
            if task_result_exists(commit_hash, task):
                log.info(f"Skipping {commit_hash[:8]} {task}, results already exist")
                mark_task(commit_hash, task, "done")
                continue

            begin_job(commit_hash, task, time.time())
            mark_task(commit_hash, task, "running")
            log.info(f"Starting {task} for {commit_hash}")
            try:
                TASK_RUNNERS[task](commit_hash)
            except Exception as run_err:
                log.error(f"[{commit_hash[:8]}] {task} error: {run_err}")
            finally:
                # Terminal either way — the log file carries the verdict, and this is
                # what releases the commit to the messenger.
                mark_task(commit_hash, task, "done")
                end_job()
            log.info(f"Finished {task} for {commit_hash[:8]}")
        except Exception as e:
            log.error(f"Worker error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if ROLE == "control":
        # Singletons + base lifecycle. No worker loop here.
        try:
            # Must run before cleanup_orphan_test_dbs(): it recovers pool DBs that
            # finished building before a past restart (marking them ready) and clears
            # stale 'building' entries — otherwise those DBs would look untracked and
            # get dropped as orphans by the next call, or (for entries that never
            # actually finished) permanently block warm_pool()'s deficit accounting.
            reconcile_pool_on_boot()
        except Exception as e:
            log.error(f"Pool reconciliation failed: {e}")
        try:
            reconcile_copies_on_boot()
        except Exception as e:
            log.error(f"Copy reconciliation failed: {e}")
        try:
            cleanup_orphan_test_dbs()
        except Exception as e:
            log.error(f"Orphan DB cleanup failed: {e}")

        # Any previously-attached Odoo subprocess died with the last container — never
        # try to reattach, always start reporting "stopped".
        instances.reset_to_stopped_on_boot()

        # Pre-split queue entries are bare commit hashes with no task, which no worker
        # can decode. Drop them; the poller re-enqueues every open PR within a minute.
        dropped = rdb.delete(QUEUE_KEY, FAST_QUEUE_KEY)
        if dropped:
            log.info("Flushed queue keys for the per-task job format")

        t_poller = threading.Thread(target=poller, daemon=True, name="poller")
        t_poller.start()
        log.info("Poller started (interval: 60s)")

        if ENABLE_TEST01_INIT_TEST:
            t_warmer = threading.Thread(target=warmer, daemon=True, name="warmer")
            t_warmer.start()
            log.info(f"Pool warmer started (interval: {POOL_WARM_INTERVAL}s)")

        t_messenger = threading.Thread(target=messenger, daemon=True, name="messenger")
        t_messenger.start()
        log.info(f"Messenger started (interval: {MESSENGER_INTERVAL}s)")

        t_api = threading.Thread(
            target=lambda: app.run(host="0.0.0.0", port=8765, use_reloader=False),
            daemon=True,
            name="api",
        )
        t_api.start()
        log.info("API started on :8765")

        log.info("Control plane ready")
        threading.Event().wait()  # block forever; daemon threads do the work
    else:
        log.info("Worker starting...")
        worker()
