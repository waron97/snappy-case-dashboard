import base64
import logging
import os
import re
import subprocess
import threading
import time
from pathlib import Path

import redis
import requests
from flask import Flask, jsonify

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

DEVOPS_ORG = os.environ["DEVOPS_ORG"]
DEVOPS_PROJECT = os.environ["DEVOPS_PROJECT"]
DEVOPS_REPO = os.environ["DEVOPS_REPO"]
DEVOPS_ACCESS_TOKEN = os.environ["DEVOPS_ACCESS_TOKEN"]
REDIS_URL = os.environ.get("REDIS_URL", "redis://redis:6379")
RESULTS_DIR = Path(os.environ.get("RESULTS_DIR", "/results"))

REPO_DIR = Path("/opt/repo")
ADDONS_DIR = Path("/opt/odoo/addons")
ODOO_BIN = "/opt/odoo/base/odoo-bin"
ODOO_CONF = "/opt/odoo/odoo.conf"

POLL_INTERVAL = 300  # 5 minutes
QUEUE_KEY = "test:queue"
CURRENT_KEY = "test:current"
EXCLUDE = "symple_address_city_and_province_it,symple_contacts_default_data,sorgenia_imperex_metadata,sorgenia_ml_install_all"

DB_HOST = "postgres"
DB_USER = "odoo"
DB_PASSWORD = os.environ.get("DB_PASSWORD", "odoo")

rdb = redis.from_url(REDIS_URL)
app = Flask(__name__)
_poll_lock = threading.Lock()


