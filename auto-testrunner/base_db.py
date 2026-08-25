"""Restore the test-01/test-02 dumps into their base DBs (once, across replicas),
manage named persistent dev copies cloned from either base, and generate the
init-test odoo.conf. See config.ENABLE_TEST01_INIT_TEST."""

import configparser
import json
import logging
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import psycopg2

from config import (
    COPIES_KEY,
    COPY_NAME_RE,
    COPY_PREFIX,
    DB_HOST,
    DB_PASSWORD,
    DB_USER,
    ODOO_CONF,
    ODOO_INIT_CONF,
    POOL_BUILDING_KEY,
    POOL_CLAIM_POLL,
    POOL_CLAIM_TIMEOUT,
    POOL_READY_KEY,
    POOL_SEQ_KEY,
    POOL_WARM_CONCURRENCY,
    SOURCES,
    TEST01_BASE_DB,
    TEST01_DUMP_DIR,
    TEST01_POOL_SIZE,
    rdb,
)
from tasks import live_jobs

log = logging.getLogger(__name__)

# Maintenance DB always present (created by the postgres image), used to hold the
# advisory lock and to create/drop the base DB from.
MAINTENANCE_DB = "odoo_base"


def pg_env():
    import os

    return {**os.environ, "PGPASSWORD": DB_PASSWORD}


READY_MARKER = "restored"


def _base_marked_ready(cur, source):
    """Readiness check that does NOT connect to the base DB, so it can never block on
    a CREATE DATABASE ... TEMPLATE lock held during a concurrent init-test copy. Reads
    a marker comment set on the base DB once its restore succeeded. `cur` is a cursor
    on the maintenance DB."""
    cur.execute(
        "SELECT shobj_description(oid, 'pg_database') FROM pg_database WHERE datname = %s",
        (SOURCES[source].base_db,),
    )
    row = cur.fetchone()
    return bool(row) and row[0] == READY_MARKER


def _base_db_ready(source):
    """Deep check (connects to the base). Used only right after a restore, when no
    template copy is in progress, to confirm the data actually landed."""
    base_db = SOURCES[source].base_db
    try:
        conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=base_db)
    except psycopg2.Error:
        return False
    try:
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM ir_module_module")
        return cur.fetchone()[0] > 0
    except psycopg2.Error:
        return False
    finally:
        conn.close()


def _restore(source):
    base_db, dump_dir, _ = SOURCES[source]
    log.info(f"Dropping any partial {base_db}...")
    subprocess.run(
        ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", base_db],
        env=pg_env(),
        check=True,
    )
    log.info(f"Creating {base_db}...")
    subprocess.run(
        ["createdb", "-h", DB_HOST, "-U", DB_USER, base_db],
        env=pg_env(),
        check=True,
    )
    log.info(f"Restoring dump from {dump_dir} (this can take several minutes)...")
    # pg_restore exits nonzero on ignorable errors too (e.g. missing pgaudit
    # extension on the target server), so don't treat rc as fatal — validate the
    # result by readiness (populated ir_module_module) instead.
    rc = subprocess.run(
        [
            "pg_restore", "-Fd", "-j", "8", "-v", "--no-owner", "--no-privileges",
            "-h", DB_HOST, "-U", DB_USER, "-d", base_db,
            str(dump_dir),
        ],
        env=pg_env(),
    ).returncode
    if rc != 0:
        log.warning(f"pg_restore exited rc={rc} (ignorable errors expected); verifying...")
    if not _base_db_ready(source):
        log.error(f"Restore incomplete (ir_module_module empty); dropping partial {base_db}")
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", base_db],
            env=pg_env(),
        )
        raise RuntimeError(f"{source} base DB restore failed")
    log.info(f"Restore of {base_db} complete")


