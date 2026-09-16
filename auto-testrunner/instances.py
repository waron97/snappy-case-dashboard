"""Manage the single Odoo dev-server process control may run at a time, always on
config.ODOO_PORT. Attaching stops whatever is running and starts a fresh
`odoo-bin -c ODOO_CONF -d <db>` (no --stop-after-init — it must stay up serving).

State is in-memory only: control is a single-process, single-replica role (unlike the
worker pool), and any previous subprocess is gone the moment the container restarts, so
there is nothing worth persisting across a restart — reset_to_stopped_on_boot() is
called at control startup precisely to avoid ever reporting a stale "running" state for
a process that no longer exists.
"""

import logging
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

import requests

from ado import fetch_pr_details
from config import (
    DEVOPS_ORG,
    DEVOPS_PROJECT,
    DEVOPS_REPO,
    INSTANCE_LOG_PATH,
    LOCAL_CODE_ROOT,
    LOCAL_SCAN_MAX_DEPTH,
    JAEGER_UI_URL,
    ODOO_BIN,
    ODOO_CONF,
    ODOO_PORT,
    OTEL_EXPORTER_OTLP_ENDPOINT,
    REPO_DIR,
    TARGET_BRANCH,
)
from runner import _prepare_checkout, _rsync_addons

log = logging.getLogger(__name__)

HEALTH_TIMEOUT = 3600  # generous backstop against a genuine hang, not a normal-case bound: a
# real crash is caught immediately by _watch() regardless of this value, and a large -u
# (e.g. "-u all") can legitimately run for a long time before Odoo ever opens its port —
# this only exists to eventually give up on a process that's alive but truly stuck.
STOP_TIMEOUT = 15  # seconds to wait for a graceful terminate before kill

# Opt-in request tracing (see profiling/sitecustomize.py): traces ORM method calls
# (odoo.models.BaseModel.<method>), so it fires regardless of whether the call came from the
# web client, an external XML-RPC/JSON-RPC caller, or internal Python code. "methods"
# defaults to "read" to match the symptom this was built for; clear it to trace every
# BaseModel method that can plausibly touch the DB (sitecustomize.py excludes the zero-IO
# recordset helpers like browse/sudo/filtered), or clear "model" too to do that across every
# model.
PROFILE_DEFAULTS = {"enabled": False, "model": "", "methods": "read"}

_lock = threading.Lock()
_proc = None  # subprocess.Popen of the current odoo-bin, or None
_state = {
    "status": "stopped",  # stopped | starting | running | error
    "db": None,
    "install": None,
    "upgrade": None,
    "syncedPr": None,
    "syncedCommit": None,
    "syncedLocal": None,  # relative path under LOCAL_CODE_ROOT, mutually exclusive with syncedPr
    "startedAt": None,
    "error": None,
    "profile": dict(PROFILE_DEFAULTS),
}


def status():
    with _lock:
        view = dict(_state)
    view["url"] = f"http://localhost:{ODOO_PORT}" if view["status"] == "running" else None
    # Static regardless of instance/Jaeger state — the UI only shows it when profile.enabled.
    view["jaegerUrl"] = JAEGER_UI_URL
    return view


def _stop_locked():
    """Caller must hold _lock. Stops the current process, if any, synchronously."""
    global _proc
    if _proc is None:
        return
    proc, _proc = _proc, None
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=STOP_TIMEOUT)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()


def _watch(proc):
    """Flip status to 'error' if the process dies on its own (crash, bad -u, DB error)
    while it's still the one we think is current."""
    proc.wait()
    with _lock:
        if _proc is proc:
            _state["status"] = "error"
            _state["error"] = f"odoo-bin exited unexpectedly (rc={proc.returncode})"
            log.error(f"Odoo instance on {_state['db']} died: rc={proc.returncode}")


def _wait_healthy():
    """Poll an actual HTTP request until Odoo answers without a 5xx, or HEALTH_TIMEOUT
    elapses. A bare TCP connect isn't enough: werkzeug binds the port successfully even
    when the WSGI app itself is broken (e.g. a missing addons_path entry before any PR
    has been synced) and 500s on every real request — that must show as "error", not
    "running"."""
    deadline = time.time() + HEALTH_TIMEOUT
    while time.time() < deadline:
        with _lock:
            if _state["status"] != "starting":
                return  # _watch already flipped it to "error"
        try:
            resp = requests.get(f"http://127.0.0.1:{ODOO_PORT}/web/login", timeout=2)
            if resp.status_code < 500:
                with _lock:
                    if _state["status"] == "starting":
                        _state["status"] = "running"
                return
        except requests.RequestException:
            pass
        time.sleep(1)
    with _lock:
        if _state["status"] == "starting":
            _state["status"] = "error"
            _state["error"] = f"Odoo did not answer :{ODOO_PORT} without a server error within {HEALTH_TIMEOUT}s"


