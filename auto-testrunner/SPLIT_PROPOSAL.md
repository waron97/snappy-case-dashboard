# Proposal: split auto-testrunner into control + worker roles

**Status:** proposed, not implemented (parked for later)
**Date:** 2026-07-03

## Context

`auto-testrunner` currently runs as `deploy.replicas: 2` identical containers. Each
replica's `orchestrator.py` starts four things in-process:

- **worker** — `BLPOP`s the Redis queue and runs `run_test` (the actual PR testing)
- **poller** — discovers open PRs via Azure DevOps and enqueues them (every 60s)
- **Flask API** (`:8765`) — serves the web dashboard (`/prs`, `/status`, `/recheck`, `/discover`, `/notify`)
- **warmer** — maintains the pre-warmed base-DB pool

Only the **worker** genuinely benefits from running N times. The other three are
singletons that we currently force to run on every replica and then coordinate:

- poller is guarded by a Redis lock (`test:poller_lock`)
- warmer is coordinated via the `test:pool:building` Redis set
- the API is simply redundant (both run it; only one is reached)

Plus base lifecycle (`ensure_base_db` restore, `flush_pool`, startup orphan cleanup)
runs in every replica's startup and leans on a Postgres advisory lock to serialize.

This works, but the coordination is load-bearing where it shouldn't need to be, and it's
confusing that control-plane concerns are duplicated across worker replicas.

## Proposed split — two roles, one image

Same Docker image; a `ROLE=control|worker` env var selects behaviour in `startup.sh`
and `orchestrator.py`.

### `testrunner-control` (replicas: 1)
The singletons + base lifecycle:
- Flask API (`:8765`) — the web dashboard target
- poller (PR discovery / enqueue)
- warmer (pool maintenance)
- `ensure_base_db` (restore + ready-marker + `flush_pool` on re-restore)
- startup orphan cleanup (`cleanup_orphan_test_dbs`)

Needs: redis, postgres, **dump mount** (`./dump-test-01`). **No repo clone** — none of
these touch `/opt/repo`.

### `testrunner-worker` (replicas: N)
The scalable part:
- worker loop + `run_test` (git checkout → rsync into addons → odoo install/tests →
  pre-commit → init test that **claims from the pool**)

Needs: repo clone, `odoo-init.conf` (generated at its own startup — it's a
per-container file, not shared), redis, postgres. **No** API / poller / warmer /
dump mount.

## Responsibilities

| Concern | Today (every replica) | control | worker |
|---|---|---|---|
| worker `BLPOP` + `run_test` | ✓ | | ✓ (×N) |
| poller | ✓ (lock) | ✓ | |
| Flask API `:8765` | ✓ | ✓ | |
| warmer | ✓ (redis-coord) | ✓ | |
| base restore / flush / marker | ✓ (advisory lock) | ✓ | |
| startup orphan cleanup | ✓ | ✓ | |
| `generate_init_conf` (odoo-init.conf) | ✓ | | ✓ (needs it to run `-u`) |
| repo clone / fetch | ✓ | | ✓ |
| dump mount | ✓ | ✓ | |

## Concrete changes

### `config.py`
- Add `ROLE = os.environ.get("ROLE", "worker")` (default worker, or make it required).

### `startup.sh`
- Branch on `$ROLE`:
  - **control**: `generate_init_conf` is not needed (control doesn't run odoo); run
    `python3 /opt/base_db.py ensure` (restore + marker). Skip the git clone.
  - **worker**: git clone/fetch as today; `python3 /opt/base_db.py init-conf` (a new
    lightweight arg that only runs `generate_init_conf`, not the restore). Do NOT
    restore.
- Both then `exec python3 /opt/orchestrator.py`.

### `orchestrator.py`
- Branch on `ROLE`:
  - **control**: run `cleanup_orphan_test_dbs()`, start poller thread, start API
    thread, start warmer thread. Do **not** run the worker loop (idle main thread, or
    just block).
  - **worker**: run the worker loop only. No poller/API/warmer.
- Keep `ENABLE_TEST01_INIT_TEST` gating the warmer inside control.

### `base_db.py`
- Split the `__main__` CLI: `ensure` (restore, control) vs `init-conf`
  (`generate_init_conf` only, worker). Restore stays control-only.

### `docker-compose.yml`
Replace the single `auto-testrunner` service with two sharing the build:
```yaml
  testrunner-control:
    build: ./auto-testrunner
    depends_on: { postgres: {condition: service_healthy}, redis: {condition: service_started} }
    env_file: [ ./.env ]
    environment:
      - ROLE=control
      - REDIS_URL=redis://redis:6379
      - RESULTS_DIR=/results
      - ENABLE_TEST01_INIT_TEST=1
    volumes:
      - test_results:/results
      - ./dump-test-01:/opt/dump-test-01:ro

  testrunner-worker:
    build: ./auto-testrunner
    depends_on: { postgres: {condition: service_healthy}, redis: {condition: service_started} }
    env_file: [ ./.env ]
    environment:
      - ROLE=worker
      - REDIS_URL=redis://redis:6379
      - RESULTS_DIR=/results
      - ENABLE_TEST01_INIT_TEST=1
    volumes:
      - test_results:/results
    deploy:
      replicas: 2
```
- Web `TESTRUNNER_API_URL` points at `http://testrunner-control:8765` (was
  `auto-testrunner:8765`).

## Benefits
- One warmer, poller, API — Redis coordination becomes belt-and-suspenders instead of
  load-bearing.
- Workers are pure horizontal scale: bump `replicas` without multiplying control work.
- Clear failure domains: control down → no new discovery/warming, running tests finish;
  worker down → just less throughput.
- Base lifecycle owned by exactly one container — restore/flush/cleanup stop being
  advisory-lock races.
- Faster, lighter workers (no dump mount; control has no repo clone).

## Caveats / open questions
- **Ordering**: `depends_on` gives start order but not "base ready". The
  ready-marker + pool-wait (`claim_pool_db`) already handle a worker that starts before
  control finishes restoring — keep the worker's on-demand fallback (`ensure_base_db`
  is a no-op once the marker is set) so an early worker still functions. Consider
  whether workers should be allowed to restore at all, or strictly wait for control.
- **Single control = single point for discovery/warming.** Acceptable (poller/warmer
  are best-effort background jobs); if it restarts, running tests are unaffected and it
  resumes. If HA is ever wanted, the existing Redis lock / `building` set already make
  control safe to run >1 — so the split doesn't foreclose that.
- Keep the Redis poller-lock and `building`-set coordination even with 1 control, as
  cheap safety if it's ever scaled or double-started during a deploy.
- Two services now share `build: ./auto-testrunner`; a rebuild rebuilds both (fine).

## Migration steps
1. Add `ROLE` handling to `config.py`, `startup.sh`, `orchestrator.py`, `base_db.py`.
2. Split the compose service; repoint web `TESTRUNNER_API_URL`.
3. `docker compose up -d --build` — control restores/warms, workers consume.
4. Verify: one API answering `/prs`, one warmer filling the pool, N workers pulling the
   queue, base restored exactly once.
