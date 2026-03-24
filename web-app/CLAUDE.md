# CLAUDE.md — case-dashboard/web-app

## Technologies

| Layer             | Tool                                                       |
| ----------------- | ---------------------------------------------------------- |
| Framework         | Next.js 16 (App Router, server actions, standalone output) |
| UI                | React 19 + TypeScript 5 (strict mode)                      |
| Component library | Mantine 8 (core, dates, hooks)                             |
| Server state      | TanStack React Query 5 (infinite pagination)               |
| Dates             | Dayjs                                                      |
| Icons             | Tabler Icons                                               |
| Editor            | CodeMirror 6 with Python support + Vim mode                |
| Linting           | ESLint 9 + TypeScript ESLint + Mantine preset              |
| Formatting        | Prettier 3 + import-sort plugin                            |
| Testing           | Jest 30 + Testing Library                                  |
| Storybook         | Storybook 10                                               |
| Package manager   | Yarn 4                                                     |
| CSS               | PostCSS with Mantine preset + simple-vars                  |

## Deployment Architecture

The app runs as **three Docker Compose services** behind an nginx reverse proxy:

```
Browser
  │
  ▼
gateway (nginx, port from .env)
  ├── /          → web (Next.js, internal port)
  └── /api/lsp   → lsp-server:3000  (WebSocket upgrade)
```

| Service      | Image / Build  | Role                                                |
| ------------ | -------------- | --------------------------------------------------- |
| `gateway`    | `nginx:alpine` | Reverse proxy; upgrades `/api/lsp` to WebSocket     |
| `web`        | `./web-app`    | Next.js 16 standalone (App Router + server actions) |
| `lsp-server` | `./lsp-server` | basedpyright WebSocket bridge for Python LSP        |

**Compose files:**

- `docker-compose.yml` — production (`.env`)
- `docker-compose.dev.yml` — live-reload; mounts `./web-app/app` and `./web-app/src` into the container
- `docker-compose.test-01.yml` — test environment (`.env.test-01`)

**Deployment:** `deploy.sh` rsyncs the repo to the remote host `arpeggio:/app/snappy-case-dashboard`, then rebuilds and restarts both the production and test-01 stacks.

## LSP Server

**Location:** `../lsp-server/` (sibling to `web-app/`)

The LSP server provides Python code intelligence (completions, diagnostics, hover) inside `PythonEditor`.

**How it works:**

1. `lsp-server/server.js` listens on port 3000 via WebSocket (`ws` package).
2. On each connection it spawns a `basedpyright-langserver --stdio` child process.
3. It bridges between the two protocols: incoming WebSocket JSON messages are wrapped with `Content-Length` headers and piped to the child's stdin; outgoing LSP responses from stdout are stripped of headers and forwarded as raw JSON over WebSocket.

**Custom Odoo type stubs:** `lsp-server/workspace/typings/builtins.pyi` declares Odoo-specific types (`Recordset`, `HelpdeskTicket`, `ResPartner`, …) so that phase code scripts get accurate autocompletion against the Odoo object model.

**Client side:** `PythonEditor` (`src/components/PythonEditor/index.tsx`) connects via the `codemirror-languageserver` extension at `wss://<host>/api/lsp` (nginx proxies and upgrades the connection). Formatting on `:w` is handled in-browser by `@wasm-fmt/ruff_fmt` (Ruff compiled to WASM).

## App Routes

| Route                                 | Description                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------ |
| `/`                                   | Case listing with filters and infinite scroll                                              |
| `/helpdesk.ticket/[id]`               | Case detail dashboard (active phase, chart, history, …)                                    |
| `/full-field-config/[model]/[record]` | Generic field inspector — shows and edits all fields on any Odoo record (debug/admin tool) |

## Odoo Data Models

The app is built around Odoo's helpdesk + a custom `symple` workflow add-on.

