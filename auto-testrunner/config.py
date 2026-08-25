import os
import re
import socket
from pathlib import Path
from typing import NamedTuple

import redis

DEVOPS_ORG = os.environ["DEVOPS_ORG"]
DEVOPS_PROJECT = os.environ["DEVOPS_PROJECT"]
DEVOPS_REPO = os.environ["DEVOPS_REPO"]
DEVOPS_ACCESS_TOKEN = os.environ["DEVOPS_ACCESS_TOKEN"]
# When set, PR comments are logged but not actually posted (safe testing).
DEVOPS_DRYRUN = os.environ.get("DEVOPS_DRYRUN") == "1"
# Container role: "control" (single instance: poller + API + warmer + base restore)
# or "worker" (N instances: the test-running loop). See SPLIT_PROPOSAL.md.
ROLE = os.environ.get("ROLE", "worker")
REDIS_URL = os.environ.get("REDIS_URL", "redis://redis:6379")
RESULTS_DIR = Path(os.environ.get("RESULTS_DIR", "/results"))

REPO_DIR = Path("/opt/repo")
ADDONS_DIR = Path("/opt/odoo/addons")
ODOO_BIN = "/opt/odoo/base/odoo-bin"
ODOO_CONF = "/opt/odoo/odoo.conf"
ODOO_INIT_CONF = "/opt/odoo/odoo-init.conf"

# test-01 initialization test: upgrade changed modules on a copy of a restored
# production-like DB. Gated by ENABLE_TEST01_INIT_TEST; normal flow untouched when off.
ENABLE_TEST01_INIT_TEST = os.environ.get("ENABLE_TEST01_INIT_TEST") == "1"


class Source(NamedTuple):
    base_db: str
    dump_dir: Path
    advisory_lock_key: int  # distinct per source so restores never serialize on each other


# Named local dev sources: a restored, read-mostly base DB per environment, cloned via
# `createdb -T` for the pool (test-01 only) and for named dev copies (either source).
SOURCES: dict[str, Source] = {
    "test-01": Source("sorgenia_test_01_base", Path("/opt/dump-test-01"), 728104),
    "test-02": Source("sorgenia_test_02_base", Path("/opt/dump-test-02"), 728105),
}
# Back-compat aliases: base_db.py's pool code and runner.py's on-demand init-test
# fallback are test-01-only and keep referencing these directly.
TEST01_BASE_DB = SOURCES["test-01"].base_db
TEST01_DUMP_DIR = SOURCES["test-01"].dump_dir
SERIES = "15.0"
# Init test runs only for PRs touching this repo subdir: heavy XML "workflow"
# modules with no logic, excluded from unit tests, but must still upgrade cleanly.
TEST01_INIT_PATH_PREFIX = "config/"
TARGET_BRANCH = "15.0-dev"
# Pool of pre-created base-DB copies kept warm so init tests grab one instantly
# instead of waiting for a ~13 min template copy. Size ~= replica_count + 2.
TEST01_POOL_SIZE = int(os.environ.get("TEST01_POOL_SIZE", "4"))
POOL_READY_KEY = "test:pool:ready"
POOL_BUILDING_KEY = "test:pool:building"
POOL_SEQ_KEY = "test:pool:seq"
POOL_WARM_INTERVAL = 30
# How many pool copies the (single) control warmer builds concurrently. One CREATE
# DATABASE doesn't saturate disk IO, so 2 gives higher aggregate throughput.
POOL_WARM_CONCURRENCY = int(os.environ.get("POOL_WARM_CONCURRENCY", "2"))
# Init test waits for a warmer-provided copy rather than making its own (a copy in
# progress is usually closer to done, and dual copies thrash disk IO). On-demand
# creation is only a last resort if the warmer is dead past this timeout.
POOL_CLAIM_TIMEOUT = 1500
POOL_CLAIM_POLL = 5

POLL_INTERVAL = 60
QUEUE_KEY = "test:queue"
# Pre-commit is ~2 min against ~1 h for tests and ~30 min for init. Its jobs go on a
# separate list that workers BLPOP first, so lint feedback never queues behind a test run.
FAST_QUEUE_KEY = "test:queue:fast"
WORKERS_KEY = "test:workers"
POLLER_LOCK_KEY = "test:poller_lock"
WORKER_ID = socket.gethostname()

# A commit's work is split into these independently-queued tasks, one per worker
# iteration, so the replicas drain them in parallel. Module install and --test-enable
# travel together (one is the other's setup), hence a single "tests" task.
TASKS = ("tests", "precommit", "init")
FAST_TASKS = {"precommit"}
# Per-commit task state: hash of task -> queued|running|done. The control-plane messenger
# waits for a full set of "done" before posting the single combined PR comment.
TASK_STATE_PREFIX = "test:tasks:"
# Workers refresh a short-lived key so control can tell a live run from a SIGKILLed one
# (a dead worker's task would otherwise stay "running" forever and block the messenger).
HEARTBEAT_PREFIX = "test:hb:"
HEARTBEAT_TTL = 90
HEARTBEAT_INTERVAL = 30
MESSENGER_INTERVAL = 20
# A task whose worker dies is requeued this many times before being force-marked done, so
# a task that reliably kills its worker can't loop forever and block the report.
MAX_TASK_ATTEMPTS = 2
EXCLUDE = "symple_address_city_and_province_it,symple_contacts_default_data,sorgenia_imperex_metadata,sorgenia_ml_install_all"

DB_HOST = "postgres"
DB_USER = "odoo"
DB_PASSWORD = os.environ.get("DB_PASSWORD", "odoo")

STATE_TTL = 14 * 24 * 3600  # 14 days in seconds

rdb = redis.from_url(REDIS_URL)

# Named, persistent dev DB copies (distinct from the ephemeral odoo_*/init_*/init_pool_*
# families): "dev_" keeps them structurally outside every existing cleanup/reset LIKE
# pattern, so no other query anywhere needs to change to leave them alone.
COPY_PREFIX = "dev_"
COPY_NAME_RE = re.compile(r"^[a-z][a-z0-9_]{0,40}$")
COPIES_KEY = "test:copies"  # Redis hash: dev_<name> -> json {source, created_at}, the
# one piece of copy/instance state that must survive a control restart — everything
# else below is in-memory only, since control is a single-process, single-replica role.

# Single always-on-8069 Odoo dev instance.
ODOO_PORT = 8069
# Deliberately NOT under RESULTS_DIR: poller.py's vacuum() globs RESULTS_DIR for
# "*.log" and deletes anything whose filename-derived "hash" isn't a currently-open
# PR's commit — which "instance.log" matched, getting it wiped out roughly every
# POLL_INTERVAL. This file doesn't need to survive a restart or be shared with workers
# anyway (matches the rest of this module's in-memory-only, gone-on-restart model), so
# a container-local path sidesteps the collision entirely rather than special-casing it.
INSTANCE_LOG_PATH = Path("/tmp/odoo-instance.log")

# Broad local codebase root (LOCAL_ADDONS_HOST_PATH in .env), mounted read-only so the
# "sync local" instance action can discover and rsync an addons folder from it without
# going through git/PR sync at all. Absent (dir doesn't exist) is a supported state —
# discovery just reports no candidates rather than erroring.
LOCAL_CODE_ROOT = Path("/opt/local-code")
LOCAL_SCAN_MAX_DEPTH = 6
