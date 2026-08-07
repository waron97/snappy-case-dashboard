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

Credentials are entered by the user on the Settings page (gear icon, top right → `/settings`) and persisted encrypted via Electron `safeStorage` at `app.getPath('userData')/settings.enc`. See `src/main/backend/settings.ts` for the full field list and `src/renderer/src/components/SettingsPage/index.tsx` for the form. Access the current values from renderer code via `useSettings()` in `src/renderer/src/lib/settings.tsx`.

Settings are **multi-profile** (`SettingsStore { profiles: Profile[]; activeProfileId }`) — a profile is effectively an environment/tenant, and `getSettings()` returns the active one flattened so `keycloak.ts`/`odoo.ts`/`devops.ts` need not know profiles exist. Switching profiles clears open tabs and hard-reloads the renderer to drop stale React Query cache and the cached Keycloak token. Three further `safeStorage`-encrypted stores sit alongside `settings.enc`: `ui-prefs.enc` (global; holds `caseWorkspaceOpenTabs`, colour scheme, editor prefs — localStorage was deliberately removed, it cost ~3.5s on first touch under `file://`), `saved-domains.enc` (global), and `saved-tab-sets.enc` (per profile).

Two independent auth layers, unchanged in shape from the old server-hosted app, just re-sourced from local settings instead of `.env`/cookies:

1. **Keycloak** (`keycloakUrl`/`keycloakClientId`/`keycloakClientSecret`/`keycloakServiceUsername`/`keycloakServicePassword`) — a service-account bearer token used for **all** Odoo/Bit2win RPC calls. Cached and refreshed on 401 (`src/main/backend/keycloak.ts`).
2. **Odoo user identity** (`odooUid`/`odooApiKey`) — the user's own uid/API key, sent inside every `execute_kw` call's args alongside the Keycloak bearer token. These two fields gate the app: the "Please Configure Your Settings" overlay shows until both are non-empty (`isConfigured` in `src/renderer/src/lib/settings.tsx`).

No test-connection validation — a blank/wrong field surfaces as a `ConnectError`/`AuthError` the first time it's actually used, matching the old app's behavior with a misconfigured `.env`.

## IPC surface

One channel per backend function, registered in `src/main/ipc.ts`, exposed to the renderer via `window.api.*` in `src/preload/index.ts`. Renderer code never calls `window.api.*` directly — use the shims in `src/renderer/src/lib/odoo-api.ts` and `src/renderer/src/lib/devops-api.ts`, which export the same function names/signatures the old `app/api.ts`/`app/devops-api.ts` server actions used (`odooSearch`, `odooRead`, `odooWrite`, `odooSearchRead`, `odooFieldsGet`, `odooNameGet`, `odooCallMethod`, `callBit2win`, `getAssets`, `getMyWorkItems`).

Note: `callBit2win`'s `params?: URLSearchParams` is converted to a plain tuple array at the IPC boundary (`URLSearchParams` isn't structured-clone-safe over `contextBridge`) and reconstructed in `src/main/ipc.ts`'s `b2w:call` handler.

The `symphony:*` channels (`window.api.symphony.*`, shimmed by `src/renderer/src/lib/symphony-api.ts`) cover the Bit2win Symphony engine, backed by `src/main/backend/symphony/`. It does **not** reuse `callBit2win`: that helper hardcodes an `output: all` header, always parses JSON, and rejects any non-200, none of which suits Symphony (the execution-tree detail endpoint returns `text/html`). `symphony/client.ts` has its own fetch with a mandatory timeout and the same 401-retry shape. Nested under the same namespace are `processKeys.*` (the BPMN-definition catalog — enumerating it costs ~58MB/~20s because every row carries a base64 SVG, so it is stripped and cached per profile in plain JSON at `userData/symphony-process-keys.json`) and `deepSearch.*` (the sweep engine; `symphony:deepSearch:progress` is a main→renderer push, subscribed in exactly one place, `lib/symphonyDeepSearch.ts`).