```
helpdesk.ticket  (the "case")
├── workflow_id              → symple.workflow
├── triplet_active_phase_id  → symple.triplet.phase   (current step)
├── stage_id                 (Solved / Done / Done KO / Cancelled …)
├── parent_case_id / child_case_ids   (recursive case hierarchy)
└── service_point_ids, integration_history_ids, market_comm_event_log_ids

symple.workflow
└── triplet_phase_id         → symple.triplet.phase   (starting node)

symple.triplet.phase          (workflow node)
├── code                     (Python script, executed by Odoo)
├── allowed_phase_result_ids → [symple.triplet.phase.result]
└── set_result_automatically  ('from_code' | …)

symple.triplet.phase.result   (workflow edge / transition)
├── starting_phase_ids       → [symple.triplet.phase]
└── next_phase_id            → symple.triplet.phase

symple.triplet.phase.history  (per-case execution log)
├── ticket_id, phase_id, phase_result_id, active_phase_id
├── error_message
└── date
```

## Workflow Chart

The workflow chart renders the `symple.workflow` graph as an interactive canvas.

**Key files** (`src/components/WorkflowFlowChart/`):

| File                 | Role                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `useWorfklowData.ts` | Recursively fetches all reachable phases and results starting from the workflow's `triplet_phase_id`. Uses two `useState` queues (`phaseIdsToFill`, `resultIdsToFill`) to lazily discover the graph in React Query. |
| `layout.ts`          | Converts phases/results into an ELK graph and runs the hierarchical layout engine (`elkjs`). Uses BPMN-style orthogonal edge routing. Returns positioned nodes.                                                     |
| `index.tsx`          | ReactFlow canvas. Phases → nodes; results → edges (`smoothstep`). Crossed/active path highlighted in teal; uncrossed nodes dimmed to 0.4 opacity. Two navigation buttons scroll to the active or starting phase.    |

**Wrapper:** `src/components/CaseWorkflowChart/index.tsx` sits between the case page and `WorkflowFlowChart`. It queries `symple.triplet.phase.history` for the case, builds the `crossedPhases` and `crossedResults` sets, and reads the workflow's starting phase — then passes everything down to `WorkflowFlowChart`.

## Odoo Bindings

All Odoo integration lives in `app/api.ts` and is **server-only** (`'use server'`).

Communication uses **JSON-RPC 2.0** against Odoo's `/jsonrpc` endpoint. Authentication is via a Bearer token obtained from Keycloak (see below).

### Core RPC wrappers (`app/api.ts`)

- `odooSearch` — search records
- `odooRead` — read fields on known IDs
- `odooWrite` — write fields on records
- `odooSearchRead` — combined search + read
- `odooFieldsGet` — introspect model fields
- `odooNameGet` — resolve display names
- `odooCallMethod` — call arbitrary model methods

### Domain helpers (`src/utils/odoo.ts`)

- `constructOdooDomain()` — build Odoo filter domains programmatically
- `OdooDomain` — TypeScript type for domain tuples
- `OdooFieldType` — union of Odoo field type strings
- `OdooFieldDefinition` — typed shape of a fields_get entry

## Authentication

Two independent auth layers are in play:

### 1. Keycloak (backend-to-backend)

A service account obtains a Bearer token that is used for **all** Odoo RPC calls. The token is cached and refreshed automatically on 401.

Required environment variables:

```
KEYCLOAK_URL
KEYCLOAK_USER
KEYCLOAK_PASSWORD
KEYCLOAK_CLIENT_ID
KEYCLOAK_CLIENT_SECRET
```

### 2. Odoo user credentials (per-user)

Each browser session stores an Odoo UID and API key in httpOnly secure cookies:

| Cookie              | Contents     |
| ------------------- | ------------ |
| `cred_odoo_uid`     | Odoo user ID |
| `cred_odoo_api_key` | Odoo API key |

- **Read**: `getCredentials()` in `app/credentials-reader.ts`
- **Write**: `saveCredentials()` server action in `app/credentials.ts`
- **UI entry point**: `CredentialsModal` component (gear icon in the app header)

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
