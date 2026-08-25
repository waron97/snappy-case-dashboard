# CLAUDE.md — web-app

## What this is

This is the devops/test-runner control panel for the `auto-testrunner` Python service
(sibling directory `auto-testrunner/`). It used to also be a full Odoo case-management
dashboard ("snappy") — that side has moved to a standalone Electron app and was removed
from this repo. This app now needs **no configuration to boot**: no Keycloak, no Odoo
credentials, nothing beyond the devops-facing env vars below.

## Technologies

| Layer             | Tool                                                       |
| ----------------- | ---------------------------------------------------------- |
| Framework         | Next.js 16 (App Router, server actions, standalone output) |
| UI                | React 19 + TypeScript 5 (strict mode)                      |
| Component library | Mantine 8 (core, hooks)                                    |
| Server state      | TanStack React Query 5                                     |
| Icons             | Tabler Icons                                               |
| Editor            | CodeMirror 6 (used only by `LogViewer`, for read-only log display) |
| Linting           | ESLint 9 + TypeScript ESLint + Mantine preset               |
| Formatting        | Prettier 3 + import-sort plugin                            |
| Testing           | Jest 30 + Testing Library                                  |
| Storybook         | Storybook 10                                               |
| Package manager   | Yarn 4                                                     |
| CSS               | PostCSS with Mantine preset + simple-vars                  |

## Deployment Architecture

Runs as two Docker Compose services behind an nginx reverse proxy:

```
Browser
  │
  ▼
gateway (nginx, port from .env)
  └── /   → web (Next.js, internal port)
```

| Service   | Image / Build | Role                                                |
| --------- | -------------- | --------------------------------------------------- |
| `gateway` | `nginx:alpine` | Reverse proxy                                       |
| `web`     | `./web-app`    | Next.js 16 standalone (App Router + server actions) |

**Compose files:**

- `docker-compose.yml` — production (`.env`)
- `docker-compose.dev.yml` — live-reload; mounts `./web-app/app` and `./web-app/src` into the container
- `docker-compose.test-01.yml` — test environment (`.env.test-01`)

The backend (`auto-testrunner/`, plus `postgres` and `redis`) lives in the same compose
files, one level up — see the root `Makefile` and `docker-compose.yml` for the full stack.

## Talking to the backend

`app/devops/actions.ts` is the single `'use server'` module through which every devops
page talks to the Python API. It does two things, never a third:

- `fetch(`${TESTRUNNER}/...`)` against the Flask service (`TESTRUNNER_API_URL`, default
  `http://auto-testrunner:8080`) for everything the backend owns — PRs, task queue/status,
  dev sources, DB copies, the Odoo dev instance.
- Direct Redis reads (`REDIS_URL`) for a couple of cheap read-only counters the backend
  doesn't bother wrapping in a route.

There is no Next.js API-route layer — add new backend calls as new functions in this
file (or a sibling `actions.ts` under a new `app/devops/<page>/` if a page's actions are
substantial enough to warrant their own file), following the existing pattern: a typed
response, a plain `fetch`, throw on `!res.ok`. Mutating calls that can return a real
`{error}` message (anything under `/sources`, `/copies`, `/instance`) parse and throw
that message instead of a generic one — see `throwApiError` in `actions.ts`.

## App Routes

| Route               | Description                                                                |
| -------------------- | --------------------------------------------------------------------------- |
| `/`                  | Redirects to `/devops/control`                                              |
| `/devops/control`    | Live queue/worker/pool status, polling                                      |
| `/devops/pr-list`    | Open PRs and their test-task status, force-discover/recheck                 |
| `/devops/[hash]`     | Per-commit detail: task states, downloadable logs (`LogViewer`)             |
| `/devops/instances`  | Dev sources (test-01/test-02 base reset), named DB copies, the single Odoo dev instance (PR sync, `-i`/`-u`, attach/restart/detach) |

## Coding Style

### Imports

**Absolute imports with `@` prefixes are strongly preferred.** Two path aliases are configured in `tsconfig.json`:

| Alias    | Resolves to |
| -------- | ----------- |
| `@/*`    | `src/*`     |
| `@app/*` | `app/*`     |

Use these over relative imports whenever available.

### Lint & type checks

All code must pass both checks before submitting:

```bash
yarn lint       # ESLint 9
yarn typecheck  # tsc --noEmit
```

Do not use `@ts-ignore` or `eslint-disable` without a written justification in a comment.