def attach(db_name, install=None, upgrade=None, profile=None):
    """Stop whatever's running and start odoo-bin against db_name, then return
    immediately with status 'starting' — -i/-u are applied at startup before Odoo opens
    its port, and a large upgrade (e.g. -u all) can legitimately take far longer than
    any single HTTP request should stay open for (Flask's dev server is also
    single-threaded, so blocking here would stall every other request too). The health
    check runs in the background instead; poll GET /instance to see it resolve to
    'running' or 'error'.

    `profile` is an optional partial dict ({"enabled": ..., "model": ..., "methods": ...})
    merged over the last-used profiling config — None (or a partial dict) preserves
    whatever wasn't given, same "don't silently clear it" convention as install/upgrade in
    restart() below, just merged per-key instead of whole-value since this is UI toggle
    state rather than a one-shot CLI flag."""
    global _proc
    with _lock:
        _stop_locked()
        # "-u" here is Python's own unbuffered-stdio flag, not Odoo's module-upgrade
        # flag (that one's added below, as its own argv entry). Without it, redirecting
        # stdout to a plain file (rather than a TTY) switches C stdio to fully-buffered
        # mode, so the live log tail would only show output in long-delayed chunks.
        # --max-cron-threads=0: this is a local inspection instance on restored,
        # possibly stale data — scheduled jobs (mailings, dunning, dashboards) have
        # overdue nextcall times and would all fire at once on boot, both risking real
        # side effects on test data and exhausting Odoo's own internal db connection
        # pool (default 64) well before Postgres's own max_connections is anywhere
        # near full.
        # Odoo's default memory cap (~2/2.5 GB soft/hard via RLIMIT_AS) is sized for a
        # prefork worker, not a single process loading this monorepo's full ~480-module
        # registry plus first-time asset compilation — it trips MemoryError mid-request
        # well before the host is under any real memory pressure. Same fix as
        # base_db.generate_init_conf() applies to workers' -u runs, via CLI flags here
        # instead of the shared odoo.conf since this is control's own one-off process.
        cmd = [
            sys.executable, "-u", ODOO_BIN, "-c", ODOO_CONF, "-d", db_name,
            "--max-cron-threads=0",
            "--limit-memory-soft=0", "--limit-memory-hard=0",
        ]
        if install:
            cmd += ["-i", install]
        if upgrade:
            cmd += ["-u", upgrade]

        profile_cfg = {**_state["profile"], **(profile or {})}
        env = None
        if profile_cfg["enabled"]:
            # Only touch the child's environment at all when tracing is on: the unprofiled
            # path must inherit the parent environment exactly as before (env=None does
            # this natively), so a profiling bug in this branch can't affect normal usage.
            env = dict(os.environ)
            env["ODOO_PROFILE_ENABLED"] = "1"
            env["ODOO_PROFILE_MODEL"] = profile_cfg["model"] or ""
            env["ODOO_PROFILE_METHODS"] = profile_cfg["methods"] or ""
            env["OTEL_EXPORTER_OTLP_ENDPOINT"] = OTEL_EXPORTER_OTLP_ENDPOINT
            profiling_dir = str(Path(__file__).resolve().parent / "profiling")
            env["PYTHONPATH"] = os.pathsep.join(filter(None, [profiling_dir, env.get("PYTHONPATH", "")]))

        _state.update(
            status="starting", db=db_name, install=install, upgrade=upgrade,
            error=None, startedAt=time.time(), profile=profile_cfg,
        )
        with open(INSTANCE_LOG_PATH, "wb") as log_f:
            # The child inherits its own duplicated fd, so closing our end (via the
            # `with` block) as soon as Popen returns doesn't affect its writes and
            # avoids leaking a parent-side fd on every attach/restart.
            _proc = subprocess.Popen(cmd, stdout=log_f, stderr=subprocess.STDOUT, env=env)
        threading.Thread(target=_watch, args=(_proc,), daemon=True, name="instance-watch").start()
        threading.Thread(target=_wait_healthy, daemon=True, name="instance-health").start()


def restart(install=None, upgrade=None, profile=None):
    """Re-sync from whichever source is currently active — the PR's latest head commit,
    or the mounted local folder — before relaunching, so a restart always reflects the
    freshest code rather than whatever was on disk at the last explicit sync. (For a PR,
    re-sync also re-resolves the PR to its current head, picking up any new commits
    pushed since the last sync — the same "pull fresh data" semantics as the initial
    sync, not just a fixed commit replay.) None for install/upgrade keeps the last-used
    value, so a plain restart doesn't silently clear it — this doubles as the UI's
    'apply -u' button. profile=None keeps the last-used profiling config too — attach()
    itself merges it over _state["profile"], so there's nothing to re-fetch here."""
    with _lock:
        db = _state["db"]
        if not db:
            raise RuntimeError("no instance attached")
        if install is None:
            install = _state["install"]
        if upgrade is None:
            upgrade = _state["upgrade"]
        pr_id = _state["syncedPr"]
        local_path = _state["syncedLocal"]

    if pr_id is not None:
        sync_pr(pr_id)
    elif local_path is not None:
        sync_local(local_path)

    attach(db, install=install, upgrade=upgrade, profile=profile)