def ado_headers():
    token = base64.b64encode(f":{DEVOPS_ACCESS_TOKEN}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def fetch_open_prs():
    url = (
        f"https://dev.azure.com/{DEVOPS_ORG}/{DEVOPS_PROJECT}"
        f"/_apis/git/repositories/{DEVOPS_REPO}/pullrequests"
        f"?searchCriteria.status=active&searchCriteria.targetRefName=refs/heads/15.0-dev&api-version=7.0"
    )
    resp = requests.get(url, headers=ado_headers(), timeout=30)
    resp.raise_for_status()
    return resp.json().get("value", [])


def result_exists(commit_hash):
    return (RESULTS_DIR / f"{commit_hash}.install.log").exists() or (
        RESULTS_DIR / f"{commit_hash}.test.log"
    ).exists()


_RUNNER_RE = re.compile(r"odoo\.tests\.runner: (\d+) failed, (\d+) error\(s\)")
_PRE_COMMIT_RE = re.compile(r"PRE_COMMIT_STATUS: (OK|KO)")


def parse_test_result(commit_hash):
    """Read last 200 lines of test.log, find runner summary. Returns 'passed', 'failed', or 'done'."""
    test_log = RESULTS_DIR / f"{commit_hash}.test.log"
    if not test_log.exists():
        return "done"
    try:
        with open(test_log, "rb") as f:
            # Read last 16 KB — runner summary is always near the end
            f.seek(max(0, test_log.stat().st_size - 16384))
            tail = f.read().decode("utf-8", errors="replace")
        for line in reversed(tail.splitlines()):
            m = _RUNNER_RE.search(line)
            if m:
                failed, errors = int(m.group(1)), int(m.group(2))
                return "passed" if failed == 0 and errors == 0 else "failed"
    except OSError:
        pass
    return "unknown"


def parse_pre_commit_result(commit_hash):
    """Read last 1 KB of precommit.log for PRE_COMMIT_STATUS sentinel. Returns 'ok', 'ko', or None."""
    precommit_log = RESULTS_DIR / f"{commit_hash}.precommit.log"
    if not precommit_log.exists():
        return None
    try:
        with open(precommit_log, "rb") as f:
            f.seek(max(0, precommit_log.stat().st_size - 1024))
            tail = f.read().decode("utf-8", errors="replace")
        m = _PRE_COMMIT_RE.search(tail)
        if m:
            return m.group(1).lower()
    except OSError:
        pass
    return None


def enqueue(commit_hash):
    if result_exists(commit_hash):
        return
    if rdb.lpos(QUEUE_KEY, commit_hash) is not None:
        return
    rdb.rpush(QUEUE_KEY, commit_hash)
    log.info(f"Enqueued {commit_hash}")


def vacuum(active_hashes):
    for f in RESULTS_DIR.glob("*.log"):
        h = f.name.split(".")[0]
        if h not in active_hashes:
            f.unlink()
            log.info(f"Vacuumed {f.name}")


def do_poll():
    with _poll_lock:
        prs = fetch_open_prs()
        log.info(f"Found {len(prs)} open PRs")
        active = {pr.get("lastMergeSourceCommit", {}).get("commitId") for pr in prs} - {
            None
        }
        vacuum(active)
        enqueued = []
        for commit in active:
            before = rdb.llen(QUEUE_KEY)
            enqueue(commit)
            if rdb.llen(QUEUE_KEY) > before:
                enqueued.append(commit)
        return len(prs), enqueued


def poller():
    while True:
        try:
            do_poll()
        except Exception as e:
            log.error(f"Poller error: {e}")
        time.sleep(POLL_INTERVAL)


@app.route("/discover", methods=["POST"])
def api_discover():
    try:
        pr_count, enqueued = do_poll()
        return jsonify({"prs_found": pr_count, "enqueued": enqueued})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/status", methods=["GET"])
def api_status():
    current = rdb.get(CURRENT_KEY)
    queue = rdb.lrange(QUEUE_KEY, 0, -1)
    return jsonify(
        {
            "current": current.decode() if current else None,
            "queue": [h.decode() if isinstance(h, bytes) else h for h in queue],
        }
    )


@app.route("/prs", methods=["GET"])
def api_prs():
    try:
        prs = fetch_open_prs()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    current = rdb.get(CURRENT_KEY)
    current = current.decode() if current else None
    result = []
    for pr in prs:
        commit = pr.get("lastMergeSourceCommit", {}).get("commitId")
        files_exist = bool(commit and result_exists(commit))
        if commit == current:
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
    # Delete existing result files
    for suffix in ("install.log", "test.log", "precommit.log"):
        f = RESULTS_DIR / f"{commit_hash}.{suffix}"
        if f.exists():
            f.unlink()

    db_name = f"odoo_{commit_hash[:12]}"
    subprocess.run(
        ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", db_name],
        env={**os.environ, **pg_env()},
    )
    # Remove from queue if already pending, then push to front
    rdb.lrem(QUEUE_KEY, 0, commit_hash)
    rdb.lpush(QUEUE_KEY, commit_hash)
    log.info(f"Force-rechecked {commit_hash[:8]}, moved to front of queue")
    return jsonify({"queued": commit_hash})


@app.route("/recheck/pr/<int:pr_id>", methods=["POST"])
def api_recheck_pr(pr_id):
    url = (
        f"https://dev.azure.com/{DEVOPS_ORG}/{DEVOPS_PROJECT}"
        f"/_apis/git/repositories/{DEVOPS_REPO}/pullrequests/{pr_id}"
        f"?api-version=7.0"
    )
    resp = requests.get(url, headers=ado_headers(), timeout=30)
    resp.raise_for_status()
    commit_hash = resp.json().get("lastMergeSourceCommit", {}).get("commitId")
    if not commit_hash:
        return jsonify({"error": "could not determine latest commit"}), 400

    for suffix in ("install.log", "test.log", "precommit.log"):
        f = RESULTS_DIR / f"{commit_hash}.{suffix}"
        if f.exists():
            f.unlink()

    db_name = f"odoo_{commit_hash[:12]}"
    subprocess.run(
        ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", db_name],
        env={**os.environ, **pg_env()},
    )
    rdb.lrem(QUEUE_KEY, 0, commit_hash)
    rdb.lpush(QUEUE_KEY, commit_hash)
    log.info(f"Force-rechecked PR#{pr_id} → {commit_hash[:8]}, moved to front of queue")
    return jsonify({"queued": commit_hash})


def run_cmd(cmd, env_extra=None, log_file=None, cwd=None):
    merged_env = {**os.environ, **(env_extra or {})}
    if log_file:
        with open(log_file, "ab") as f:
            return subprocess.run(
                cmd, env=merged_env, stdout=f, stderr=subprocess.STDOUT, cwd=cwd
            ).returncode
    return subprocess.run(cmd, env=merged_env, cwd=cwd).returncode


def run_pre_commit(commit_hash):
    precommit_log = RESULTS_DIR / f"{commit_hash}.precommit.log"
    rc = run_cmd(
        ["pre-commit", "run", "--all-files"],
        log_file=precommit_log,
        cwd=str(REPO_DIR),
    )
    status = "OK" if rc == 0 else "KO"
    with open(precommit_log, "ab") as f:
        f.write(f"\nPRE_COMMIT_STATUS: {status}\n".encode())
    return status.lower()


def pg_env():
    return {"PGPASSWORD": DB_PASSWORD}


def remove_from_csv(csv_str, item):
    parts = [x for x in csv_str.split(",") if x and x != item]
    return ",".join(parts)


def run_test(commit_hash):
    db_name = f"odoo_{commit_hash[:12]}"
    install_log = RESULTS_DIR / f"{commit_hash}.install.log"
    test_log = RESULTS_DIR / f"{commit_hash}.test.log"

    rdb.set(CURRENT_KEY, commit_hash)
    log.info(f"Starting test run for {commit_hash}")

    # Checkout commit and sync to addons dir (preserve baked-in submodule dirs)
    subprocess.run(["git", "-C", str(REPO_DIR), "fetch", "--all"], check=True)
    subprocess.run(["git", "-C", str(REPO_DIR), "checkout", commit_hash], check=True)
    # Sync repo → addons dir; symple_addons excluded (baked at /opt/odoo/symple_addons/)
    # Nested dirs (config/, OCA/) are kept so odoo.conf addons_path can resolve deps.
    subprocess.run(
        [
            "rsync",
            "-a",
            "--delete",
            "--exclude=.git",
            "--exclude=symple_addons",
            str(REPO_DIR) + "/",
            str(ADDONS_DIR) + "/",
        ],
        check=True,
    )

    # Install pip requirements from custom addons only
    subprocess.run(
        "find /opt/odoo/addons -name 'requirements.txt' -not -path '*/symple_addons/*'"
        " -exec pip install --no-cache-dir -r {} \\; 2>/dev/null || true",
        shell=True,
    )
    subprocess.run(
        ["pip", "install", "cryptography==37.0.0", "pyopenssl==22.0.0", "paramiko<3.0"],
        check=True,
    )

    # Create fresh database
    subprocess.run(
        ["createdb", "-h", DB_HOST, "-U", DB_USER, db_name],
        env={**os.environ, **pg_env()},
        check=True,
    )

    try:
        # Init base module
        log.info(f"[{commit_hash[:8]}] Initializing base module...")
        subprocess.run(
            [
                "python3",
                ODOO_BIN,
                "-c",
                ODOO_CONF,
                "-d",
                db_name,
                "-i",
                "base",
                "--stop-after-init",
                "--log-level=info",
            ],
            check=True,
        )

        # Activate it_IT language
        lang_script = (
            "lang = env['res.lang'].search([('code', '=', 'it_IT')], limit=1)\n"
            "if lang:\n    lang.active = True\n"
            "else:\n    env['res.lang']._activate_lang('it_IT')\n"
        )
        subprocess.run(
            ["python3", ODOO_BIN, "shell", "-c", ODOO_CONF, "-d", db_name],
            input=lang_script.encode(),
            capture_output=True,
        )

        # Discover addons via manifestoo
        depends_raw = subprocess.run(
            [
                "manifestoo",
                "--select-addons-dir",
                "/opt/odoo/addons",
                "--select-exclude",
                EXCLUDE,
                "list-depends",
                "--separator=,",
            ],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        depends_list = remove_from_csv(depends_raw, "base")

        addons_raw = subprocess.run(
            [
                "manifestoo",
                "--select-addons-dir",
                "/opt/odoo/addons",
                "--select-exclude",
                EXCLUDE,
                "list",
                "--separator=,",
            ],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        addons_list = remove_from_csv(addons_raw, "base")

        log.info(f"[{commit_hash[:8]}] {len(addons_list.split(','))} addons to test")

        # Install dependencies → install.log
        if depends_list:
            log.info(f"[{commit_hash[:8]}] Installing dependencies...")
            run_cmd(
                [
                    "python3",
                    ODOO_BIN,
                    "-c",
                    ODOO_CONF,
                    "-d",
                    db_name,
                    "-i",
                    depends_list,
                    "--stop-after-init",
                    "--log-level=info",
                ],
                log_file=install_log,
            )

        # Install addons + run tests → test.log
        if addons_list:
            log.info(f"[{commit_hash[:8]}] Running tests...")
            run_cmd(
                [
                    "python3",
                    ODOO_BIN,
                    "-c",
                    ODOO_CONF,
                    "-d",
                    db_name,
                    "-i",
                    addons_list,
                    "--stop-after-init",
                    "--log-level=info",
                    "--test-enable",
                ],
                log_file=test_log,
            )

        log.info(f"[{commit_hash[:8]}] Test run complete")

        log.info(f"[{commit_hash[:8]}] Running pre-commit checks...")
        try:
            result = run_pre_commit(commit_hash)
            log.info(f"[{commit_hash[:8]}] Pre-commit: {result}")
        except Exception as pre_err:
            log.error(f"[{commit_hash[:8]}] Pre-commit error: {pre_err}")
            precommit_log = RESULTS_DIR / f"{commit_hash}.precommit.log"
            with open(precommit_log, "ab") as f:
                f.write(f"\nPRE_COMMIT_ERROR: {pre_err}\nPRE_COMMIT_STATUS: KO\n".encode())

    except Exception as e:
        log.error(f"[{commit_hash[:8]}] Test run failed: {e}")
        with open(test_log, "a") as f:
            f.write(f"\n\nORCHESTRATOR ERROR: {e}\n")
        raise
    finally:
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", db_name],
            env={**os.environ, **pg_env()},
        )
        rdb.delete(CURRENT_KEY)


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
            run_test(commit_hash)
        except Exception as e:
            log.error(f"Worker error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    t_poller = threading.Thread(target=poller, daemon=True, name="poller")
    t_poller.start()
    log.info("Poller started (interval: 5 min)")

    t_api = threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=8765, use_reloader=False),
        daemon=True,
        name="api",
    )
    t_api.start()
    log.info("API started on :8080")

    log.info("Worker starting...")
    worker()