def ensure_base_db(source, force=False):
    """Ensure the restored base DB for `source` exists. Idempotent and safe across
    replicas: a Postgres advisory lock (per-source, so test-01/test-02 never serialize
    on each other) serializes concurrent starts so each dump restores once.

    `force=True` always re-restores (terminating any backends on the base first) even
    if it's already marked ready — used by reset_source()."""
    base_db, _, lock_key = SOURCES[source]
    conn = psycopg2.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=MAINTENANCE_DB
    )
    conn.autocommit = True
    try:
        cur = conn.cursor()
        cur.execute("SELECT pg_advisory_lock(%s)", (lock_key,))
        if not force and _base_marked_ready(cur, source):
            log.info(f"{base_db} already present, skipping restore")
            return
        if force:
            cur.execute(
                "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = %s",
                (base_db,),
            )
        _restore(source)
        cur.execute(f'COMMENT ON DATABASE "{base_db}" IS %s', (READY_MARKER,))
        log.info(f"Marked {base_db} ready")
        if source == "test-01":
            # Base data changed → any pre-warmed copies of the old base are stale.
            # test-02 has no pool.
            flush_pool()
    finally:
        cur.execute("SELECT pg_advisory_unlock(%s)", (lock_key,))
        conn.close()


def ensure_all_bases():
    """Restore every source concurrently. Called once at control startup — distinct
    per-source advisory-lock keys mean test-01 and test-02 don't serialize on each other."""
    with ThreadPoolExecutor(max_workers=len(SOURCES)) as ex:
        list(ex.map(ensure_base_db, SOURCES.keys()))


def reset_source(source):
    """Re-restore `source`'s base from its current dump dir, in-process. The single
    implementation both `make reset-base` and the API's reset route call, so they
    can't drift. Never touches named dev copies (Part C) — those are independent DBs
    from the moment they're created."""
    ensure_base_db(source, force=True)


def reconcile_pool_on_boot():
    """Recover pool-warming bookkeeping across a control restart. Must run before
    cleanup_orphan_test_dbs(), for two reasons:
    - Any entry in POOL_BUILDING_KEY is necessarily stale the moment control restarts:
      the background thread that would eventually move it to ready or drop it on
      failure died with the old process, so a name can be stuck "building" forever
      with no thread left to ever finish it.
    - Some of those stale entries may have actually finished createdb before the old
      process died — the DB exists, it's perfectly usable, it just never got moved
      ready→building. If left untracked, cleanup_orphan_test_dbs() (which runs right
      after this) would treat it as an orphan and drop a perfectly good pool copy.
    Restarting control repeatedly (e.g. during active development) previously let
    these accumulate until POOL_BUILDING_KEY alone reached TEST01_POOL_SIZE, at which
    point warm_pool()'s deficit was permanently zero and the pool never recovered."""
    building = {_decode(x) for x in rdb.smembers(POOL_BUILDING_KEY)}
    if not building:
        return
    live = _existing_db_names(POOL_PREFIX)
    completed = building & live
    if completed:
        rdb.sadd(POOL_READY_KEY, *completed)
        log.info(f"Recovered {len(completed)} pool DB(s) that finished building before a restart: {sorted(completed)}")
    rdb.delete(POOL_BUILDING_KEY)
    log.info(f"Cleared {len(building)} stale pool 'building' entry(ies) after restart")


def reconcile_copies_on_boot():
    """Recover named-copy bookkeeping across a control restart — the same problem as
    reconcile_pool_on_boot(), for the same reason: a 'creating' entry can only be
    stale after a restart, since the background thread that would ever finish it died
    with the old process. If the actual DB exists, the clone genuinely completed
    before the restart — mark it ready. Otherwise it never finished; mark it failed so
    the UI surfaces that instead of showing 'creating' forever with nothing left to
    finish it."""
    raw = rdb.hgetall(COPIES_KEY)
    meta = {_decode(k): json.loads(_decode(v)) for k, v in raw.items()}
    stuck = {n: info for n, info in meta.items() if info.get("status") == "creating"}
    if not stuck:
        return
    live = _existing_db_names(COPY_PREFIX)
    for n, info in stuck.items():
        if n in live:
            _put_copy_meta(n, info["source"], info["created_at"], "ready")
            log.info(f"Recovered dev copy {n} that finished creating before a restart")
        else:
            _put_copy_meta(
                n, info["source"], info["created_at"], "failed",
                error="creation was interrupted by a control restart",
            )
            log.warning(f"Dev copy {n} never finished creating before a restart; marked failed")


_resetting_lock = threading.Lock()
_resetting = set()


def is_resetting(source):
    return source in _resetting