def detach():
    with _lock:
        _stop_locked()
        # profile resets too: it's investigation-specific and shouldn't leak onto whatever
        # gets attached next.
        _state.update(
            status="stopped", db=None, install=None, upgrade=None, error=None, startedAt=None,
            profile=dict(PROFILE_DEFAULTS),
        )


def detach_if_attached(db_name):
    """No-op unless db_name is the currently attached copy. Called before deleting a
    copy, so dropping an attached DB out from under a live Odoo process can't happen."""
    with _lock:
        current = _state["db"]
    if current == db_name:
        detach()


def reset_to_stopped_on_boot():
    with _lock:
        _state.update(
            status="stopped", db=None, install=None, upgrade=None,
            syncedPr=None, syncedCommit=None, syncedLocal=None, startedAt=None, error=None,
            profile=dict(PROFILE_DEFAULTS),
        )


def _ensure_repo_cloned():
    """Workers get their /opt/repo clone from startup.sh; control never has — this is
    the first control-side feature that needs one, so clone lazily on first sync."""
    if (REPO_DIR / ".git").is_dir():
        return
    log.info("Cloning repository for PR sync (first sync on this container)...")
    repo_url = f"git@ssh.dev.azure.com:v3/{DEVOPS_ORG}/{DEVOPS_PROJECT}/{DEVOPS_REPO}"
    subprocess.run(["git", "clone", "--branch", TARGET_BRANCH, repo_url, str(REPO_DIR)], check=True)


def sync_pr(pr_id):
    """Check out an open PR's head commit into control's own /opt/repo and rsync it
    into control's /opt/odoo/addons — the same checkout mechanism workers already use
    for testing (runner._prepare_checkout), applied to control for the first time."""
    details = fetch_pr_details(pr_id)
    commit_hash = details.get("head")
    if not commit_hash:
        raise RuntimeError(f"could not resolve PR #{pr_id}'s head commit")
    _ensure_repo_cloned()
    _prepare_checkout(commit_hash, rsync_addons=True)
    with _lock:
        _state["syncedPr"] = pr_id
        _state["syncedCommit"] = commit_hash
        _state["syncedLocal"] = None  # mutually exclusive with a local sync
    return {"prId": pr_id, "commit": commit_hash}


def _has_manifest_child(path):
    """True if `path` directly contains at least one subdirectory with __manifest__.py
    (i.e. `path` itself is usable as one addons_path entry)."""
    try:
        with os.scandir(path) as it:
            for entry in it:
                if not entry.is_dir(follow_symlinks=False) or entry.name.startswith("."):
                    continue
                if os.path.isfile(os.path.join(entry.path, "__manifest__.py")):
                    return True
    except OSError:
        pass
    return False


def discover_addons_folders():
    """Walk LOCAL_CODE_ROOT for addons-folder candidates: a directory that directly
    has a manifest-bearing subfolder is reported and NOT descended into further — a
    submodule living inside a monorepo already qualifies on its own, so stopping there
    avoids also reporting its parent's other submodules as separate spurious matches
    while still finding each one independently when the parent itself doesn't qualify.
    Returns paths as POSIX strings relative to LOCAL_CODE_ROOT, sorted."""
    if not LOCAL_CODE_ROOT.is_dir():
        return []
    found = []

    def walk(path, depth):
        if _has_manifest_child(path):
            found.append(path)
            return
        if depth >= LOCAL_SCAN_MAX_DEPTH:
            return
        try:
            with os.scandir(path) as it:
                children = [e for e in it if e.is_dir(follow_symlinks=False) and not e.name.startswith(".")]
        except OSError:
            return
        for entry in children:
            walk(entry.path, depth + 1)

    walk(LOCAL_CODE_ROOT, 0)
    return sorted(os.path.relpath(p, LOCAL_CODE_ROOT) for p in found)


def sync_local(rel_path):
    """Rsync a discovered local folder straight into ADDONS_DIR — same target and
    exclusions as a PR sync (runner._rsync_addons), just skipping git entirely."""
    target = (LOCAL_CODE_ROOT / rel_path).resolve()
    root = LOCAL_CODE_ROOT.resolve()
    if root not in (target, *target.parents):
        raise ValueError("path escapes the local addons root")
    if not _has_manifest_child(target):
        raise ValueError(f"{rel_path!r} is no longer a valid addons folder")
    _rsync_addons(source_dir=target)
    with _lock:
        _state["syncedLocal"] = rel_path
        _state["syncedPr"] = None
        _state["syncedCommit"] = None
    return {"path": rel_path}


def tail_log(n=200):
    try:
        with open(INSTANCE_LOG_PATH, "rb") as f:
            f.seek(max(0, INSTANCE_LOG_PATH.stat().st_size - 64_000))
            text = f.read().decode("utf-8", errors="replace")
    except FileNotFoundError:
        return ""
    return "\n".join(text.splitlines()[-n:])
