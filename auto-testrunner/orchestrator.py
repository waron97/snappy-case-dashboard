import logging
import time

from api import app
from base_db import cleanup_orphan_test_dbs, warm_pool
from config import (
    ENABLE_TEST01_INIT_TEST,
    POLL_INTERVAL,
    POOL_WARM_INTERVAL,
    QUEUE_KEY,
    RESULTS_DIR,
    ROLE,
    rdb,
)
from notifier import notify_pr
from poller import do_poll
from runner import result_exists, run_test

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


def worker():
    while True:
        try:
            item = rdb.blpop(QUEUE_KEY, timeout=30)
            if item is None:
                continue
            _, raw = item
            commit_hash = raw.decode() if isinstance(raw, bytes) else raw
            if result_exists(commit_hash):
                log.info(f"Skipping {commit_hash[:8]}, results already exist")
                continue
            try:
                run_test(commit_hash)
            except Exception as run_err:
                log.error(f"[{commit_hash[:8]}] Run error: {run_err}")
            if not result_exists(commit_hash):
                log.warning(f"[{commit_hash[:8]}] No results produced, skipping notification")
                continue
            try:
                notify_pr(commit_hash)
            except Exception as notify_err:
                log.error(f"[{commit_hash[:8]}] Notification error: {notify_err}")
        except Exception as e:
            log.error(f"Worker error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    import threading

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if ROLE == "control":
        # Singletons + base lifecycle. No worker loop here.
        try:
            cleanup_orphan_test_dbs()
        except Exception as e:
            log.error(f"Orphan DB cleanup failed: {e}")

        t_poller = threading.Thread(target=poller, daemon=True, name="poller")
        t_poller.start()
        log.info("Poller started (interval: 60s)")

        if ENABLE_TEST01_INIT_TEST:
            t_warmer = threading.Thread(target=warmer, daemon=True, name="warmer")
            t_warmer.start()
            log.info(f"Pool warmer started (interval: {POOL_WARM_INTERVAL}s)")

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
