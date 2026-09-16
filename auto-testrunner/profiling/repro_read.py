"""Manual repro helper for the instance-tracing feature (see sitecustomize.py).

Not wired into the app — run it by hand (`python3 repro_read.py`) from anywhere with network
access to the attached instance, after enabling "Request tracing" for it in the devops UI.
Tracing is hooked at the ORM level (odoo.models.BaseModel), so it fires regardless of
whether the call arrives via this script's XML-RPC call, an external JSON-RPC client, or
just loading the record in the web UI directly — no need to match transports.

Edit the values below to match the real slow call (same db/ids/fields/context) before running.
"""

import xmlrpc.client

URL = "http://localhost:8069"
DB = "dev_yourcopy"  # the DB name of the attached copy, not the source ("test-01"/"test-02")
USER = "admin"
PASSWORD = "admin"
MODEL = "helpdesk.ticket"
METHOD = "read"
IDS = [1]
KWARGS = {"fields": []}  # empty = all fields, matching a naive/unscoped real-world caller

common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
uid = common.authenticate(DB, USER, PASSWORD, {})

models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
result = models.execute_kw(DB, uid, PASSWORD, MODEL, METHOD, [IDS], KWARGS)
print(result)
