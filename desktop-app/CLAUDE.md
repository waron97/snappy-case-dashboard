# CLAUDE.md — snappy-case-dashboard/desktop-app

## Technologies

| Layer             | Tool                                                  |
| ------------------ | ------------------------------------------------------ |
| Shell              | Electron (main process, preload, renderer)             |
| Bundler            | Vite via `electron-vite`                                |
| UI                 | React 19 + TypeScript 5 (strict mode)                   |
| Routing            | react-router v7 (`HashRouter` — required under `file://`) |
| Component library  | Mantine 8 (core, dates, hooks)                          |
| Server state       | TanStack React Query 5 (infinite pagination)            |
| Dates              | Dayjs                                                   |
| Icons              | Tabler Icons                                            |
| Editor             | CodeMirror 6 with Python support + Vim mode (no LSP)    |
| Packaging          | electron-builder → Linux AppImage/deb, Windows NSIS installer, auto-update via `electron-updater` off public GitHub Releases |
| Package manager    | npm (`legacy-peer-deps=true` in `.npmrc` — needed for `react-json-view`'s stale React peer range) |

## Architecture

Fully standalone desktop app. No server, no docker, no shared secrets. Everything the old `web-app` server-hosted deployment needed now lives locally:

```
Electron BrowserWindow (renderer: React SPA, HashRouter)
   ⇅ IPC (contextBridge / ipcMain.handle) — see src/preload/index.ts, src/main/ipc.ts
Electron main process
   → src/main/backend/{keycloak,odoo,devops}.ts — direct fetch to Odoo/Keycloak/Azure DevOps
   → src/main/backend/settings.ts — safeStorage-encrypted local settings file
```

- `src/main/` — Electron main process: window creation, IPC handlers, backend modules.
- `src/preload/` — `contextBridge` surface exposed to the renderer as `window.api`.
- `src/renderer/src/` — the React SPA (routes, components, hooks, lib).

No LSP server, no nginx, no docker-compose. The old 3-container deployment (`gateway`/`web`/`lsp-server`) and the Next.js app it ran are gone — this repo directory is the entire application.

## Settings & auth

All credentials are entered once by the user into the Settings modal (gear icon, top right) and persisted encrypted via Electron `safeStorage` at `app.getPath('userData')/settings.enc`. See `src/main/backend/settings.ts` for the full field list and `src/renderer/src/components/SettingsModal/index.tsx` for the form. Access the current values from renderer code via `useSettings()` in `src/renderer/src/lib/settings.tsx`.

Two independent auth layers, unchanged in shape from the old server-hosted app, just re-sourced from local settings instead of `.env`/cookies:

1. **Keycloak** (`keycloakUrl`/`keycloakClientId`/`keycloakClientSecret`/`keycloakServiceUsername`/`keycloakServicePassword`) — a service-account bearer token used for **all** Odoo/Bit2win RPC calls. Cached and refreshed on 401 (`src/main/backend/keycloak.ts`).
2. **Odoo user identity** (`odooUid`/`odooApiKey`) — the user's own uid/API key, sent inside every `execute_kw` call's args alongside the Keycloak bearer token. These two fields gate the app: the "Please Configure Your Settings" overlay shows until both are non-empty (`isConfigured` in `src/renderer/src/lib/settings.tsx`).

No test-connection validation — a blank/wrong field surfaces as a `ConnectError`/`AuthError` the first time it's actually used, matching the old app's behavior with a misconfigured `.env`.

## IPC surface

One channel per backend function, registered in `src/main/ipc.ts`, exposed to the renderer via `window.api.*` in `src/preload/index.ts`. Renderer code never calls `window.api.*` directly — use the shims in `src/renderer/src/lib/odoo-api.ts` and `src/renderer/src/lib/devops-api.ts`, which export the same function names/signatures the old `app/api.ts`/`app/devops-api.ts` server actions used (`odooSearch`, `odooRead`, `odooWrite`, `odooSearchRead`, `odooFieldsGet`, `odooNameGet`, `odooCallMethod`, `callBit2win`, `getAssets`, `getMyWorkItems`).

Note: `callBit2win`'s `params?: URLSearchParams` is converted to a plain tuple array at the IPC boundary (`URLSearchParams` isn't structured-clone-safe over `contextBridge`) and reconstructed in `src/main/ipc.ts`'s `b2w:call` handler.

## App Routes

Most routes are wired in `routes/index.tsx` under `<AppRoutes/>`. `/`, `/helpdesk.ticket/:id`, and `/full-field-config/:model/:record` are the exception: they're all owned by `components/CasesWorkspace/`, mounted as a permanent sibling of `<AppRoutes/>` in `App.tsx`'s `Shell()` (outside the `<Routes>` switch) rather than as `<Route>` entries, so it never unmounts when the user switches between tabs. Every open tab (case detail or field inspector) is a real Mantine `Tabs.Panel` kept mounted — see `lib/caseWorkspace.tsx` (`CaseTabsProvider`), `lib/caseWorkspaceContext.ts` (the `CaseWorkspaceTab` union + `tabKey`/`tabPath` helpers) for the tab state.

