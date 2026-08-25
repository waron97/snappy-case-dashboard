import logging
import os
import subprocess
import time

from flask import Flask, jsonify, request

import base_db
import instances
from ado import fetch_open_prs, fetch_pr_details
from config import (
    DB_HOST,
    DB_USER,
    FAST_QUEUE_KEY,
    ODOO_CONF,
    QUEUE_KEY,
    RESULTS_DIR,
    SOURCES,
    TASKS,
    rdb,
)
from notifier import notify_pr
from poller import do_poll, enqueue_all
from runner import (
    parse_init_result,
    parse_pre_commit_result,
    parse_test_result,
    pg_env,
    result_exists,
    task_log_paths,
    task_result_exists,
)
from tasks import decode_job, encode_job, live_jobs, queue_for, reset_tasks, task_states
from upgrade import detect_changed_modules

log = logging.getLogger(__name__)
app = Flask(__name__)


def _queue_jobs(queue_key):
    jobs = []
    for raw in rdb.lrange(queue_key, 0, -1):
        commit, task = decode_job(raw)
        jobs.append({"commit": commit, "task": task})
    return jobs


@app.route("/discover", methods=["POST"])
def api_discover():
    try:
        pr_count, enqueued = do_poll()
        return jsonify({"prs_found": pr_count, "enqueued": enqueued})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/status", methods=["GET"])
def api_status():
    # `now` lets the UI render elapsed times against the server clock rather than the
    # browser's, which can be minutes off.
    return jsonify(
        {
            "now": time.time(),
            "workers": sorted(live_jobs().values(), key=lambda j: j.get("worker", "")),
            "queue": _queue_jobs(QUEUE_KEY),
            "fastQueue": _queue_jobs(FAST_QUEUE_KEY),
        }
    )


@app.route("/prs", methods=["GET"])
def api_prs():
    try:
        prs = fetch_open_prs()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    running_commits = {j.get("commit") for j in live_jobs().values()}
    result = []
    for pr in prs:
        commit = pr.get("lastMergeSourceCommit", {}).get("commitId")
        files_exist = bool(commit and result_exists(commit))
        if commit in running_commits:
            status = "running"
        elif files_exist:
            status = parse_test_result(commit)
        elif commit and _is_queued(commit):
            status = "queued"
        else:
            status = "pending"
        test_log_exists = bool(commit and (RESULTS_DIR / f"{commit}.test.log").exists())
        precommit_log_exists = bool(commit and (RESULTS_DIR / f"{commit}.precommit.log").exists())
        pre_commit_status = parse_pre_commit_result(commit) if precommit_log_exists else None
        init_log_exists = bool(commit and (RESULTS_DIR / f"{commit}.init.log").exists())
        init_status = parse_init_result(commit) if init_log_exists else None
        result.append(
            {
                "id": pr.get("pullRequestId"),
                "title": pr.get("title"),
                "author": pr.get("createdBy", {}).get("displayName"),
                "sourceBranch": pr.get("sourceRefName", "").replace("refs/heads/", ""),
                "commitId": commit,
                "status": status,
                # The tests task's own result. `status` above conflates it with "some
                # task of this commit is running", so the UI must not derive it from that.
                "testStatus": parse_test_result(commit) if test_log_exists else None,
                "preCommitStatus": pre_commit_status,
                "initStatus": init_status,
                "tasks": _task_view(commit, task_states(commit)) if commit else {},
                "isDraft": pr.get("isDraft", False),
            }
        )
    return jsonify(result)


def _task_view(commit_hash, states):
    """Per-task lifecycle state for the UI.

    `test:tasks:<commit>` only tracks the *current* run: a task whose logs already
    existed is never enqueued, so it has no entry there. Absence of an entry is not
    absence of a result — fall back to the log files, which are the durable record.
    A task with neither is genuinely untracked and is omitted."""
    view = {}
    for task in TASKS:
        state = states.get(task)
        if not state and task_result_exists(commit_hash, task):
            state = "done"
        if state:
            view[task] = state
    return view


def _is_queued(commit_hash):
    return any(
        rdb.lpos(queue_for(task), encode_job(commit_hash, task)) is not None
        for task in TASKS
    )


def _requeue_all(commit_hash):
    """Wipe every trace of a commit's previous run and re-queue all of its tasks at the
    front, so a manual recheck doesn't wait behind the backlog."""
    for task in TASKS:
        for p in task_log_paths(commit_hash, task):
            p.unlink(missing_ok=True)
    rdb.delete(f"test:notified:{commit_hash}")
    reset_tasks(commit_hash)

    for db_name in (f"odoo_{commit_hash[:12]}", f"init_{commit_hash[:12]}"):
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", db_name],
            env={**os.environ, **pg_env()},
        )
    return enqueue_all(commit_hash, force=True, front=True)


