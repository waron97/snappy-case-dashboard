import logging
import tempfile
from pathlib import Path

from ado import (
    comment_exists_for_commit,
    fetch_pr_details,
    post_pr_comment,
    upload_pr_attachment,
)
from config import DEVOPS_DRYRUN, MAX_TASK_ATTEMPTS, RESULTS_DIR, STATE_TTL, rdb
from poller import enqueue_task
from runner import (
    parse_init_result,
    parse_pre_commit_result,
    parse_test_result,
    task_log_paths,
)
from tasks import bump_attempts, iter_task_commits, live_jobs, mark_task, task_states

log = logging.getLogger(__name__)

_TEST_ICON = {
    "passed": "✅",
    "failed": "❌",
    "unknown": "❌",
    "done": "ℹ️",
}
_PRE_COMMIT_ICON = {"ok": "✅", "ko": "❌"}
_INIT_ICON = {"ok": "✅", "ko": "❌"}
_INIT_LABEL = {"ok": "Initialization succeeded", "ko": "Initialization failed"}
_TEST_STATUS_LABEL = {
    "passed": "All tests passed",
    "failed": "Test failures detected",
    "unknown": "Test failures detected",
    "done": "Done",
}


def get_pr_id_for_commit(commit_hash):
    val = rdb.get(f"test:pr_id:{commit_hash}")
    return int(val) if val else None


def get_pr_desc_for_commit(commit_hash):
    val = rdb.get(f"test:pr_desc:{commit_hash}")
    return val.decode() if val else ""


def has_notified(commit_hash):
    return bool(rdb.get(f"test:notified:{commit_hash}"))


def mark_notified(commit_hash):
    rdb.setex(f"test:notified:{commit_hash}", STATE_TTL, "1")


def _build_combined_log(install_log_path, test_log_path):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    try:
        tmp.write(b"--- INSTALL.LOG ---\n")
        if install_log_path.exists():
            with open(install_log_path, "rb") as f:
                tmp.write(f.read())
        else:
            tmp.write(b"(not found)\n")
        tmp.write(b"\n--- TEST.LOG ---\n")
        if test_log_path.exists():
            with open(test_log_path, "rb") as f:
                tmp.write(f.read())
        else:
            tmp.write(b"(not found)\n")
    finally:
        tmp.close()
    return Path(tmp.name)


