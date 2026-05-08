import logging
import tempfile
from pathlib import Path

from ado import (
    comment_exists_for_commit,
    fetch_pr_details,
    post_pr_comment,
    upload_pr_attachment,
)
from config import RESULTS_DIR, STATE_TTL, rdb
from runner import all_phases_done, parse_pre_commit_result, parse_test_result

log = logging.getLogger(__name__)

_TEST_ICON = {
    "passed": "✅",
    "failed": "❌",
    "unknown": "❌",
    "done": "ℹ️",
}
_PRE_COMMIT_ICON = {"ok": "✅", "ko": "❌"}
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

    if not force and not all_phases_done(commit_hash):
        log.info(f"[{h8}] Phases not all done yet, skipping notification")
        return

    if not force and comment_exists_for_commit(pr_id, commit_hash):
        log.info(f"[{h8}] Comment already exists on PR#{pr_id}, skipping notification")
        mark_notified(commit_hash)
        return

    if not force:
        pr = fetch_pr_details(pr_id)
        if pr["status"] != "active":
            log.info(f"[{h8}] PR#{pr_id} is {pr['status']}, skipping notification")
            return
        if pr["head"] != commit_hash:
            current = (pr["head"] or "unknown")[:8]
            log.info(f"[{h8}] PR#{pr_id} HEAD is now {current}, skipping stale notification")
            return

    test_status = parse_test_result(commit_hash)
    pre_commit_status = parse_pre_commit_result(commit_hash)
    pre_label = pre_commit_status.upper() if pre_commit_status else "N/A"
    pre_icon = (_PRE_COMMIT_ICON.get(pre_commit_status, "") + " ") if pre_commit_status else ""
    test_icon = _TEST_ICON.get(test_status, "")
    test_label = _TEST_STATUS_LABEL.get(test_status, test_status)

    lines = [
        f"### Automated Test Report [HEAD {h8}]",
        "",
        "| Check | Result |",
        "|---|---|",
        f"| Pre-commit | {pre_icon}{pre_label} |",
        f"| Tests | {test_icon} {test_label} |",
    ]

    attachment_lines = []

    if test_status in ("failed", "unknown"):
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

    if pre_commit_status == "ko":
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
    mark_notified(commit_hash)
    log.info(f"[{h8}] Posted test result comment on PR#{pr_id}")
