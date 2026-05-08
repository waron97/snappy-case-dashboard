import logging
import os
import re
import subprocess
import threading
from pathlib import Path

from config import (
    ADDONS_DIR,
    DB_HOST,
    DB_PASSWORD,
    DB_USER,
    EXCLUDE,
    ODOO_BIN,
    ODOO_CONF,
    REPO_DIR,
    RESULTS_DIR,
    STATE_TTL,
    WORKER_ID,
    WORKERS_KEY,
    rdb,
)

log = logging.getLogger(__name__)

_RUNNER_RE = re.compile(r"odoo\.tests\.runner: (\d+) failed, (\d+) error\(s\)")
_PRE_COMMIT_RE = re.compile(r"PRE_COMMIT_STATUS: (OK|KO)")


def result_exists(commit_hash):
    return (RESULTS_DIR / f"{commit_hash}.install.log").exists() or (
        RESULTS_DIR / f"{commit_hash}.test.log"
    ).exists()


def parse_test_result(commit_hash):
    """Read last 16 KB of test.log, find runner summary. Returns 'passed', 'failed', 'done', or 'unknown'."""
    test_log = RESULTS_DIR / f"{commit_hash}.test.log"
    if not test_log.exists():
        return "done"
    try:
        with open(test_log, "rb") as f:
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


def all_phases_done(commit_hash):
    return (
        rdb.get(f"test:phase:{commit_hash}:tests") is not None
        and rdb.get(f"test:phase:{commit_hash}:precommit") is not None
    )


def vacuum(active_hashes):
    for f in RESULTS_DIR.glob("*.log"):
        h = f.name.split(".")[0]
        if h not in active_hashes:
            f.unlink()
            log.info(f"Vacuumed {f.name}")


def pg_env():
    return {"PGPASSWORD": DB_PASSWORD}


def remove_from_csv(csv_str, item):
    parts = [x for x in csv_str.split(",") if x and x != item]
    return ",".join(parts)


def run_cmd(cmd, env_extra=None, log_file=None, cwd=None):
    merged_env = {**os.environ, **(env_extra or {})}
    if log_file:
        with open(log_file, "ab") as f:
            return subprocess.run(
                cmd, env=merged_env, stdout=f, stderr=subprocess.STDOUT, cwd=cwd
            ).returncode
    return subprocess.run(cmd, env=merged_env, cwd=cwd).returncode


def run_pre_commit(commit_hash):
    """Run pre-commit checks and mark the Redis phase key. Safe to call as a thread target."""
    precommit_log = RESULTS_DIR / f"{commit_hash}.precommit.log"
    try:
        rc = run_cmd(
            ["python3", "-m", "pre_commit", "run", "--all-files"],
            log_file=precommit_log,
            cwd=str(REPO_DIR),
        )
        status = "OK" if rc == 0 else "KO"
        with open(precommit_log, "ab") as f:
            f.write(f"\nPRE_COMMIT_STATUS: {status}\n".encode())
        rdb.setex(f"test:phase:{commit_hash}:precommit", STATE_TTL, "done")
        log.info(f"[{commit_hash[:8]}] Pre-commit: {status}")
    except Exception as e:
        log.error(f"[{commit_hash[:8]}] Pre-commit error: {e}")
        try:
            with open(precommit_log, "ab") as f:
                f.write(f"\nPRE_COMMIT_ERROR: {e}\nPRE_COMMIT_STATUS: KO\n".encode())
        except OSError:
            pass
        rdb.setex(f"test:phase:{commit_hash}:precommit", STATE_TTL, "error")