def notify_pr(commit_hash, force=False):
    h8 = commit_hash[:8]

    if not force and has_notified(commit_hash):
        return

    pr_id = get_pr_id_for_commit(commit_hash)
    if not pr_id:
        log.warning(f"[{h8}] No PR ID cached, skipping notification")
        return

    if not force and comment_exists_for_commit(pr_id, commit_hash):
        log.info(f"[{h8}] Comment already exists on PR#{pr_id}, skipping notification")
        mark_notified(commit_hash)
        return

    if not force:
        # Both of these are terminal, not transient: mark notified so the messenger,
        # which retries every MESSENGER_INTERVAL, stops reconsidering this commit.
        pr = fetch_pr_details(pr_id)
        if pr["status"] != "active":
            log.info(f"[{h8}] PR#{pr_id} is {pr['status']}, skipping notification")
            mark_notified(commit_hash)
            return
        if pr["head"] != commit_hash:
            current = (pr["head"] or "unknown")[:8]
            log.info(f"[{h8}] PR#{pr_id} HEAD is now {current}, skipping stale notification")
            mark_notified(commit_hash)
            return

    pre_commit_status = parse_pre_commit_result(commit_hash)
    pre_label = pre_commit_status.upper() if pre_commit_status else "N/A"
    pre_icon = (_PRE_COMMIT_ICON.get(pre_commit_status, "") + " ") if pre_commit_status else ""

    # The messenger reports as soon as every task is terminal, including a task that
    # crashed before writing anything. Distinguish "no test log at all" (⚠️ Not run) from
    # parse_test_result's "done" (it ran, but produced no runner summary line).
    test_status = parse_test_result(commit_hash)
    if (RESULTS_DIR / f"{commit_hash}.test.log").exists():
        test_icon = _TEST_ICON.get(test_status, "")
        test_label = _TEST_STATUS_LABEL.get(test_status, test_status)
    else:
        test_status = "unknown"  # so the install log gets attached below
        test_icon, test_label = "⚠️", "Not run"

    lines = [
        f"### Automated Test Report [HEAD {h8}]",
        "",
        "| Check | Result |",
        "|---|---|",
        f"| Pre-commit | {pre_icon}{pre_label} |",
        f"| Tests | {test_icon} {test_label} |",
    ]

    # The init test runs on every PR now, so always render the row: a missing init.log
    # means the task did not produce a result, which should be visible, not omitted.
    init_status = parse_init_result(commit_hash)
    init_icon = _INIT_ICON.get(init_status, "⚠️")
    init_label = _INIT_LABEL.get(init_status, "Not run")
    lines.append(f"| Initialization (live dump) | {init_icon} {init_label} |")

    attachment_lines = []

    if test_status in ("failed", "unknown") and not DEVOPS_DRYRUN:
        test_log = RESULTS_DIR / f"{commit_hash}.test.log"
        install_log = RESULTS_DIR / f"{commit_hash}.install.log"
        upload_path = (
            _build_combined_log(install_log, test_log)
            if test_status == "unknown"
            else (test_log if test_log.exists() else None)
        )
        if upload_path and upload_path.exists():
            try:
                att_url = upload_pr_attachment(pr_id, f"{h8}.test.txt", upload_path)
                if att_url:
                    attachment_lines.append(f"[Test log]({att_url})")
            except Exception as e:
                resp_body = getattr(getattr(e, "response", None), "text", None)
                log.warning(f"[{h8}] Could not upload test log: {e} | response: {resp_body}")
            finally:
                if test_status == "unknown":
                    upload_path.unlink(missing_ok=True)

    if init_status == "ko" and not DEVOPS_DRYRUN:
        init_log = RESULTS_DIR / f"{commit_hash}.init.log"
        if init_log.exists():
            try:
                att_url = upload_pr_attachment(pr_id, f"{h8}.init.txt", init_log)
                if att_url:
                    attachment_lines.append(f"[Init log]({att_url})")
            except Exception as e:
                resp_body = getattr(getattr(e, "response", None), "text", None)
                log.warning(f"[{h8}] Could not upload init log: {e} | response: {resp_body}")

    if pre_commit_status == "ko" and not DEVOPS_DRYRUN:
        pc_log = RESULTS_DIR / f"{commit_hash}.precommit.log"
        if pc_log.exists():
            try:
                att_url = upload_pr_attachment(pr_id, f"{h8}.precommit.txt", pc_log)
                if att_url:
                    attachment_lines.append(f"[Pre-commit log]({att_url})")
            except Exception as e:
                resp_body = getattr(getattr(e, "response", None), "text", None)
                log.warning(f"[{h8}] Could not upload pre-commit log: {e} | response: {resp_body}")

    if attachment_lines:
        lines.append("")
        lines.append("**Logs:** " + " | ".join(attachment_lines))

    lines.append("")
    lines.append("---")
    lines.append("*Automated comment by snappy-case-dashboard*")

    post_pr_comment(pr_id, "\n".join(lines))
    if not DEVOPS_DRYRUN:
        mark_notified(commit_hash)
    log.info(f"[{h8}] Posted test result comment on PR#{pr_id}")


def dispatch_ready():
    """Post the report for every commit whose whole task set has finished.

    Workers each run a single task and no longer notify; this runs as a thread on the
    single control replica, so exactly one process ever assembles and posts a comment,
    and only once all of the commit's tasks are terminal (never a partial report)."""
    for commit_hash in iter_task_commits():
        if has_notified(commit_hash):
            continue
        states = task_states(commit_hash)
        if not states or any(s != "done" for s in states.values()):
            continue
        try:
            notify_pr(commit_hash)
        except Exception as e:
            # Transient (ADO hiccup): leave it unmarked so the next pass retries.
            log.error(f"[{commit_hash[:8]}] Notification error: {e}")


def reap_dead_tasks():
    """Requeue tasks whose worker died mid-run.

    A SIGKILLed worker never marks its task done, which would leave dispatch_ready
    waiting on that commit forever. live_jobs() drops workers whose heartbeat lapsed;
    any task still 'running' but held by no live worker is retried. Its partial logs are
    deleted first, otherwise task_result_exists would short-circuit the retry."""
    running = {
        (j.get("commit"), j.get("task")) for j in live_jobs().values()
    }
    for commit_hash in iter_task_commits():
        for task, state in task_states(commit_hash).items():
            if state != "running" or (commit_hash, task) in running:
                continue
            attempts = bump_attempts(commit_hash, task)
            if attempts > MAX_TASK_ATTEMPTS:
                # Give up rather than loop forever: mark done so the report goes out,
                # with the missing log rendering as "Not run".
                mark_task(commit_hash, task, "done")
                log.error(
                    f"[{commit_hash[:8]}] {task} died {attempts} times, giving up"
                )
                continue
            for p in task_log_paths(commit_hash, task):
                p.unlink(missing_ok=True)
            enqueue_task(commit_hash, task, force=True)
            log.warning(
                f"[{commit_hash[:8]}] {task} worker died, requeued (attempt {attempts})"
            )
