import logging
import os
import subprocess

from flask import Flask, jsonify

from ado import fetch_open_prs, fetch_pr_details
from config import DB_HOST, DB_USER, QUEUE_KEY, RESULTS_DIR, WORKERS_KEY, rdb
from notifier import notify_pr
from poller import do_poll, enqueue
from runner import parse_pre_commit_result, parse_test_result, pg_env, result_exists

log = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/discover", methods=["POST"])
def api_discover():
    try:
        pr_count, enqueued = do_poll()
        return jsonify({"prs_found": pr_count, "enqueued": enqueued})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/status", methods=["GET"])
def api_status():
    workers_raw = rdb.hgetall(WORKERS_KEY)
    workers = {k.decode(): v.decode() for k, v in workers_raw.items()}
    queue = rdb.lrange(QUEUE_KEY, 0, -1)
    return jsonify(
        {
            "workers": workers,
            "queue": [h.decode() if isinstance(h, bytes) else h for h in queue],
        }
    )


@app.route("/prs", methods=["GET"])
def api_prs():
    try:
        prs = fetch_open_prs()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    workers_raw = rdb.hgetall(WORKERS_KEY)
    running_commits = {v.decode() for v in workers_raw.values()}
    result = []
    for pr in prs:
        commit = pr.get("lastMergeSourceCommit", {}).get("commitId")
        files_exist = bool(commit and result_exists(commit))
        if commit in running_commits:
            status = "running"
        elif files_exist:
            status = parse_test_result(commit)
        elif commit and rdb.lpos(QUEUE_KEY, commit) is not None:
            status = "queued"
        else:
            status = "pending"
        precommit_log_exists = bool(commit and (RESULTS_DIR / f"{commit}.precommit.log").exists())
        pre_commit_status = parse_pre_commit_result(commit) if precommit_log_exists else None
        result.append(
            {
                "id": pr.get("pullRequestId"),
                "title": pr.get("title"),
                "author": pr.get("createdBy", {}).get("displayName"),
                "sourceBranch": pr.get("sourceRefName", "").replace("refs/heads/", ""),
                "commitId": commit,
                "status": status,
                "preCommitStatus": pre_commit_status,
                "isDraft": pr.get("isDraft", False),
            }
        )
    return jsonify(result)


@app.route("/recheck/<commit_hash>", methods=["POST"])
def api_recheck(commit_hash):
    for suffix in ("install.log", "test.log", "precommit.log"):
        f = RESULTS_DIR / f"{commit_hash}.{suffix}"
        if f.exists():
            f.unlink()
    # Clear phase keys so notify guard resets
    rdb.delete(f"test:phase:{commit_hash}:tests")
    rdb.delete(f"test:phase:{commit_hash}:precommit")
    rdb.delete(f"test:notified:{commit_hash}")

    db_name = f"odoo_{commit_hash[:12]}"
    subprocess.run(
        ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", db_name],
        env={**os.environ, **pg_env()},
    )
    rdb.lrem(QUEUE_KEY, 0, commit_hash)
    rdb.lpush(QUEUE_KEY, commit_hash)
    log.info(f"Force-rechecked {commit_hash[:8]}, moved to front of queue")
    return jsonify({"queued": commit_hash})


@app.route("/recheck/pr/<int:pr_id>", methods=["POST"])
def api_recheck_pr(pr_id):
    details = fetch_pr_details(pr_id)
    commit_hash = details["head"]
    if not commit_hash:
        return jsonify({"error": "could not determine latest commit"}), 400

    for suffix in ("install.log", "test.log", "precommit.log"):
        f = RESULTS_DIR / f"{commit_hash}.{suffix}"
        if f.exists():
            f.unlink()
    rdb.delete(f"test:phase:{commit_hash}:tests")
    rdb.delete(f"test:phase:{commit_hash}:precommit")
    rdb.delete(f"test:notified:{commit_hash}")

    db_name = f"odoo_{commit_hash[:12]}"
    subprocess.run(
        ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", db_name],
        env={**os.environ, **pg_env()},
    )
    rdb.lrem(QUEUE_KEY, 0, commit_hash)
    rdb.lpush(QUEUE_KEY, commit_hash)
    log.info(f"Force-rechecked PR#{pr_id} → {commit_hash[:8]}, moved to front of queue")
    return jsonify({"queued": commit_hash})


@app.route("/notify/<commit_hash>", methods=["POST"])
def api_notify(commit_hash):
    try:
        notify_pr(commit_hash, force=True)
        return jsonify({"notified": commit_hash})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
