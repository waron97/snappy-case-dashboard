import os
import socket
from pathlib import Path

import redis

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