def _run_odoo_tests(commit_hash):
    """Run DB setup + Odoo tests and mark the Redis phase key. Safe to call as a thread target."""
    db_name = f"odoo_{commit_hash[:12]}"
    install_log = RESULTS_DIR / f"{commit_hash}.install.log"
    test_log = RESULTS_DIR / f"{commit_hash}.test.log"

    try:
        subprocess.run(
            ["createdb", "-h", DB_HOST, "-U", DB_USER, db_name],
            env={**os.environ, **pg_env()},
            check=True,
        )

        log.info(f"[{commit_hash[:8]}] Initializing base module...")
        subprocess.run(
            [
                "python3", ODOO_BIN, "-c", ODOO_CONF, "-d", db_name,
                "-i", "base", "--stop-after-init", "--log-level=info",
            ],
            check=True,
        )

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

        depends_raw = subprocess.run(
            [
                "manifestoo", "--select-addons-dir", "/opt/odoo/addons",
                "--select-exclude", EXCLUDE, "list-depends", "--separator=,",
            ],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        depends_list = remove_from_csv(depends_raw, "base")

        addons_raw = subprocess.run(
            [
                "manifestoo", "--select-addons-dir", "/opt/odoo/addons",
                "--select-exclude", EXCLUDE, "list", "--separator=,",
            ],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        addons_list = remove_from_csv(addons_raw, "base")

        log.info(f"[{commit_hash[:8]}] {len(addons_list.split(','))} addons to test")

        if depends_list:
            log.info(f"[{commit_hash[:8]}] Installing dependencies...")
            run_cmd(
                [
                    "python3", ODOO_BIN, "-c", ODOO_CONF, "-d", db_name,
                    "-i", depends_list, "--stop-after-init", "--log-level=info",
                ],
                log_file=install_log,
            )

        if addons_list:
            log.info(f"[{commit_hash[:8]}] Running tests...")
            run_cmd(
                [
                    "python3", ODOO_BIN, "-c", ODOO_CONF, "-d", db_name,
                    "-i", addons_list, "--stop-after-init", "--log-level=info",
                    "--test-enable",
                ],
                log_file=test_log,
            )

        log.info(f"[{commit_hash[:8]}] Test run complete")
        rdb.setex(f"test:phase:{commit_hash}:tests", STATE_TTL, "done")

    except Exception as e:
        log.error(f"[{commit_hash[:8]}] Odoo tests failed: {e}")
        try:
            with open(test_log, "a") as f:
                f.write(f"\n\nORCHESTRATOR ERROR: {e}\n")
        except OSError:
            pass
        rdb.setex(f"test:phase:{commit_hash}:tests", STATE_TTL, "error")
    finally:
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", db_name],
            env={**os.environ, **pg_env()},
        )


def run_test(commit_hash):
    rdb.hset(WORKERS_KEY, WORKER_ID, commit_hash)
    log.info(f"Starting test run for {commit_hash}")

    try:
        # Serial setup: repo must be checked out before either thread starts
        subprocess.run(["git", "-C", str(REPO_DIR), "fetch", "--all"], check=True)
        subprocess.run(["git", "-C", str(REPO_DIR), "reset", "--hard", "HEAD"], check=True)
        subprocess.run(["git", "-C", str(REPO_DIR), "checkout", "-f", commit_hash], check=True)
        subprocess.run(
            [
                "rsync", "-a", "--delete", "--exclude=.git", "--exclude=symple_addons",
                str(REPO_DIR) + "/", str(ADDONS_DIR) + "/",
            ],
            check=True,
        )
        subprocess.run(
            "find /opt/odoo/addons -name 'requirements.txt' -not -path '*/symple_addons/*'"
            " -exec pip install --no-cache-dir -r {} \\; 2>/dev/null || true",
            shell=True,
        )
        subprocess.run(
            ["pip", "install", "cryptography==37.0.0", "pyopenssl==22.0.0", "paramiko<3.0"],
            check=True,
        )

        # Tests and pre-commit run in parallel
        t_tests = threading.Thread(
            target=_run_odoo_tests, args=(commit_hash,), name=f"tests-{commit_hash[:8]}"
        )
        t_precommit = threading.Thread(
            target=run_pre_commit, args=(commit_hash,), name=f"precommit-{commit_hash[:8]}"
        )
        t_tests.start()
        t_precommit.start()
        t_tests.join()
        t_precommit.join()

        # Safety: if a thread exited without setting its key, mark as error
        if rdb.get(f"test:phase:{commit_hash}:tests") is None:
            rdb.setex(f"test:phase:{commit_hash}:tests", STATE_TTL, "error")
        if rdb.get(f"test:phase:{commit_hash}:precommit") is None:
            rdb.setex(f"test:phase:{commit_hash}:precommit", STATE_TTL, "error")

    except Exception as e:
        log.error(f"[{commit_hash[:8]}] Setup failed: {e}")
        test_log = RESULTS_DIR / f"{commit_hash}.test.log"
        try:
            with open(test_log, "a") as f:
                f.write(f"\n\nSETUP ERROR: {e}\n")
        except OSError:
            pass
        rdb.setex(f"test:phase:{commit_hash}:tests", STATE_TTL, "error")
        rdb.setex(f"test:phase:{commit_hash}:precommit", STATE_TTL, "error")
        raise
    finally:
        rdb.hdel(WORKERS_KEY, WORKER_ID)