Symphony API gotchas, all verified against the live API. The filter ones are handled in `components/SymphonyFilters/types.ts`; the catalog ones in `symphony/catalog.ts`. The recurring theme: **several params look like hints but are actually allowlists, and several response fields look like totals but are caps** — so "send everything we know about" and "divide by the reported number" are both wrong by default.

- **`deadJob` is a state, not a toggle.** It means the engine failed to execute a process state because of a malformation, as opposed to a normal business error (e.g. a 400 from an external call). It is **never a no-op**: with no statuses selected, `deadJob: true` narrowed a 7-row window to 0 — it constrains rather than includes. So `resolveDeadJob()` / `resolveJobDeadJob()` send it **only when the box is ticked**, and omit it otherwise. It stays a separate wire param and lives outside `Checkbox.Group`, which drives descendants from its own `value` array and ignores `checked`.
- **The persisted catalog carries a `schemaVersion`** (`SCHEMA_VERSION` in `catalog.ts`), and a mismatch counts as stale regardless of age. Without it, a catalog cached by an older build was served as fresh for the full 12h TTL, so shipping a change that adds keys appeared to do nothing. Bump it whenever the sources or the stored shape change. **The check must live in main, not the renderer**: `useSymphonyProcessKeys` passes the persisted copy to react-query as `initialData` with `initialDataUpdatedAt: fetchedAt` and a 12h `staleTime`, so anything main hands over suppresses the network query entirely and `isFresh()` never runs. That is why IPC serves `getUsableCachedCatalog` (withholds a foreign-schema catalog, so the sweep runs at once) rather than `getCachedCatalog` — a v1 cache otherwise kept the process-builder source invisible for 12h after it shipped, and its unstripped names match zero request rows. A current-schema catalog is still served at any age: instant render, background refetch.
- **`listStatusSelected` is an ALLOWLIST — never send a "complete" set.** Symphony has statuses beyond the five the legacy filter bar exposes (at minimum `RESUBMIT`), so enumerating CANCELLED/NEW/COMPLETED/WORKING/FAILED silently drops rows. Verified on a one-minute window: omitting the param returned 7 rows including a `RESUBMIT`; sending the five returned 6. **Omitting is the only way to say "any status"**, so `resolveStatuses()` / `resolveJobStatuses()` return `undefined` when nothing is ticked rather than expanding. The checkboxes start unticked, and a job stores `statuses: []` verbatim so they render as the user left them. The same applies to the exact-id lookups in `SymphonyRequestDetail` — filtering those by the five statuses hid a `RESUBMIT` request and made a live process look nonexistent.
- **A request's `processKey` is the BPMN definition name with its deployment prefix stripped.** Definition `B2WA_async_case_engine` produces requests keyed `async_case_engine`, and `getRequestTree`'s `name` filter matches **only the stripped form** — passing the prefixed name returns zero rows. `catalog.ts` therefore strips `B2WA_`/`B2W_` on ingest and stores the request-facing key as `name` (keeping the original as `definitionName`). Measured against a live sample of 54 request keys, the raw names covered 1; stripped, 48.
- **Two catalog sources.** Deployed BPMN definitions (`SymphBpmnFileTabCon`, `latestVersion=true`) plus **process builders** at `/api/processbuilder/v1/builder/process` — a different base path, same bearer token, ~26MB because each row embeds its pages/structure, so rows are stripped on ingest just like the BPMN SVGs. Builder-spawned processes are not deployed BPMN files, so they appear nowhere in the first source. Together ~650 keys (361 BPMN + 291 builder `document_id`s, measured live). A process builder's `document_id` is the key; its `process_name` is a human label ("Ricostruzione Consumi") with zero overlap with request keys, so it is used only as a description. A PB fetch failure is non-fatal — the BPMN half still loads.
- **Even so, the list is not a superset of keys on requests.** The remaining gap is versions: the BPMN sweep pins `latestVersion=true`, so a request started against a superseded definition carries a key that is in neither source. So `ProcessKeySelect` is an `Autocomplete`, not a `Select`: suggestions with arbitrary values still accepted, plus a hint when the typed key is unknown. Its filter strips the prefix from the *query* too, so pasting a full definition name still finds the option. `client.ts` additionally records the `processKey` of every row the request list returns (`recordObservedProcessKeys`), and those keys are served over `symphony:listObservedProcessKeys` and unioned into the picker's options — by construction they are exactly what the `name` filter can match, so they are always valid. Note `sweep()` shares one JSON file with them and must spread the store when persisting or it drops `observed`. (An older note here claimed `ml_voltura_data_input` existed in neither catalog; it is in fact a builder `document_id` — that measurement came off a stale v1 cache.)
- **`maximumRecordsNumber` is the enumeration CAP, not a total** — a constant 10000, returned unchanged by a query matching 14 rows. There is **no** way to ask Symphony how many requests match a filter. That is why the deep-search UI shows counts only and has no progress bar: any percentage would be dividing by an invented number. `SweepSegment.reportedTotal` keeps the value solely for the truncation check (`tableLimit`, or offset+page >= cap), and must never become a denominator.