def reset_source_async(source):
    """Fire-and-forget reset_source(), guarded so concurrent resets of the same source
    can't overlap (a restore takes minutes, too long for a synchronous HTTP request).
    Returns False if a reset of this source is already running."""
    with _resetting_lock:
        if source in _resetting:
            return False
        _resetting.add(source)

    def _run():
        try:
            reset_source(source)
        except Exception:
            log.exception(f"reset_source({source}) failed")
        finally:
            with _resetting_lock:
                _resetting.discard(source)

    threading.Thread(target=_run, daemon=True, name=f"reset-{source}").start()
    return True


def cleanup_orphan_test_dbs():
    """Drop leftover per-run test DBs (odoo_* / init_*) from workers killed mid-run
    (SIGKILL skips the finally: dropdb). Liveness is judged by *active Postgres
    connections*, not Redis: a DB with 0 connections is not in use, so it is safe to
    drop even while a concurrent replica runs (its DBs have live connections).
    Commits held by a heartbeating worker are protected too, covering the window between
    createdb and Odoo's first connection, when a live run's DB has no connections yet."""
    # Also reaps worker entries whose heartbeat lapsed, so the UI stops showing dead runs.
    protected = {j["commit"][:12] for j in live_jobs().values() if j.get("commit")}
    rows = subprocess.run(
        [
            "psql", "-h", DB_HOST, "-U", DB_USER, "-d", MAINTENANCE_DB, "-tAc",
            "SELECT d.datname, count(a.pid) FROM pg_database d "
            "LEFT JOIN pg_stat_activity a ON a.datname = d.datname "
            "WHERE d.datname LIKE 'odoo\\_%' OR d.datname LIKE 'init\\_%' "
            "GROUP BY d.datname",
        ],
        env=pg_env(), capture_output=True, text=True,
    ).stdout.splitlines()

    # Pooled copies tracked in Redis belong to the shared pool (possibly in use by
    # another replica) — leave them. Only untracked, idle ones are true orphans.
    tracked = {_decode(x) for x in rdb.smembers(POOL_READY_KEY)} | {
        _decode(x) for x in rdb.smembers(POOL_BUILDING_KEY)
    }

    for row in rows:
        if "|" not in row:
            continue
        datname, conns = row.split("|")
        conns = int(conns)
        if datname == MAINTENANCE_DB:
            continue
        if datname.startswith(POOL_PREFIX):
            if datname in tracked or conns > 0:
                continue  # valid shared-pool DB or in use — keep
            subprocess.run(
                ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", "--force", datname],
                env=pg_env(),
            )
            log.info(f"Dropped orphan pool DB {datname} (untracked in Redis)")
            continue
        # Per-run test DB (odoo_<hash> / init_<hash>): single-use, drop if idle and
        # not claimed by a live worker.
        if conns > 0 or datname.split("_", 1)[1] in protected:
            continue
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", "--force", datname],
            env=pg_env(),
        )
        log.info(f"Dropped orphan test DB {datname}")


POOL_PREFIX = "init_pool_"


def _decode(v):
    return v.decode() if isinstance(v, bytes) else v


def base_ready(source):
    """Quick marker check via the maintenance DB (never connects to the base)."""
    conn = psycopg2.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=MAINTENANCE_DB
    )
    conn.autocommit = True
    try:
        return _base_marked_ready(conn.cursor(), source)
    finally:
        conn.close()


def claim_pool_db(timeout=POOL_CLAIM_TIMEOUT, on_wait=None):
    """Atomically take a ready pre-warmed copy, waiting for the warmer to produce one
    rather than racing it with an own copy. Returns a DB name, or None only if none
    became available within `timeout` (warmer presumably dead → caller does on-demand).
    `on_wait(seconds_waited)` is called each poll so the caller can surface the wait —
    this can block for up to 25 min and would otherwise look like a hung worker."""
    waited = 0
    while True:
        name = _decode(rdb.spop(POOL_READY_KEY))
        if name:
            return name
        if waited >= timeout:
            return None
        time.sleep(POOL_CLAIM_POLL)
        waited += POOL_CLAIM_POLL
        if on_wait:
            on_wait(waited)


def flush_pool():
    """Drop every pooled copy and clear the pool bookkeeping. Called after an actual
    base re-restore, since pre-warmed copies of the old base are now stale."""
    rows = subprocess.run(
        [
            "psql", "-h", DB_HOST, "-U", DB_USER, "-d", MAINTENANCE_DB, "-tAc",
            f"SELECT datname FROM pg_database WHERE datname LIKE '{POOL_PREFIX}%'",
        ],
        env=pg_env(), capture_output=True, text=True,
    ).stdout.split()
    for name in rows:
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", "--force", name],
            env=pg_env(),
        )
    rdb.delete(POOL_READY_KEY, POOL_BUILDING_KEY)
    if rows:
        log.info(f"Flushed {len(rows)} stale pooled DB(s) after re-restore")


