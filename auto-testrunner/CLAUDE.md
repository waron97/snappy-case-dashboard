# CLAUDE.md — auto-testrunner

## What this is

This is the PR test-running control plane for the Odoo 15.0 monorepo tracked in Azure
DevOps (`config.DEVOPS_ORG`/`DEVOPS_PROJECT`/`DEVOPS_REPO`, target branch `15.0-dev`). It
polls for open PRs, runs their tests/pre-commit/init-upgrade checks across a worker pool, and
posts a combined result comment back to the PR. It also runs and exposes a single, always-on
local Odoo dev instance for interactive inspection — that's `instances.py`, described below.
The `web-app` sibling directory is the devops-facing UI for all of this (see its own
`CLAUDE.md`) and is otherwise unrelated to Odoo itself.

**Important terminology**: "live" in this codebase means **a DB copy restored from a
production dump**, not a separate remote server. There is no remote Odoo host this service
manages or connects to — see "The single Odoo dev instance" below.

## Container roles

One image (`Dockerfile`), two roles selected by the `ROLE` env var (`startup.sh` branches on
it, `orchestrator.py` reads it too):

| Role      | Replicas | Does |
| --------- | -------- | ---- |
| `control` | 1        | Restores the `test-01`/`test-02` base DBs, runs the Flask API (`api.py`), the PR poller, the pool warmer, and owns the single Odoo dev instance (`instances.py`). Single-process/single-replica by design — see `instances.py`'s module docstring. |
| `worker`  | N (`docker-compose.yml`: 3) | Clones the repo, drains the task queue (`tasks`/`precommit`/`init`), runs pre-commit and Odoo test suites, reports results. |

## Key files

| File | Owns |
| ---- | ---- |
| `config.py` | All env-derived constants, Redis key names, the `SOURCES` dict (dump sources), Odoo paths/series. Read this first when anything below references a constant you don't recognize. |
| `orchestrator.py` | Process entrypoint: starts the poller thread, the Flask API, the pool warmer, and (control only) reconciles copies/pool on boot. |
| `poller.py` | Polls Azure DevOps for open PRs (`ado.py`), enqueues their tasks, holds the cross-replica poller lock. |
| `tasks.py` | Redis-backed queue encoding, per-commit task state, per-worker heartbeats/live status. Leaf module — only imports `config`. |
| `runner.py` | The actual test-running logic a worker executes per task: checkout, pre-commit, Odoo test suite, init-upgrade test, log parsing. |
| `base_db.py` | Restores `test-01`/`test-02` dumps into base DBs, manages named persistent `dev_*` copies (`createdb -T` clones), the pool of pre-warmed init-test copies, and `odoo-init.conf` generation. |
| `upgrade.py` | Diffs a DB's installed module versions against manifests to compute a minimal `-u` list. |
| `ado.py` | Azure DevOps REST calls: PR listing/details, posting comments, uploading attachments. |
| `notifier.py` | Watches finished task sets and posts the single combined PR comment. |
| `instances.py` | The single local Odoo dev-process manager — see below. |
| `api.py` | Flask app exposing all of the above over HTTP for `web-app`. Single-file, no blueprints. |
| `profiling/` | Opt-in request tracing for the dev instance — see below. |

`SPLIT_PROPOSAL.md` in this directory has more historical context on the control/worker split
if you need it; nothing here should contradict it, but this file is the current source of truth.

## The single Odoo dev instance (`instances.py`)

`control` runs at most one `odoo-bin` subprocess, always on port 8069, managed entirely
in-memory (state doesn't survive a container restart — `reset_to_stopped_on_boot()` is called
for exactly that reason). It is **not** a remote/production Odoo server: it's a local process
inside the `testrunner-control` container, attachable to either a `SOURCES` base DB or a named
persistent `dev_*` copy (`base_db.py`) — including copies cloned from a restored production
dump, which is what "live data" means in this codebase.

Core operations, all exposed via `/instance/*` routes in `api.py` and the `web-app`
`/devops/instances` page:
- `attach(db_name, install=, upgrade=, profile=)` — stop whatever's running, start fresh against
  `db_name`.
- `restart(...)` — re-syncs from whichever source is active (PR head or local folder) and
  re-attaches; doubles as the "apply -u" button.
- `sync_pr(pr_id)` / `sync_local(rel_path)` — rsync a PR checkout or a locally-mounted addons
  folder into the instance's addons path.
- `tail_log(n)` — tails `/tmp/odoo-instance.log`.

## Request tracing (opt-in, for diagnosing slow calls)

`profiling/sitecustomize.py` adds OpenTelemetry tracing to the attached instance, viewed in
**Jaeger** rather than a page in this app. It's off by default and has zero effect on the
instance when disabled.

- **Enable** via the "Request tracing" toggle on `/devops/instances` (sent as part of
  attach/restart) or directly via `profile: {enabled, model, methods}` in the
  `/instance/attach` or `/instance/restart` request body.