### Symphony processes on a case

Odoo keeps a case's Symphony ids in **three** places, all surfaced by the "Symphony processes" tab (`components/CaseSymphonyProcesses`):

1. `helpdesk.ticket.symphonie_process` — the current long-running-process id.
2. `symphony.case.id` — the history. `helpdesk.ticket.write()` appends a row on every write of `symphonie_process`, so earlier values survive being overwritten.
3. `symple.pb.instance.key` — written by `set_instance_key(instance_key, process_name, state_code, status)` on completing a wizard. The only source carrying more than a bare id: it has the process name and the wizard outcome. Filter on the stored related `res_model` char rather than traversing `res_model_id`.

Note `symphony.process` / `symple_symphony_process` is **not installed** on at least one environment ("Object symphony.process doesn't exist"), so every source is fetched independently and a missing model degrades to no rows rather than failing the tab.

**None of these records which kind of id it stored** — a value may be a request id or a process-instance id. `SymphonyRequestDetail` therefore tries a `requestId` lookup and falls back to a `processId` one, and rows open with `processId: NO_PROCESS_ID` until it resolves.

A sweep's variable query is a list of clauses (`SweepPredicate.clauses`) combined by `mode: 'all' | 'any'`. Within one clause the name and value must match the SAME variable; across clauses under `all`, each may be satisfied by a *different* variable of the same process instance — that cross-variable behaviour is the point, and is verified against live data (A=`name~search`, B=`value~Domestico`, which land on disjoint variables, yet `A AND B` matches). `normalizePredicate` migrates the pre-multi-clause `{name, value}` shape, since job headers are plain JSON with no version field. Recorded evidence is collected one-match-per-clause first, then extras up to `MAX_MATCHES_PER_REQUEST` — a flat cap filled in variable order hid whole clauses from the hits table.

A deep-search job's request filter is editable after creation (paused jobs only). Changing it **resets the job**: the scanned-id set, cursor and hits all describe the old query, so `updateSweep` clears the log, rebuilds the segments and zeroes the counters.

A sweep splits its date range into per-day windows (`buildSegments`) when the range spans more than `SEGMENT_THRESHOLD_DAYS`, because the 10000 cap is *per query* — a per-day query essentially never trips it while a month-wide one on a busy tenant is guaranteed to. **Known gap:** a job with no start date gets a single unbounded window, since `buildSegments` bails out when either bound is unparseable. That is the shape most likely to hit the cap, so it is exactly backwards; the UI warns on draft jobs with no start date, but the real fix is to segment backwards from the end until a window comes back empty.

Deep-search sweeps persist to `userData/sweeps/<profileId>/<jobId>.{job,log}` and deliberately break from the `.enc` store pattern: those stores rewrite and re-encrypt the whole document on every mutation, which a sweep performs thousands of times. Instead a small header is atomically rewritten at most every 3s and results go to an append-only, per-line-encrypted log. **On load the log is authoritative** — the scanned-id set, hits and counters are all replayed from it, so a crash can never leave the header and the log disagreeing in a way that matters.