def _build_pool_db(name):
    """Create one pooled copy (CREATE DATABASE ... TEMPLATE) and move it building→ready."""
    try:
        subprocess.run(
            ["createdb", "-h", DB_HOST, "-U", DB_USER, "-T", TEST01_BASE_DB, name],
            env=pg_env(), check=True,
        )
    except subprocess.CalledProcessError as e:
        log.warning(f"Pool warm failed for {name}: {e}")
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", "--force", name],
            env=pg_env(),
        )
        rdb.srem(POOL_BUILDING_KEY, name)
        return
    rdb.srem(POOL_BUILDING_KEY, name)
    rdb.sadd(POOL_READY_KEY, name)
    log.info(f"Warmed pool DB {name} ({rdb.scard(POOL_READY_KEY)}/{TEST01_POOL_SIZE} ready)")


def warm_pool():
    """Top up the shared pool to TEST01_POOL_SIZE ready base copies. Reserves every
    missing slot up front (SADD building) so the size gate holds, then builds them
    POOL_WARM_CONCURRENCY at a time — a single CREATE DATABASE doesn't saturate disk
    IO, so a couple in parallel fill the pool faster. Runs off the critical path."""
    if not base_ready("test-01"):
        return
    deficit = TEST01_POOL_SIZE - (rdb.scard(POOL_READY_KEY) + rdb.scard(POOL_BUILDING_KEY))
    if deficit <= 0:
        return
    names = []
    for _ in range(deficit):
        name = f"{POOL_PREFIX}{rdb.incr(POOL_SEQ_KEY)}"
        rdb.sadd(POOL_BUILDING_KEY, name)
        names.append(name)
    with ThreadPoolExecutor(max_workers=POOL_WARM_CONCURRENCY) as ex:
        list(ex.map(_build_pool_db, names))


# --- named, persistent dev DB copies -----------------------------------------------
# Unlike the pool above (test-01-only, single-use, dropped after one claim), these are
# user-named, persist indefinitely for reattaching, and can come from either source.
# The "dev_" prefix (config.COPY_PREFIX) keeps them structurally outside every LIKE
# pattern cleanup_orphan_test_dbs()/flush_pool() use, so those never touch them.


def copy_db_name(name):
    return f"{COPY_PREFIX}{name}"


def _existing_db_names(prefix):
    return set(
        subprocess.run(
            [
                "psql", "-h", DB_HOST, "-U", DB_USER, "-d", MAINTENANCE_DB, "-tAc",
                f"SELECT datname FROM pg_database WHERE datname LIKE '{prefix}%'",
            ],
            env=pg_env(), capture_output=True, text=True,
        ).stdout.split()
    )


def _put_copy_meta(db_name, source, created_at, status, error=None):
    rdb.hset(
        COPIES_KEY, db_name,
        json.dumps({"source": source, "created_at": created_at, "status": status, "error": error}),
    )


def list_copies():
    """Redis metadata (source, created_at, status) reconciled against a live Postgres
    scan — but only for entries already marked 'ready': a 'creating' one has no backing
    DB yet by design (the clone is still running in the background), so it must never
    be pruned by the reconciliation before that background thread finishes."""
    raw = rdb.hgetall(COPIES_KEY)
    meta = {_decode(k): json.loads(_decode(v)) for k, v in raw.items()}
    if not meta:
        return []
    live = _existing_db_names(COPY_PREFIX)
    stale = [n for n, info in meta.items() if info.get("status") == "ready" and n not in live]
    for n in stale:
        del meta[n]
    if stale:
        rdb.hdel(COPIES_KEY, *stale)
    return [
        {
            # Bare name (prefix stripped) — every other route (create/delete/attach)
            # takes and re-prefixes a bare name, so this must match that contract or
            # a name round-tripped straight from here gets double-prefixed downstream.
            "name": n[len(COPY_PREFIX):], "source": info["source"], "createdAt": info["created_at"],
            "status": info.get("status", "ready"), "error": info.get("error"),
        }
        for n, info in meta.items()
    ]


