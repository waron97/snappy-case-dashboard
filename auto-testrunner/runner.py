import logging
import os
import re
import subprocess

from base_db import claim_pool_db, ensure_base_db
from config import (
    ADDONS_DIR,
    CONFIG_WF_ML_TEST_PREFIX,
    DB_HOST,
    DB_PASSWORD,
    DB_USER,
    EXCLUDE,
    ODOO_BIN,
    ODOO_CONF,
    ODOO_INIT_CONF,
    REPO_DIR,
    RESULTS_DIR,
    TARGET_BRANCH,
    TEST01_BASE_DB,
    TEST01_INIT_PATH_PREFIX,
)
from tasks import reset_tasks, set_stage
from upgrade import detect_changed_modules, installed_modules

log = logging.getLogger(__name__)

_RUNNER_RE = re.compile(r"odoo\.tests\.runner: (\d+) failed, (\d+) error\(s\)")
_PRE_COMMIT_RE = re.compile(r"PRE_COMMIT_STATUS: (OK|KO)")
_INIT_RE = re.compile(r"INIT_STATUS: (OK|KO)")


# Which log files each task produces. Doubles as the per-task idempotency marker: a
# worker that pops a task whose logs already exist skips it instead of redoing an hour
# of work, and the reaper deletes them before a retry so a partial log can't look done.
TASK_LOGS = {
    "tests": ("install.log", "test.log"),
    "precommit": ("precommit.log",),
    "init": ("init.log",),
}


def task_log_paths(commit_hash, task):
    return [RESULTS_DIR / f"{commit_hash}.{s}" for s in TASK_LOGS[task]]


def task_result_exists(commit_hash, task):
    return any(p.exists() for p in task_log_paths(commit_hash, task))


def result_exists(commit_hash):
    return task_result_exists(commit_hash, "tests")


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


def parse_init_result(commit_hash):
    """Read last 1 KB of init.log for INIT_STATUS sentinel. Returns 'ok', 'ko', or None."""
    init_log = RESULTS_DIR / f"{commit_hash}.init.log"
    if not init_log.exists():
        return None
    try:
        with open(init_log, "rb") as f:
            f.seek(max(0, init_log.stat().st_size - 1024))
            tail = f.read().decode("utf-8", errors="replace")
        m = _INIT_RE.search(tail)
        if m:
            return m.group(1).lower()
    except OSError:
        pass
    return None


def vacuum(active_hashes):
    stale = set()
    for f in RESULTS_DIR.glob("*.log"):
        h = f.name.split(".")[0]
        if h not in active_hashes:
            f.unlink()
            stale.add(h)
            log.info(f"Vacuumed {f.name}")
    for h in stale:
        reset_tasks(h)


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
    precommit_log = RESULTS_DIR / f"{commit_hash}.precommit.log"
    set_stage("running pre-commit hooks")
    rc = run_cmd(
        ["python3", "-m", "pre_commit", "run", "--all-files"],
        log_file=precommit_log,
        cwd=str(REPO_DIR),
    )
    status = "OK" if rc == 0 else "KO"
    with open(precommit_log, "ab") as f:
        f.write(f"\nPRE_COMMIT_STATUS: {status}\n".encode())
    return status.lower()


def _run_odoo_tests(commit_hash):
    db_name = f"odoo_{commit_hash[:12]}"
    install_log = RESULTS_DIR / f"{commit_hash}.install.log"
    test_log = RESULTS_DIR / f"{commit_hash}.test.log"

    try:
        set_stage(f"creating {db_name}")
        subprocess.run(
            ["createdb", "-h", DB_HOST, "-U", DB_USER, db_name],
            env={**os.environ, **pg_env()},
            check=True,
        )

        set_stage("installing base")
        subprocess.run(
            [
                "python3", ODOO_BIN, "-c", ODOO_CONF, "-d", db_name,
                "-i", "base", "--stop-after-init", "--log-level=info",
            ],
            check=True,
        )

        set_stage("activating it_IT")
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

        set_stage("resolving addon list")
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
            set_stage(f"installing {len(depends_list.split(','))} dependencies")
            run_cmd(
                [
                    "python3", ODOO_BIN, "-c", ODOO_CONF, "-d", db_name,
                    "-i", depends_list, "--stop-after-init", "--log-level=info",
                ],
                log_file=install_log,
            )

        if addons_list:
            set_stage(f"running tests on {len(addons_list.split(','))} addons")
            run_cmd(
                [
                    "python3", ODOO_BIN, "-c", ODOO_CONF, "-d", db_name,
                    "-i", addons_list, "--stop-after-init", "--log-level=info",
                    "--test-enable",
                ],
                log_file=test_log,
            )

        log.info(f"[{commit_hash[:8]}] Test run complete")

    except Exception as e:
        log.error(f"[{commit_hash[:8]}] Odoo tests failed: {e}")
        try:
            with open(test_log, "a") as f:
                f.write(f"\n\nORCHESTRATOR ERROR: {e}\n")
        except OSError:
            pass
        raise
    finally:
        set_stage(f"dropping {db_name}")
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", db_name],
            env={**os.environ, **pg_env()},
        )