## App Routes

**There is no `<Routes>` switch.** Every page is a tab in `components/CasesWorkspace/`, which is the only content renderer besides the settings page. `TAB_ROUTES` in `lib/caseWorkspaceContext.ts` is the app's single route table: `tabFromPath(pathname)` maps a URL to a tab, `tabPath(tab)` maps it back, and a `useLocation`-driven effect in `lib/caseWorkspace.tsx` applies the result. That indirection is what lets any plain `<Link>` anywhere in the app open a tab without knowing the tab system exists. `/settings` is the one exception (`NON_TAB_PATHS`): it renders in its own branch of `App.tsx`, outside the `isConfigured` gate, because it's the only way out of an unconfigured install.

Every open tab is a Mantine `Tabs.Panel` kept mounted, so switching tabs preserves filters, scroll and unsaved edits. Consequences worth knowing: a panel's queries keep running in the background (each page gates its *first* fetch behind `useVisitedGate`, so an unvisited restored tab costs nothing), and anything portalled out of a panel — `Modal`, `Drawer` — is **not** hidden by the panel's `display: none`, so it must gate `opened` on `useTabIsActive()` (`lib/tabActive.ts`) or it floats over whichever tab the user switched to.

| Route | Tab kind | File | Description |
| --- | --- | --- | --- |
| `/` | `list` | `components/CasesWorkspace/`, `CaseList.tsx` | Case list — the permanent, non-closable leftmost tab |
| `/helpdesk.ticket/:id` | `case` | `CaseDetail.tsx` | One case per tab |
| `/full-field-config/:model/:record` | `field-config` | `FullFieldConfig.tsx` | Generic field inspector — any Odoo record (debug/admin); from the `</>` buttons or Ctrl+E |
| `/symphony/requests` | `symphony-list` | `SymphonyRequests.tsx` | Symphony (Bit2win BPMN engine) request list. Singleton |
| `/symphony/request/:requestId/:processId` | `symphony-request` | `SymphonyRequestDetail/` | One Symphony request: all variables (filterable as one set, JSON viewer) + condensed activity history. `:processId` is `-` when unknown, then resolved by an exact `requestId` lookup |
| `/symphony/deep-search/:jobId` | `symphony-deep-search` | `SymphonyDeepSearch/` | A resumable client-side sweep that pages requests and matches inside their variables (the API has no server-side variable filter) |
| `/rip/mfa/list/:instance` | `rip-mfa-list` | `RipMfaList.tsx` | MFA list. **Multi-instance** — every RIP → MFA click opens another one with its own filters |
| `/rip/mfa/:id` | `rip-mfa` | `RipMfaDetail.tsx` | One MFA record per tab (code editor + metadata + recent calls) |
| `/rip/logs/:instance` | `rip-logs` | `RipLogs.tsx` | Log listing/viewer. **Multi-instance**, as above |
| `/symple.workflow/:id` | `symple-workflow` | `SympleWorkflowDetail/` | Workflow phase/results editor |
| `/devops/work-items` | `devops-work-items` | `DevOpsWorkItems.tsx` | "My Work Items" from Azure DevOps. Singleton |

`:instance` is a counter minted by `newInstance()` in an event handler (never in `tabFromPath`, which must stay pure — it runs in a StrictMode-double-invoked effect). It is what makes those two kinds multi-instance: it's part of both `tabKey` and the URL, so each tab stays individually addressable and append-if-absent still de-duplicates. `HeaderNav` therefore calls `openTab` rather than using `<Link>` — a second `<Link to="/rip/logs">` wouldn't change the pathname, so no second tab would appear.

### Adding a tab kind

Add the variant to `CaseWorkspaceTab` (it **must** carry `label`, or `sanitizeTabs` drops it) and the compiler walks you through the rest: `tabKey`, `tabPath`, `defaultLabel`, `TAB_ROUTES` and `TAB_VALIDATORS` are all keyed off the union, and `TabPanelContent`'s switch ends in a `never` guard. Not enforced, so easy to forget: the page itself must take its identity as **props, not `useParams`** (panels render outside any `<Route>`, so `useParams()` returns `{}` and every id becomes `NaN`), pass `isActive` to `useDocumentTitle` and to `useVisitedGate` for its `enabled:`, and report its resolved name via `useResolvedTabName`.