def copy_exists(db_name):
    # db_name is always COPY_PREFIX + a name already validated against COPY_NAME_RE
    # ([a-z0-9_] only), so plain interpolation here can't be injected.
    out = subprocess.run(
        [
            "psql", "-h", DB_HOST, "-U", DB_USER, "-d", MAINTENANCE_DB, "-tAc",
            f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'",
        ],
        env=pg_env(), capture_output=True, text=True,
    ).stdout.strip()
    return out == "1"


def create_copy(name, source):
    """Validate synchronously (cheap) and kick off the actual clone in the background —
    `createdb -T` on a multi-GB base can take minutes (see the pool's warm-up comment
    above), too long to hold an HTTP request open for. The pending copy shows up in
    list_copies() immediately with status 'creating'."""
    if source not in SOURCES:
        raise ValueError(f"unknown source {source!r}")
    if not name or not COPY_NAME_RE.match(name):
        raise ValueError(
            "name must start with a lowercase letter and contain only lowercase "
            "letters, digits, or underscores (max 41 chars)"
        )
    db_name = copy_db_name(name)
    if rdb.hexists(COPIES_KEY, db_name) or copy_exists(db_name):
        raise ValueError(f"copy {name!r} already exists")
    if not base_ready(source):
        raise RuntimeError(f"{source} base is not ready yet")

    created_at = time.time()
    _put_copy_meta(db_name, source, created_at, "creating")

    def _run():
        # Catches any exception, not just a failed createdb: a Redis hiccup or
        # anything else raised after a successful clone must still mark this
        # 'failed' rather than silently dying and leaving it stuck 'creating' forever
        # with no thread left to ever finish it (reconcile_copies_on_boot() is the
        # backstop for a restart mid-flight, but this covers the same-process case).
        try:
            subprocess.run(
                ["createdb", "-h", DB_HOST, "-U", DB_USER, "-T", SOURCES[source].base_db, db_name],
                env=pg_env(), check=True,
            )
            _put_copy_meta(db_name, source, created_at, "ready")
            log.info(f"Created dev copy {db_name} from {source}")
        except Exception as e:
            _put_copy_meta(db_name, source, created_at, "failed", error=str(e))
            log.error(f"Creating dev copy {db_name} failed: {e}")

    threading.Thread(target=_run, daemon=True, name=f"create-copy-{db_name}").start()
    return db_name


def delete_copy(name):
    db_name = copy_db_name(name)
    subprocess.run(
        ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", "--force", db_name],
        env=pg_env(),
    )
    rdb.hdel(COPIES_KEY, db_name)


def generate_init_conf():
    """Copy the baked odoo.conf to the init conf, loading module_upgrade_optimizer
    server-wide so it can skip unchanged modules during -u."""
    cp = configparser.ConfigParser()
    cp.read(ODOO_CONF)
    if "options" not in cp:
        cp["options"] = {}
    cp["options"]["server_wide_modules"] = "base,web,module_upgrade_optimizer"
    # Disable Odoo's memory cap (defaults ~2.5 GB via RLIMIT_AS) — a full -u of many
    # modules on production-like data exceeds it and dies with MemoryError. This is a
    # single one-shot process on a host with ample RAM.
    cp["options"]["limit_memory_soft"] = "0"
    cp["options"]["limit_memory_hard"] = "0"
    with open(ODOO_INIT_CONF, "w") as f:
        cp.write(f)
    log.info(f"Wrote {ODOO_INIT_CONF} with module_upgrade_optimizer server-wide, memory caps disabled")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "ensure-all":  # control startup: restore every source (needs both dump mounts)
        ensure_all_bases()
    elif arg == "ensure":  # restore one source, e.g. `base_db.py ensure test-01`
        ensure_base_db(sys.argv[2] if len(sys.argv) > 2 else "test-01")
    elif arg == "reset":  # force re-restore one source, e.g. after a dump swap
        reset_source(sys.argv[2] if len(sys.argv) > 2 else "test-01")
    elif arg == "init-conf":  # worker: generate the odoo-init.conf it runs -u/-i with
        generate_init_conf()
    else:
        print("usage: base_db.py ensure-all|ensure <source>|reset <source>|init-conf")
        sys.exit(1)
