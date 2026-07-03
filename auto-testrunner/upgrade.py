"""Detect modules whose manifest version differs from the version installed in a
DB, so -u only touches what actually changed. Ported from ../run.sh."""

import ast
import configparser
import logging
import os

import psycopg2

from config import DB_HOST, DB_PASSWORD, DB_USER, SERIES

log = logging.getLogger(__name__)


def _adapt(v):
    """Normalize a manifest version to the SERIES-prefixed form Odoo stores in
    ir_module_module.latest_version (e.g. '1.2' -> '15.0.1.2')."""
    return v if v == SERIES or v.startswith(SERIES + ".") else f"{SERIES}.{v}"


def _manifest_versions(addons_path):
    paths = [
        os.path.expanduser(p.strip())
        for p in addons_path.replace("\n", ",").split(",")
        if p.strip()
    ]
    mver = {}
    for base in paths:
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            mf = os.path.join(base, name, "__manifest__.py")
            if name in mver or not os.path.isfile(mf):
                continue
            try:
                manifest = ast.literal_eval(open(mf, encoding="utf-8").read())
                mver[name] = _adapt(str(manifest.get("version") or "1.0"))
            except Exception:
                pass
    return mver


def installed_modules(db_name):
    """Names of all modules marked installed in the DB."""
    conn = psycopg2.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=db_name
    )
    try:
        cur = conn.cursor()
        cur.execute("SELECT name FROM ir_module_module WHERE state='installed'")
        return {r[0] for r in cur.fetchall()}
    finally:
        conn.close()


def detect_changed_modules(conf_path, db_name):
    """Return sorted list of installed modules whose manifest version != the
    version recorded in the DB."""
    cp = configparser.ConfigParser()
    cp.read(conf_path)
    mver = _manifest_versions(cp["options"]["addons_path"])

    conn = psycopg2.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=db_name
    )
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT name, latest_version FROM ir_module_module WHERE state='installed'"
        )
        changed = [
            n
            for n, latest in cur.fetchall()
            if n in mver and latest and mver[n] and mver[n] != latest
        ]
    finally:
        conn.close()
    return sorted(changed)