def _write_init_status(init_log, status):
    with open(init_log, "ab") as f:
        f.write(f"\nINIT_STATUS: {status}\n".encode())


def rebase_onto_target():
    """Rebase the current detached HEAD (PR head) onto a fresh origin/TARGET_BRANCH so
    the init test runs the PR's config changes on top of the latest dev, matching a
    dump that may be newer than the PR's base. `git fetch --all` (in _prepare_checkout)
    already refreshed the remote ref.

    Returns (status, output) where status is 'clean', 'conflict', or 'error'. Replaying
    commits needs a committer identity, which a fresh clone has not got — pass one
    inline rather than relying on container-level git config. Anything that is not a
    real merge conflict is reported as 'error': calling it a conflict tells the author
    to go fix a rebase that was never actually attempted."""
    proc = subprocess.run(
        [
            "git", "-C", str(REPO_DIR),
            "-c", "user.name=auto-testrunner",
            "-c", "user.email=auto-testrunner@localhost",
            "rebase", f"origin/{TARGET_BRANCH}",
        ],
        capture_output=True, text=True,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    if proc.returncode == 0:
        return "clean", output
    conflicted = "CONFLICT" in output or "could not apply" in output
    subprocess.run(
        ["git", "-C", str(REPO_DIR), "rebase", "--abort"], capture_output=True
    )
    return ("conflict" if conflicted else "error"), output


def changed_config_modules(commit_hash):
    """Set of module names under config/ that the PR (commit vs its merge-base with
    the target branch) changed. Non-empty gates the init test; the same set scopes the
    -u so we only upgrade the workflow modules the PR touched, not the whole dev↔prod
    drift (which is huge, and pulls in migrations that need filestore/memory)."""
    try:
        base = subprocess.run(
            ["git", "-C", str(REPO_DIR), "merge-base", f"origin/{TARGET_BRANCH}", commit_hash],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        files = subprocess.run(
            ["git", "-C", str(REPO_DIR), "diff", "--name-only", base, commit_hash],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    except subprocess.CalledProcessError as e:
        log.warning(f"[{commit_hash[:8]}] Could not diff for config changes: {e}")
        return set()

    mods = set()
    for f in files:
        if not f.startswith(TEST01_INIT_PATH_PREFIX):
            continue
        parts = f.split("/")
        if len(parts) >= 2 and parts[1]:  # config/<module>/...
            mods.add(parts[1])
    return mods


def _config_wf_ml_test_modules():
    """config_wf_ml_* directories under ADDONS_DIR that contain a tests/ subfolder.
    Filesystem-based and PR-independent by design: this exercises the standing
    config_wf_ml_* + tests/ population on every init run, not just what the PR touched."""
    if not ADDONS_DIR.is_dir():
        return set()
    return {
        p.name for p in ADDONS_DIR.iterdir()
        if p.name.startswith(CONFIG_WF_ML_TEST_PREFIX) and (p / "tests").is_dir()
    }


def _run_init_test(commit_hash, config_mods):
    """Upgrade the PR's changed config/ modules on an isolated copy of the restored
    test-01 base DB, to verify initialization succeeds on production-like data."""
    init_log = RESULTS_DIR / f"{commit_hash}.init.log"

    # Grab a pre-warmed copy from the pool for an instant start; if the pool is empty,
    # fall back to an on-demand template copy so a run never blocks on an empty pool.
    copy_db = claim_pool_db(on_wait=lambda w: set_stage(f"waiting for warm DB ({w}s)"))
    try:
        if copy_db:
            set_stage(f"claimed {copy_db}")
        else:
            ensure_base_db("test-01")
            copy_db = f"init_{commit_hash[:12]}"
            set_stage(f"pool empty, copying template into {copy_db}")
            subprocess.run(
                ["createdb", "-h", DB_HOST, "-U", DB_USER, "-T", TEST01_BASE_DB, copy_db],
                env={**os.environ, **pg_env()},
                check=True,
            )

        # Upgrade every version-changed module, plus the PR's diffed config modules
        # that already exist (an XML-only change still needs -u). Config modules the PR
        # *adds* (not yet installed on the base) are installed instead with -i, so a
        # brand-new config_wf_* module is exercised too.
        set_stage("diffing module versions")
        changed = set(detect_changed_modules(ODOO_INIT_CONF, copy_db))
        installed = installed_modules(copy_db)
        to_upgrade = sorted(changed | (config_mods & installed))
        to_install = sorted(config_mods - installed)

        rc = 0
        if to_upgrade or to_install:
            set_stage(f"installing {len(to_install)} / upgrading {len(to_upgrade)} modules")
            with open(init_log, "ab") as f:
                f.write(f"INSTALL_MODULES: {','.join(to_install) or '(none)'}\n".encode())
                f.write(f"CHANGED_MODULES: {','.join(to_upgrade) or '(none)'}\n".encode())
            cmd = ["python3", ODOO_BIN, "-c", ODOO_INIT_CONF, "-d", copy_db]
            if to_install:
                cmd += ["-i", ",".join(to_install)]
            if to_upgrade:
                cmd += ["-u", ",".join(to_upgrade)]
            cmd += ["--stop-after-init", "--i18n-overwrite", "--log-level=info"]
            rc = run_cmd(cmd, log_file=init_log)
        else:
            log.info(f"[{commit_hash[:8]}] Init test: nothing to install or upgrade")
            with open(init_log, "ab") as f:
                f.write(b"No modules to install or upgrade.\n")

        # Second pass: -u/-i --test-enable, scoped to config_wf_ml_* modules with a
        # tests/ folder (none today). Only runs after a clean pass 1 (testing atop a
        # failed upgrade isn't meaningful) and only starts Odoo again if there's
        # something to test, so this is a no-op until such a module exists.
        test_rc = 0
        if rc == 0:
            installed = installed_modules(copy_db)
            test_mods = _config_wf_ml_test_modules()
            test_upgrade = sorted(test_mods & installed)
            test_install = sorted(test_mods - installed)
            if test_upgrade or test_install:
                set_stage(f"testing {len(test_mods)} config_wf_ml_* modules")
                with open(init_log, "ab") as f:
                    f.write(f"TEST_INSTALL_MODULES: {','.join(test_install) or '(none)'}\n".encode())
                    f.write(f"TEST_UPGRADE_MODULES: {','.join(test_upgrade) or '(none)'}\n".encode())
                test_cmd = ["python3", ODOO_BIN, "-c", ODOO_INIT_CONF, "-d", copy_db]
                if test_install:
                    test_cmd += ["-i", ",".join(test_install)]
                if test_upgrade:
                    test_cmd += ["-u", ",".join(test_upgrade)]
                test_cmd += [
                    "--stop-after-init", "--i18n-overwrite", "--log-level=info",
                    "--test-enable",
                ]
                test_rc = run_cmd(test_cmd, log_file=init_log)

        _write_init_status(init_log, "OK" if rc == 0 and test_rc == 0 else "KO")
        log.info(f"[{commit_hash[:8]}] Init test complete (rc={rc}, test_rc={test_rc})")

    except Exception as e:
        log.error(f"[{commit_hash[:8]}] Init test failed: {e}")
        try:
            with open(init_log, "a") as f:
                f.write(f"\n\nORCHESTRATOR ERROR: {e}\n")
            _write_init_status(init_log, "KO")
        except OSError:
            pass
    finally:
        # Copies are single-use: -u mutates them (partially, even on failure), so a
        # used copy can never return to the pool — always drop; the warmer replenishes.
        if copy_db:
            set_stage(f"dropping {copy_db}")
            subprocess.run(
                ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", copy_db],
                env={**os.environ, **pg_env()},
            )


def _rsync_addons(source_dir=REPO_DIR):
    """Mirror `source_dir` into ADDONS_DIR. Default caller is the PR checkout in
    REPO_DIR; instances.sync_local() reuses this with an arbitrary local folder as the
    source, same target and exclusions either way."""
    subprocess.run(
        [
            "rsync", "-a", "--delete", "--exclude=.git", "--exclude=symple_addons",
            str(source_dir) + "/", str(ADDONS_DIR) + "/",
        ],
        check=True,
    )


def _prepare_checkout(commit_hash, rsync_addons=True):
    """Shared prologue for every task: put REPO_DIR on the PR head, and for the tasks
    that run Odoo, mirror it into ADDONS_DIR. Each worker container owns a private
    /opt/repo and /opt/odoo/addons and runs one task at a time, so tasks of the same
    commit never collide here even though they run concurrently on different replicas."""
    set_stage("fetching repo")
    subprocess.run(["git", "-C", str(REPO_DIR), "fetch", "--all"], check=True)
    subprocess.run(["git", "-C", str(REPO_DIR), "reset", "--hard", "HEAD"], check=True)
    subprocess.run(["git", "-C", str(REPO_DIR), "checkout", "-f", commit_hash], check=True)
    if rsync_addons:
        set_stage("syncing addons")
        _rsync_addons()
    # GitHub outage workaround: skip pip installs temporarily
    # subprocess.run(
    #     "find /opt/odoo/addons -name 'requirements.txt' -not -path '*/symple_addons/*'"
    #     " -exec pip install --no-cache-dir -r {} \\; 2>/dev/null || true",
    #     shell=True,
    # )
    # subprocess.run(
    #     ["pip", "install", "cryptography==37.0.0", "pyopenssl==22.0.0", "paramiko<3.0"],
    #     check=True,
    # )


def run_tests_task(commit_hash):
    _prepare_checkout(commit_hash)
    _run_odoo_tests(commit_hash)


def run_precommit_task(commit_hash):
    # pre-commit reads REPO_DIR only, so skip the addons rsync entirely.
    _prepare_checkout(commit_hash, rsync_addons=False)
    try:
        result = run_pre_commit(commit_hash)
        log.info(f"[{commit_hash[:8]}] Pre-commit: {result}")
    except Exception as pre_err:
        log.error(f"[{commit_hash[:8]}] Pre-commit error: {pre_err}")
        precommit_log = RESULTS_DIR / f"{commit_hash}.precommit.log"
        with open(precommit_log, "ab") as f:
            f.write(f"\nPRE_COMMIT_ERROR: {pre_err}\nPRE_COMMIT_STATUS: KO\n".encode())


def run_init_task(commit_hash):
    _prepare_checkout(commit_hash)
    # Compute the PR's changed config modules BEFORE rebasing: it diffs explicit
    # merge-base..commit_hash refs, so it stays correct regardless of HEAD. The set no
    # longer gates the run (the init test is a fixture on every PR now) — it only scopes
    # which config/ modules get -i / -u inside _run_init_test.
    config_mods = changed_config_modules(commit_hash)
    # Rebase the PR onto the latest dev so init runs against code that matches a
    # (possibly newer) dump; conflicts fail the init test.
    set_stage(f"rebasing onto origin/{TARGET_BRANCH}")
    rebase, rebase_output = rebase_onto_target()
    if rebase != "clean":
        log.warning(f"[{commit_hash[:8]}] Init test: rebase onto {TARGET_BRANCH} -> {rebase}")
        init_log = RESULTS_DIR / f"{commit_hash}.init.log"
        reason = (
            "PR conflicts with the latest dev; resolve before merge."
            if rebase == "conflict"
            else "The rebase could not be run at all; this is a testrunner problem, "
            "not a problem with the PR."
        )
        with open(init_log, "ab") as f:
            f.write(f"Rebase onto origin/{TARGET_BRANCH} failed: {rebase}. {reason}\n".encode())
            f.write(b"\n--- git output ---\n")
            f.write(rebase_output.encode())
        _write_init_status(init_log, "KO")
        return
    # Re-sync the rebased tree so the init test reads the latest manifests and code
    # (rebase mutated REPO_DIR only, not ADDONS_DIR).
    set_stage("syncing addons")
    _rsync_addons()
    _run_init_test(commit_hash, config_mods)


TASK_RUNNERS = {
    "tests": run_tests_task,
    "precommit": run_precommit_task,
    "init": run_init_task,
}
