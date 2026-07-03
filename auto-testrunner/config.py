import os
import socket
from pathlib import Path

import redis

DEVOPS_ORG = os.environ["DEVOPS_ORG"]
DEVOPS_PROJECT = os.environ["DEVOPS_PROJECT"]
DEVOPS_REPO = os.environ["DEVOPS_REPO"]
DEVOPS_ACCESS_TOKEN = os.environ["DEVOPS_ACCESS_TOKEN"]
# When set, PR comments are logged but not actually posted (safe testing).
DEVOPS_DRYRUN = os.environ.get("DEVOPS_DRYRUN") == "1"
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
TEST01_BASE_DB = "sorgenia_test_01_base"
TEST01_DUMP_DIR = Path("/opt/dump-test-01")
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
# Init test waits for a warmer-provided copy rather than making its own (a copy in
# progress is usually closer to done, and dual copies thrash disk IO). On-demand
# creation is only a last resort if the warmer is dead past this timeout.
POOL_CLAIM_TIMEOUT = 1500
POOL_CLAIM_POLL = 5

POLL_INTERVAL = 60
QUEUE_KEY = "test:queue"
WORKERS_KEY = "test:workers"
POLLER_LOCK_KEY = "test:poller_lock"
WORKER_ID = socket.gethostname()
EXCLUDE = "symple_address_city_and_province_it,symple_contacts_default_data,sorgenia_imperex_metadata,sorgenia_ml_install_all"

DB_HOST = "postgres"
DB_USER = "odoo"
DB_PASSWORD = os.environ.get("DB_PASSWORD", "odoo")

STATE_TTL = 14 * 24 * 3600  # 14 days in seconds

rdb = redis.from_url(REDIS_URL)