- **Hook point**: `odoo.models.BaseModel.<method>` for each method named in
  `ODOO_PROFILE_METHODS` (default `"read"`; blank traces every BaseModel method that can
  plausibly touch the DB — `sitecustomize.py`'s `_NO_IO_METHODS` excludes the pure in-memory
  recordset helpers like `browse`/`sudo`/`filtered`/`mapped`, which are called far too often
  to trace usefully), optionally filtered to one model via `ODOO_PROFILE_MODEL` (blank there
  really does mean every model). Spans export via `BatchSpanProcessor`, not per-span
  synchronous export — "every method" mode can wrap dozens of methods, and a blocking HTTP
  POST per span would make the instrumentation itself the bottleneck. This is deliberately
  ORM-level, not transport-level — a slow call
  shows up here whether it came from the web client's `/web/dataset/call_kw` (i.e. someone
  just loading a record in the browser), an external XML-RPC/JSON-RPC caller, or internal
  Python code. (An earlier design hooked `odoo.http.dispatch_rpc` instead, which only covers
  external RPC — that misses the "loading a record in the browser" case, which is the actual
  symptom this was built for, so don't reintroduce that as the primary hook.)
- **Computed fields get their own spans too**, independent of `ODOO_PROFILE_METHODS`
  (`ODOO_PROFILE_COMPUTES`, default on): Odoo dispatches every field computation — stored or
  not, on any model — through one method, `BaseModel._compute_field_value(self, field)`.
  Wrapping that single choke point gives a `compute.<model>.<field>` span per field actually
  evaluated, which is the only way to see *which* compute is slow on a model with many of
  them (e.g. `helpdesk.ticket`) — wrapping only `read` itself shows one opaque duration with
  no breakdown of the compute work that happened inside it.
- **Every span carries an `odoo.caller` attribute** (`file:line:function` of whoever called
  it, captured via a cheap fixed-depth `sys._getframe` walk, not a full stack trace). Nested
  wrapped calls already show their trigger through the trace's own parent/child spans, but an
  independently-triggered top-level call (no wrapped parent active — whatever a page load
  fires directly) otherwise gives no indication of what Python code asked for it.
- SQL queries (via `psycopg2`) and outbound HTTP calls (via `requests`/`urllib3`) are
  auto-instrumented as child spans, so a trace directly shows whether a slow call is
  SQL-bound, waiting on an external HTTP call, or spending time in uninstrumented Python.
- **Injection mechanism**: `instances.py`'s `attach()` puts `profiling/` on the odoo-bin
  subprocess's `PYTHONPATH` only when tracing is enabled, so it's picked up as a standard
  `sitecustomize` module — no Odoo addon/module install involved, and the unprofiled path
  (`env=None` passed to `Popen`) is untouched.
- **Viewing traces**: Jaeger isn't part of the normal stack — bring it up explicitly with
  `docker compose --profile debug up -d jaeger`, then open `http://localhost:16686` (service
  `odoo-dev-instance`). Storage is in-memory; traces don't survive a Jaeger restart, which is
  fine for a one-off investigation.
- **One trace per call, not per page load**: because the hook is per-ORM-call with no shared
  parent span, a single page load that fires many `read()`/`search_read()` calls produces many
  independent traces. Use Jaeger's min-duration filter on operation `orm.<model>.<method>` to
  find the slow outlier rather than expecting one trace per page.
- `profiling/repro_read.py` is a standalone (not wired into the app) manual `xmlrpc.client`
  script for triggering a specific call by hand.

## Appendix: broken web assets on a dev copy (404/500 on `/web/assets/...`)

Symptom: an attached instance renders an unstyled/broken or partially-broken web client; its
log is full of `404` for `/web/assets/<id>-<version>/web.assets_*.min.{js,css}` plus
`CacheMiss: 'ir.attachment(<id>,).raw'` and `_read_file reading .../filestore/<db>/<hh>/<hash>`
for files that don't exist, occasionally followed by `500 MissingError` on the same URLs.

Root cause — two independent caches going stale at once:

1. **DB-side**: named dev copies are made with `createdb -T` (`base_db.create_copy`), and the
   base itself is a plain `pg_restore` (`base_db._restore`). Neither copies the Odoo filestore.
   The production dump's already-generated `ir_attachment` rows named `web.assets_*` therefore
   point at `store_fname` blobs that were never placed under the local per-DB filestore
   (`/home/odoo/.local/share/Odoo/filestore/<db>/`), so Odoo serves 404 for bundle URLs it
   itself emitted.
2. **Process-side**: generated asset node URLs (with those attachment ids baked in) are held in
   an in-process `@ormcache` (`ir_qweb._generate_asset_nodes_cache` / `_get_asset_content`).
   Its own comment: assets are "cached forever... the admin can force a cache clear by
   restarting the server". Editing/deleting the rows under a running instance does not clear
   it, so it keeps emitting URLs for the now-missing attachments — and can serve ids that no
   longer exist, giving `500 MissingError` instead of a clean regenerate.

Fix (verified working):

```sql
-- on the attached copy, e.g. dev_general_01
DELETE FROM ir_attachment WHERE name LIKE 'web.assets%';
```

then restart (clears the ormcache so bundles recompile into the local filestore):

```bash
docker exec snappy-testrunner-testrunner-control-1 python3 -c "
import urllib.request, json
body = json.dumps({'upgrade': '', 'install': ''}).encode()  # '' = don't re-apply the previous -u
req = urllib.request.Request('http://127.0.0.1:8765/instance/restart', data=body,
                             headers={'Content-Type': 'application/json'})
print(urllib.request.urlopen(req).read().decode())"
```

Verify: fetch `/web/login`, collect every `/web/assets/...` ref, request each — all should be
200. (`GET /web/assets/...` as a logged-out user is enough; the backend bundle regenerates on
first authenticated `/web` load.)

Not yet automated: the recurrence is structural (every `pg_restore`/`createdb -T` inherits the
dump's asset rows without a filestore), so a durable fix belongs in `base_db` right after the
restore/clone — wipe `web.assets%` attachments there — rather than as a manual cleanup after
each attach.
