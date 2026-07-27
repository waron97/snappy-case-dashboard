# Snappy Dashboard → Electron/AppImage migration plan

Status: **done**. Implemented in `desktop-app/` (see `desktop-app/CLAUDE.md` for the resulting architecture). `web-app/`, `lsp-server/`, and the docker-compose/nginx/deploy.sh server-hosted deployment have been deleted — this repo is now the Electron app only. This document is kept as a historical record of the scoping decisions; nothing in it describes current state going forward.

## Desired output

A single **AppImage** (Linux; Windows `.exe` via the same Electron/`electron-builder` pipeline is a near-free byproduct if wanted, but Linux/AppImage is the primary target) that:

- Runs fully standalone on a user's machine — **no server, no docker-compose, no nginx, no shared `.env`**. The current 3-container deployment (`gateway`/`web`/`lsp-server`) is retired entirely for this build target (the server-hosted deployment can still exist in parallel if desired — this is a new distribution channel, not necessarily a replacement).
- Ships as one launchable binary a user downloads and double-clicks. First launch shows an expanded settings screen (see below) where the user enters every credential/endpoint the app needs; nothing is baked into the binary.
- Renders the current app's functionality (case list, case detail dashboard, workflow chart, RIP MFA/logs, full-field-config, DevOps work items, Python phase-code editor) as a **pure React SPA** — no Next.js, no server components, no server actions.
- Talks to Odoo/Keycloak/Azure DevOps directly from a **local Node backend embedded in the Electron main process** (or a `worker_thread` off it), reached from the renderer via **IPC**, not HTTP/server actions.
- Persists all secrets (Keycloak URL/client id/client secret/service user+password, Odoo URL/DB/service API key, the user's own Odoo uid/api-key, Azure DevOps org + PAT) in **local encrypted storage** (Electron `safeStorage`, OS-keychain-backed), entered through one expanded settings modal. No secret ships inside the binary.
- Drops the LSP-backed Python autocomplete/diagnostics/hover feature entirely. The Python editor itself (CodeMirror 6, Python syntax highlighting, Vim mode, Ruff formatting via `@wasm-fmt/ruff_fmt` WASM — all already client-side/in-browser) **stays and keeps working**, just without the language-server smarts. The sibling `lsp-server/` service is deleted from this build's dependency tree.

**Definition of done:** a person with no prior access to the current server can download the AppImage, run it, fill in their own Odoo/Keycloak/DevOps credentials in Settings, and use every current feature of the app (except LSP autocomplete) against the real backend services, with nothing routed through `snappy-case-dashboard`'s current server infrastructure.

## Locked-in decisions (from scoping discussion — do not re-litigate without reason)

1. **Shell: Electron**, not Tauri. Reason: the app's backend logic needs a real Node runtime to run (fetch-based Odoo JSON-RPC, Keycloak token exchange, Azure DevOps REST calls) — Electron bundles Node in its main process for free; Tauri would require shipping a separate Node sidecar binary per platform, which erases Tauri's usual size/memory advantage for this specific use case.
2. **Communication: IPC**, not localhost HTTP. `contextBridge.exposeInMainWorld` in a preload script + `ipcMain.handle`/`ipcRenderer.invoke`, not a spawned HTTP server.
3. **Secrets: 100% local, 100% user-entered.** No shared/baked service credentials of any kind. Every current `.env` value that isn't a plain non-secret endpoint becomes a settings-modal field, stored via `safeStorage`.
4. **LSP: dropped, editor kept.** No attempt to bundle `basedpyright` / Python runtime for the desktop build.
5. **No DB, ever.** Consistent with the existing app's philosophy — local encrypted settings file, not sqlite/etc.

## Architecture: before → after

**Before (current, server-hosted):**
```
Browser → nginx gateway → Next.js (App Router, SSR + server actions) → Odoo / Keycloak / Azure DevOps
                        → lsp-server (WebSocket) → basedpyright
Per-user secrets: httpOnly cookies, read server-side via next/headers
Shared secrets: root .env, read via process.env inside server actions
```

**After (AppImage):**
```
Electron BrowserWindow (renderer: pure React SPA, Vite build)
   ⇅ IPC (contextBridge / ipcMain.handle)
Electron main process (or worker_thread): plain Node modules (ported from app/api.ts, app/devops-api.ts)
   → Odoo / Keycloak / Azure DevOps (direct fetch, same as today)
All secrets: local encrypted file via Electron safeStorage, edited through Settings modal
No nginx, no lsp-server, no docker-compose, no cookies.
```

## Work breakdown (estimate: ~9-14 focused days, pre-polish)

### 1. SPA port (2-4 days)
- New Vite + React project (or Vite config added alongside, then old `app/`/Next scaffolding removed once ported).
- Replace Next's file-based routing with `react-router` (or similar) covering: `/`, `/helpdesk.ticket/[id]`, `/full-field-config/[model]/[record]`, `/rip/mfa`, `/rip/logs`, `/symple.workflow`, `/devops/work-items`.
- Port `app/layout.tsx`'s header/shell into a plain top-level `<App>` component (Mantine `MantineProvider`, theme, header, nav — all framework-agnostic already).
- Remove: `next/font` (swap for a normal `@font-face`/Google Fonts `<link>`), `ColorSchemeScript` (Mantine has a CSR-only equivalent or just default the color scheme), `next/navigation`'s `redirect()`, `Metadata` export (replace with plain `<title>`/`document.title` handling).
- Drop `output: 'standalone'` and all Next-specific config once nothing depends on it.

### 2. Server-action functions → plain Node modules (1-2 days)
- `app/api.ts` and `app/devops-api.ts` are already plain `fetch`-based async functions with minimal Next coupling (`cookies()`, `redirect()` are the only Next-specific calls) — port near-verbatim into new main-process/worker modules (e.g. `electron/backend/odoo.ts`, `electron/backend/devops.ts`).
- Replace every `getCredentials()`/`cookies()` read with a call into the new local settings store (see #4).
- Token caching pattern (`tokenPromise`/`getCachedToken`/`invalidateToken` in `api.ts`) carries over unchanged — still just module-level state, now living in the main process instead of a Next server process.

### 3. IPC bridge + callsite migration (2-3 days)
- One `ipcMain.handle('channel:name', ...)` per exported backend function: `odooSearch`, `odooRead`, `odooWrite`, `odooSearchRead`, `odooFieldsGet`, `odooNameGet`, `odooCallMethod`, `getMyWorkItems`, `getSettings`/`saveSettings` (replacing `getCredentials`/`saveCredentials`).
- Preload script exposes a typed `window.api.*` surface via `contextBridge`.
- Update every caller — grep hit list to revisit: `app/page.tsx`, `app/rip/mfa/page.tsx`, `app/rip/logs/page.tsx`, `app/full-field-config/[model]/[record]/page.tsx`, `app/helpdesk.ticket/[id]/*`, `app/symple.workflow/page.tsx`, `app/devops/work-items/page.tsx`, `src/components/CaseChildren`, `CaseMarketComm`, `CaseLogs`, `RipLogModal`, `CaseStagingArea`, `CaseIntegrationHistory`, `WorkflowFlowChart/useWorfklowData.ts`, `CredentialsModal` (becomes the new Settings modal). Swap `import { x } from '@app/api'` → `window.api.x(...)`. TanStack Query `queryFn`/mutation shape is otherwise unchanged.

### 4. Unified local-secrets settings modal + storage (2-3 days)
- Replace `CredentialsModal` with a larger **Settings** modal, grouped by section:
  - **Keycloak**: URL, client id, client secret, service username, service password
  - **Odoo**: URL, DB, service API key, your Odoo UID, your Odoo API key
  - **Azure DevOps**: org, personal access token
- Storage: a local JSON file (e.g. `app.getPath('userData')/settings.enc`) encrypted with Electron's `safeStorage.encryptString`/`decryptString`. Main process exposes `getSettings`/`saveSettings` over IPC; no more httpOnly cookies anywhere.
- Every `process.env.X` read remaining in the ported backend modules (`KEYCLOAK_URL`, `ODOO_URL`, `DEVOPS_ORG`, etc.) gets rerouted to read from this store instead.
- The existing "please configure credentials" full-screen gate (`app/layout.tsx` lines ~86-108) is the right UX precedent to keep — just re-key it off "required settings present" rather than "Odoo cookies present".

### 5. Electron shell + AppImage packaging (1-2 days)
- `electron-builder` config targeting `AppImage` (Linux) at minimum; `nsis`/`dmg` targets are close to free once the main config exists, if wanted later.
- Main process: create `BrowserWindow`, load the built Vite `index.html` (or `file://` in production, `localhost:5173` in dev), wire preload script.
- No more embedded Next server, no port management — this step is simpler than the earlier "wrap the existing Next server" idea that was scoped before the full-rewrite decision.

### 6. LSP removal + editor cleanup (0.5-1 day)
- Strip `codemirror-languageserver` usage and the `wss://.../api/lsp` connection logic from `src/components/PythonEditor/index.tsx`.
- Delete/detach the `lsp-server/` sibling directory from this build's dependency tree (it can remain in the repo for the still-existing server-hosted deployment, if that deployment mode is kept around).
- Remove the `ws` dependency if nothing else in `web-app` uses it.
- Verify Ruff formatting (`:w` in Vim mode) and Python syntax highlighting still work with no LSP connection — they're WASM/client-side already, should be unaffected.

## Explicitly out of scope / not estimated above

- Code signing (mac notarization, Windows Authenticode) — additive, not started.
- Auto-update — AppImage auto-update via `electron-builder`'s generic/AppImage updater needs an update-feed host; decide later whether that's wanted (it would reintroduce a small server dependency purely for version checks).
- Whether the existing server-hosted deployment (`docker-compose.yml` + nginx + nightly `deploy.sh` to `arpeggio`) is kept running alongside the AppImage, retired, or becomes dev-only. Not decided — doesn't block this migration either way since they'd be separate build targets from the same `web-app` source tree (until/unless the Next-specific code is deleted outright).
- Multi-window/tray-icon/native-menu polish.
- Windows/mac builds beyond "should be close to free with electron-builder" — not verified.

## Open questions for the next session

1. Does the settings modal need per-field validation/test-connection buttons (e.g. "Test Keycloak connection" before saving), or is silent fail-on-first-use acceptable, consistent with today's UX?
2. Should the server-hosted deployment keep existing after this migration, or is the AppImage meant to fully replace it? Affects whether Next.js code gets deleted or kept as a second build target.
3. Any target beyond Linux/AppImage for v1 (Windows `.exe`, mac `.dmg`)?
4. Confirm final list of settings fields — is the Odoo "service API key" (currently the Keycloak-authenticated shared service account used for all Odoo calls regardless of user) still a needed concept once secrets are per-install, or does every user just use their own Odoo uid/api-key directly for RPC and the Keycloak layer goes away too? (Current code always goes through the Keycloak-obtained bearer token *plus* the per-user uid/api-key inside the JSON-RPC call args — worth confirming this dual-auth model is still required, or if it was only serving multi-tenant server needs that don't apply to a single local install.)