| Route                                  | File                          | Description                                              |
| ---------------------------------------- | ------------------------------ | ----------------------------------------------------------- |
| `/` *(outside `<Routes>`, see above)*     | `components/CasesWorkspace/`, `CaseList.tsx` | Case list + tab strip — the list is the permanent leftmost tab |
| `/helpdesk.ticket/:id` *(outside `<Routes>`, see above)* | `components/CasesWorkspace/`, `CaseDetail.tsx` | Opening a case adds/focuses a closable tab; background tabs stay mounted |
| `/full-field-config/:model/:record` *(outside `<Routes>`, see above)* | `components/CasesWorkspace/`, `FullFieldConfig.tsx` | Generic field inspector — any Odoo record (debug/admin); also opens as a closable tab (e.g. from the `</>` buttons or Ctrl+E) |
| `/rip/mfa/:id?`                          | `components/MfaWorkspace/`, `RipMfaList.tsx`, `RipMfaDetail.tsx` | MFA list always visible; opening a record slides up a bottom `Drawer` |
| `/rip/logs`                              | `RipLogs.tsx`                   | Log listing/viewer                                           |
| `/symple.workflow/:id`                   | `SympleWorkflowDetail/`         | Workflow phase/results editor                                |
| `/devops/work-items`                     | `DevOpsWorkItems.tsx`           | "My Work Items" from Azure DevOps                             |

## Odoo Data Models

Unchanged from the old app — see the original data-model diagram if needed (helpdesk.ticket / symple.workflow / symple.triplet.phase / symple.triplet.phase.result / symple.triplet.phase.history). Domain helpers live in `src/renderer/src/utils/odoo.ts` (`constructOdooDomain`, `OdooDomain`, `OdooFieldType`, `OdooFieldDefinition`).

## Coding style

### Imports

`@/*` resolves to `src/renderer/src/*` (renderer only — see `tsconfig.web.json` and `electron.vite.config.ts`). Prefer it over relative imports for anything crossing a directory boundary.

### Checks

```bash
npm run typecheck   # tsc --noEmit, both main/preload and renderer configs
npm run lint        # ESLint 9
npm run build        # typecheck + electron-vite build
```

### Packaging

```bash
npm run build:appimage   # Linux AppImage
npm run build:deb        # Linux .deb
npm run build:win        # Windows NSIS installer (cross-built from Linux)
npm run build:mac        # macOS dmg + zip (must run on a macOS host — no cross-build)
npm run build:all        # win + linux (still Linux-host only)
npm run release          # win + linux, publish to GitHub Releases (needs GH_TOKEN)
npm run release:mac      # mac, publish to GitHub Releases (needs GH_TOKEN, macOS host)
```

Output lands in `dist/`, artifact names have no version suffix (`Snappy.AppImage`, `Snappy.deb`, `Snappy-Setup.exe`, `Snappy.dmg`, `Snappy.zip`) — see `electron-builder.yml`'s `artifactName` overrides.

`.github/workflows/release.yml` (repo root) builds on tag push (`v*`): one job on `ubuntu-latest` for win+linux (wine cross-build, as below), one job on `macos-latest` for mac (native — `electron-builder` cannot cross-build mac from Linux, needs real `hdiutil`/codesign tooling). Both publish to the same GitHub Release via the default `GITHUB_TOKEN`. Free on `macos-latest` for a public repo (unlimited minutes); a private repo would burn Actions minutes at a 10x multiplier for mac jobs.

Windows target is `nsis`, not `portable` — a real (one-click, per-user, no admin needed) installer, required so `electron-updater` has something to update in place. Switching back to `portable` would break Windows auto-update.

Known runtime caveat: AppImages built by electron-builder require `libfuse2` on the host to self-mount. Distros without it by default (Ubuntu 22.04+, Debian 12+) will fail to launch the AppImage until it's installed.

Cross-building the Windows target from Linux requires `wine` on the host (electron-builder shells out to it via `rcedit`/`signtool` to set the exe icon/metadata, even unsigned).

**Mac is unsigned/unnotarized.** No Apple Developer Program enrollment ($99/yr) configured, so the `.dmg`/`.zip` aren't codesigned or notarized. Consequence: Gatekeeper blocks first launch ("unidentified developer" — user must right-click → Open, or `xattr -d com.apple.quarantine`), and `electron-updater`'s `Squirrel.Mac` backend verifies code signatures before applying an update, so **auto-update on mac will not work reliably** until signing/notarization is added (Apple dev account + `APPLE_ID`/`APPLE_APP_SPECIFIC_PASSWORD` or API key secrets + `notarize` config/`afterSign` hook). Win (NSIS) and Linux (AppImage) auto-update are unaffected by this.

### Auto-update

`electron-updater` (`src/main/updater.ts`) checks the public GitHub Releases feed for `waron97/snappy-case-dashboard` (see `publish:` in `electron-builder.yml`) on launch and every 4 hours, only in packaged builds (`app.isPackaged` guard — it throws under `npm run dev`, which has no `app-update.yml`). Downloads happen silently in the background; once `update-downloaded` fires, the renderer shows a persistent toast (`components/UpdateNotifier/`) with a "Restart & update" button that calls `quitAndInstall()` via IPC (`updater:quitAndInstall`).

Only AppImage and NSIS support in-place auto-update (mac's `zip` target is the update payload `Squirrel.Mac` needs, but see the signing caveat above — unsigned builds won't actually apply it). The `.deb` artifact still gets built and published, but `electron-updater` doesn't update it — deb users update by reinstalling the new `.deb` manually. `npm run release`/`release:mac` require a `GH_TOKEN` env var (repo scope) to upload build artifacts to the release; downloading them at runtime needs no token since the repo is public.

`productName` (electron-builder.yml) is `Snappy` — the display name shown in Explorer/Start Menu/taskbar. Deliberately kept separate from package.json's `name` (`desktop-app`), which is what Electron's `app.getName()` actually uses for the userData directory (`~/.config/desktop-app` on Linux) — changing `productName` doesn't move or orphan a user's existing encrypted settings.
