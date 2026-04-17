# Auto Test Runner — Summary

## What it does
Polls Azure DevOps for open PRs every 5 minutes. For each PR's HEAD commit hash, if no result file exists and it's not already queued, pushes hash to Redis. Worker pops hashes one at a time, checks out the addons repo to that commit, runs Odoo unit tests, writes results to shared volume.

## Services added to docker-compose.dev.yml
| Service | Image | Notes |
|---|---|---|
| `postgres` | postgres:13 | Fresh DB per test run (`odoo_<hash[:12]>`), dropped after |
| `redis` | redis:7-alpine | Job queue |
| `redis-ui` | rediscommander/redis-commander | http://localhost:8081 |
| `auto-testrunner` | built from `./auto-testrunner` | Orchestrator service |

## Named volumes
- `postgres_test_data` — postgres data
- `addons_repo` — persists `/opt/repo` git clone across restarts
- `test_results` — result log files, **shared volume for NextJS to mount later**

## Result files
Written to named volume `test_results` (mounted at `/results` in container):
- `/results/<full_commit_hash>.install.log` — dependency install output
- `/results/<full_commit_hash>.test.log` — Odoo test output with `--test-enable`

## Redis keys
- `test:queue` — list, RPUSH to enqueue / BLPOP to dequeue
- `test:queued` — set, tracks in-progress + queued hashes to avoid duplicates; SREM'd on completion

## Environment variables required (pass via .env or compose)
| Var | Purpose |
|---|---|
| `DEVOPS_ACCESS_TOKEN` | Azure DevOps PAT for PR API |
| `DEVOPS_ORG` | Azure DevOps organisation |
| `DEVOPS_PROJECT` | Azure DevOps project |
| `DEVOPS_REPO` | Repository name |

## Git / submodule strategy
- Clones addons repo to `/opt/repo` at startup (branch `15.0-dev`)
- `git submodule update --init --recursive` — non-fatal, skips broken deeply-nested submodules
- `symple_addons` excluded from rsync — already baked into testrunner image at `/opt/odoo/symple_addons/`
- OCA submodules (`OCA/web`, `OCA/partner-contact`, etc.) synced from `/opt/repo` → `/opt/odoo/addons/`
- Per test run: `git fetch` + `git checkout <hash>` only (submodules not re-synced per run)

## NextJS integration TODO
- Mount `test_results` volume in the `web` service: `test_results:/results`
- Read `.install.log` / `.test.log` files by commit hash
- Optionally: read Redis to show queue status / in-progress runs
- Redis accessible at `redis:6379` from within compose network