@app.route("/recheck/<commit_hash>", methods=["POST"])
def api_recheck(commit_hash):
    tasks = _requeue_all(commit_hash)
    log.info(f"Force-rechecked {commit_hash[:8]}, queued {tasks} at the front")
    return jsonify({"queued": commit_hash, "tasks": tasks})


@app.route("/recheck/pr/<int:pr_id>", methods=["POST"])
def api_recheck_pr(pr_id):
    details = fetch_pr_details(pr_id)
    commit_hash = details["head"]
    if not commit_hash:
        return jsonify({"error": "could not determine latest commit"}), 400
    tasks = _requeue_all(commit_hash)
    log.info(f"Force-rechecked PR#{pr_id} → {commit_hash[:8]}, queued {tasks} at the front")
    return jsonify({"queued": commit_hash, "tasks": tasks})


@app.route("/notify/<commit_hash>", methods=["POST"])
def api_notify(commit_hash):
    try:
        notify_pr(commit_hash, force=True)
        return jsonify({"notified": commit_hash})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- dev sources / db copies / the single Odoo instance ---------------------------


@app.route("/sources", methods=["GET"])
def api_sources():
    return jsonify(
        [
            {
                "id": source_id,
                "baseDb": source.base_db,
                "ready": base_db.base_ready(source_id),
                "resetting": base_db.is_resetting(source_id),
            }
            for source_id, source in SOURCES.items()
        ]
    )


@app.route("/sources/<source>/reset", methods=["POST"])
def api_reset_source(source):
    if source not in SOURCES:
        return jsonify({"error": f"unknown source {source!r}"}), 404
    if not base_db.reset_source_async(source):
        return jsonify({"error": "reset already in progress"}), 409
    return jsonify({"resetting": source})


@app.route("/copies", methods=["GET"])
def api_list_copies():
    return jsonify(base_db.list_copies())


@app.route("/copies", methods=["POST"])
def api_create_copy():
    body = request.get_json(force=True, silent=True) or {}
    try:
        db_name = base_db.create_copy(body.get("name", ""), body.get("source", ""))
    except (ValueError, RuntimeError) as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"created": db_name})


@app.route("/copies/<name>", methods=["DELETE"])
def api_delete_copy(name):
    instances.detach_if_attached(base_db.copy_db_name(name))
    base_db.delete_copy(name)
    return jsonify({"deleted": name})


@app.route("/instance", methods=["GET"])
def api_instance_status():
    return jsonify(instances.status())


@app.route("/instance/attach", methods=["POST"])
def api_instance_attach():
    body = request.get_json(force=True, silent=True) or {}
    name = body.get("name", "")
    db_name = base_db.copy_db_name(name)
    if not base_db.copy_exists(db_name):
        pending = next((c for c in base_db.list_copies() if c["name"] == db_name), None)
        if pending and pending["status"] == "creating":
            return jsonify({"error": f"copy {name!r} is still being created"}), 409
        return jsonify({"error": f"no such copy {name!r}"}), 404
    try:
        instances.attach(db_name, install=body.get("install") or None, upgrade=body.get("upgrade") or None)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify(instances.status())


@app.route("/instance/restart", methods=["POST"])
def api_instance_restart():
    body = request.get_json(force=True, silent=True) or {}
    try:
        instances.restart(install=body.get("install") or None, upgrade=body.get("upgrade") or None)
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify(instances.status())


@app.route("/instance/detach", methods=["POST"])
def api_instance_detach():
    instances.detach()
    return jsonify(instances.status())


@app.route("/instance/sync", methods=["POST"])
def api_instance_sync():
    body = request.get_json(force=True, silent=True) or {}
    pr_id = body.get("prId")
    if not isinstance(pr_id, int):
        return jsonify({"error": "prId (int) is required"}), 400
    try:
        result = instances.sync_pr(pr_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify(result)


@app.route("/instance/local-addons", methods=["GET"])
def api_instance_local_addons():
    return jsonify({"folders": instances.discover_addons_folders()})


@app.route("/instance/sync-local", methods=["POST"])
def api_instance_sync_local():
    body = request.get_json(force=True, silent=True) or {}
    path = body.get("path")
    if not path:
        return jsonify({"error": "path is required"}), 400
    try:
        result = instances.sync_local(path)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify(result)


@app.route("/instance/log", methods=["GET"])
def api_instance_log():
    return jsonify({"log": instances.tail_log()})


@app.route("/instance/suggested-upgrades", methods=["GET"])
def api_instance_suggested_upgrades():
    db_name = instances.status().get("db")
    if not db_name:
        return jsonify({"error": "no instance attached"}), 400
    try:
        modules = detect_changed_modules(ODOO_CONF, db_name)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"modules": modules})