Two invariants in `TAB_ROUTES` worth preserving: every pattern is matched with `end: true`, which makes them mutually exclusive and iteration order irrelevant (`/rip/mfa/:id` can't swallow `/rip/mfa/list/:instance`); and `toTab` returns `null` for anything it can't parse, so a junk URL yields no tab rather than one keyed `case:NaN`. The `decodeURIComponent` calls on Symphony ids are required, not redundant — `useMatch` decodes the pathname before matching, bare `matchPath` does not.

### The refresh button

The ⟳ in the tab strip bumps a counter in `lib/refresh.ts`'s `RefreshProvider`. Every mounted panel already reads that context, so a bump re-renders all of them and each decides for itself — via `useTabIsActive` — whether it is the tab the user is looking at. **Only the active tab refetches**; an unscoped `queryClient.invalidateQueries()` would hit every open tab at once, which is exactly what `useVisitedGate` exists to avoid. Nothing is registered or keyed by tab, so nothing has to be cleaned up when a tab closes.

The convention is to call `useRefreshQueries(...keys)` **next to the `useQuery` it refreshes**, at whatever depth that is, rather than hoisting a list of keys up to the page — `useTabIsActive` works anywhere inside a panel, so a query added later brings its own refresh with it. Keys match by prefix, so `['case', id]` covers `['case', id, 'symphony-processes']`.

Three deliberate omissions, all of which would do harm rather than good: `['symphony', 'processKeys', …]` (the catalog is a ~20s/~58MB sweep behind a 12h `staleTime`); `['phase', …, 'for-active-phase']` in `CaseActivePhase`, and `WorkflowFlowChart`, which accumulates into local state and stops fetching once `isDone`. The `CaseActivePhase` case is the subtle one: it re-seeds `form.code` whenever that query's data changes *identity*, so a refresh that picked up someone else's write would silently replace unsaved edits. Structural sharing (on by default, and `QueryProvider` is a bare `new QueryClient()`) keeps the reference stable when a refetch returns the same payload, so ordinary window-focus refetches are harmless — the seed-once-per-record guard in `MfaCode` is what closes the remaining conflict window.

Related but separate: `CaseDetail`'s base-view query drops its 3s `refetchInterval` while the case is unlocked (`refetchInterval: isCaseDone || !isLocked ? undefined : 3 * 1000`) so polling doesn't churn under an open editor. That guard is on the base-view poll only — it does not gate `enabled` on any `CaseActivePhase` query, and it does not affect window-focus refetches.

## Odoo Data Models

Unchanged from the old app — see the original data-model diagram if needed (helpdesk.ticket / symple.workflow / symple.triplet.phase / symple.triplet.phase.result / symple.triplet.phase.history). Domain helpers live in `src/renderer/src/utils/odoo.ts` (`constructOdooDomain`, `OdooDomain`, `OdooFieldType`, `OdooFieldDefinition`).

## Coding style

### Imports

`@/*` resolves to `src/renderer/src/*` (renderer only — see `tsconfig.web.json` and `electron.vite.config.ts`). Prefer it over relative imports for anything crossing a directory boundary.

### Vim ex commands in CodeMirror

`Vim.defineEx` registers **globally**, across every mounted codemirror-vim instance — it is not per editor. So two editors cannot each define the same command in an effect: whichever mounted last silently answers it for both. `DomainEditor` did exactly that with `:w`, and because the case list is a permanently mounted tab, it won — `:w` in a Python editor applied the domain filter instead of saving.

Either read and write through the `cm` argument the handler is given (what `:f`/format does in `PythonEditor`), or register per editor through `lib/vimWrite.ts`, which owns the single `:w` definition and dispatches via a `WeakMap` keyed by `EditorView` so the focused editor's handler runs. New shared commands should follow one of those two shapes.

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
