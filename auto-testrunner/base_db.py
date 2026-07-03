"""Restore the test-01 dump into a base DB (once, across replicas) and generate
the init-test odoo.conf. See config.ENABLE_TEST01_INIT_TEST."""

import configparser
import logging
import subprocess
import sys

import psycopg2

from config import (
    DB_HOST,
    DB_PASSWORD,
    DB_USER,
    ODOO_CONF,
    ODOO_INIT_CONF,
    TEST01_BASE_DB,
    TEST01_DUMP_DIR,
    WORKERS_KEY,
    rdb,
)

log = logging.getLogger(__name__)

# Maintenance DB always present (created by the postgres image), used to hold the
# advisory lock and to create/drop the base DB from.
MAINTENANCE_DB = "odoo_base"
# Arbitrary fixed key so all replicas serialize on the same lock.
ADVISORY_LOCK_KEY = 728104


def pg_env():
    import os

    return {**os.environ, "PGPASSWORD": DB_PASSWORD}


READY_MARKER = "restored"


def _base_marked_ready(cur):
    """Readiness check that does NOT connect to the base DB, so it can never block on
    a CREATE DATABASE ... TEMPLATE lock held during a concurrent init-test copy. Reads
    a marker comment set on the base DB once its restore succeeded. `cur` is a cursor
    on the maintenance DB."""
    cur.execute(
        "SELECT shobj_description(oid, 'pg_database') FROM pg_database WHERE datname = %s",
        (TEST01_BASE_DB,),
    )
    row = cur.fetchone()
    return bool(row) and row[0] == READY_MARKER


def _base_db_ready():
    """Deep check (connects to the base). Used only right after a restore, when no
    template copy is in progress, to confirm the data actually landed."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=TEST01_BASE_DB
        )
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


def _restore():
    log.info(f"Dropping any partial {TEST01_BASE_DB}...")
    subprocess.run(
        ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", TEST01_BASE_DB],
        env=pg_env(),
        check=True,
    )
    log.info(f"Creating {TEST01_BASE_DB}...")
    subprocess.run(
        ["createdb", "-h", DB_HOST, "-U", DB_USER, TEST01_BASE_DB],
        env=pg_env(),
        check=True,
    )
    log.info(f"Restoring dump from {TEST01_DUMP_DIR} (this can take several minutes)...")
    # pg_restore exits nonzero on ignorable errors too (e.g. missing pgaudit
    # extension on the target server), so don't treat rc as fatal — validate the
    # result by readiness (populated ir_module_module) instead.
    rc = subprocess.run(
        [
            "pg_restore", "-Fd", "-j", "8", "-v", "--no-owner", "--no-privileges",
            "-h", DB_HOST, "-U", DB_USER, "-d", TEST01_BASE_DB,
            str(TEST01_DUMP_DIR),
        ],
        env=pg_env(),
    ).returncode
    if rc != 0:
        log.warning(f"pg_restore exited rc={rc} (ignorable errors expected); verifying...")
    if not _base_db_ready():
        log.error("Restore incomplete (ir_module_module empty); dropping partial base DB")
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", TEST01_BASE_DB],
            env=pg_env(),
        )
        raise RuntimeError("test-01 base DB restore failed")
    log.info(f"Restore of {TEST01_BASE_DB} complete")


def ensure_base_db():
    """Ensure the restored base DB exists. Idempotent and safe across replicas:
    a Postgres advisory lock serializes concurrent starts so the dump restores once."""
    conn = psycopg2.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=MAINTENANCE_DB
    )
    conn.autocommit = True
    try:
        cur = conn.cursor()
        cur.execute("SELECT pg_advisory_lock(%s)", (ADVISORY_LOCK_KEY,))
        if _base_marked_ready(cur):
            log.info(f"{TEST01_BASE_DB} already present, skipping restore")
            return
        _restore()
        cur.execute(f'COMMENT ON DATABASE "{TEST01_BASE_DB}" IS %s', (READY_MARKER,))
        log.info(f"Marked {TEST01_BASE_DB} ready")
    finally:
        cur.execute("SELECT pg_advisory_unlock(%s)", (ADVISORY_LOCK_KEY,))
        conn.close()


def cleanup_orphan_test_dbs():
    """Drop leftover per-run test DBs (odoo_* / init_*) from workers killed mid-run
    (SIGKILL skips the finally: dropdb). Liveness is judged by *active Postgres
    connections*, not Redis: a DB with 0 connections is not in use, so it is safe to
    drop even while a concurrent replica runs (its DBs have live connections).
    Also reaps stale WORKERS_KEY entries (SIGKILL never hdel'd them) so the UI stops
    showing dead runs as 'running'."""
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

    live_hashes = set()
    for row in rows:
        if "|" not in row:
            continue
        datname, conns = row.split("|")
        if datname == MAINTENANCE_DB:
            continue
        if int(conns) > 0:
            live_hashes.add(datname.split("_", 1)[1])  # 12-char commit prefix
            continue
        subprocess.run(
            ["dropdb", "-h", DB_HOST, "-U", DB_USER, "--if-exists", "--force", datname],
            env=pg_env(),
        )
        log.info(f"Dropped orphan test DB {datname}")

    for wid, commit in rdb.hgetall(WORKERS_KEY).items():
        wid = wid.decode() if isinstance(wid, bytes) else wid
        commit = commit.decode() if isinstance(commit, bytes) else commit
        if commit[:12] not in live_hashes:
            rdb.hdel(WORKERS_KEY, wid)
            log.info(f"Reaped stale worker entry {wid} -> {commit[:8]}")


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
    if len(sys.argv) > 1 and sys.argv[1] == "ensure":
        generate_init_conf()
        ensure_base_db()
    else:
        print("usage: base_db.py ensure")
        sys.exit(1)
