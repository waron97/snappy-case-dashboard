// Process-key (BPMN definition) catalog cache.
//
// The list endpoint has no field projection and returns a base64 `bpmnFileSvg`
// per row, which is ~99% of the payload: enumerating all ~361 definitions costs
// ~58MB and 15-20s, and the server does not gzip. So the catalog is fetched in
// the background, stripped down to the handful of fields the UI needs (~80KB),
// and persisted so the filter dropdown is instant on subsequent launches.
//
// Stored as PLAIN JSON, unlike the four safeStorage-encrypted stores in this
// directory: this is public deployment metadata (process names and versions),
// and encrypting it only makes it undebuggable. Deliberate, not an oversight.

import { app } from 'electron'
import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'
import { getStore } from '../settings'
import { symphonyFetch } from './client'
import type { SymphonyProcessKey, SymphonyProcessKeyCatalog } from './types'

const CONNECTOR = 'SymphBpmnFileTabCon'
/** Process-builder wizards, which spawn processes this page also lists. */
const PB_PATH = '/api/processbuilder/v1/builder/process'
/**
 * Deployment prefixes the Symphony runtime strips from a BPMN definition name
 * when stamping a request's processKey. Verified against live data: definition
 * `B2WA_async_case_engine` produces requests keyed `async_case_engine`, and the
 * request-list `name` filter only matches the stripped form.
 */
const DEPLOY_PREFIXES = ['B2WA_', 'B2W_']

function stripDeployPrefix(name: string): string {
  for (const prefix of DEPLOY_PREFIXES) {
    if (name.startsWith(prefix)) {
      return name.slice(prefix.length)
    }
  }
  return name
}
/** Small enough that one page is a ~15MB buffer rather than one 58MB buffer. */
const PAGE_SIZE = 100
const MAX_PAGES = 40
/** Filtered typeahead queries; a `like` match at PAGE_SIZE could still be ~15MB. */
const SEARCH_PAGE_SIZE = 20
/** Bump on any change to which sources feed the catalog or how keys are stored.
 *  v2 = deployment prefix stripped + process-builder source added. */
const SCHEMA_VERSION = 2
const TTL_MS = 12 * 60 * 60 * 1000
/** Don't re-hammer a broken environment on every component mount. */
const MIN_RETRY_MS = 10 * 60 * 1000

type Store = {
  catalogs: SymphonyProcessKeyCatalog[]
  /** Keys seen on actual requests, per profile. See recordObservedProcessKeys. */
  observed?: Record<string, string[]>
}

/** The wire row. Everything not in SymphonyProcessKey is dropped on ingest. */
type RawBpmnFile = {
  id: string
  name: string
  tenantId: string
  status: string
  version: number
  description: string | null
  lastModifiedDate: string
  bpmnFileSvg?: string
}

type TabulatorPage = { last_page: number; data: RawBpmnFile[] }

function catalogPath(): string {
  return join(app.getPath('userData'), 'symphony-process-keys.json')
}

let cache: Store | null = null

function load(): Store {
  if (cache) {
    return cache
  }
  const path = catalogPath()
  if (!existsSync(path)) {
    cache = { catalogs: [] }
    return cache
  }
  try {
    cache = JSON.parse(readFileSync(path, 'utf-8')) as Store
  } catch {
    // A corrupt cache is not worth failing over — it's re-derivable.
    cache = { catalogs: [] }
  }
  return cache
}

function persist(store: Store): void {
  cache = store
  writeFileSync(catalogPath(), JSON.stringify(store), 'utf-8')
}

function activeProfileId(): string | null {
  return getStore().activeProfileId
}

/**
 * `othersort` is mandatory — omitting it makes the server return HTTP 500.
 * `card` is left off (defaults to false): with card=true rows come back packed
 * four-per-row into cellContent1..4.
 */
function tabulatorParams(page: number, size: number, nameLike: string | null): URLSearchParams {
  return new URLSearchParams({
    params: JSON.stringify({ page, size, sorters: [], filters: [] }),
    connector: CONNECTOR,
    otherfilters: JSON.stringify([
      { field: 'id', type: '=', value: null },
      { field: 'name', type: 'like', value: nameLike },
      { field: 'tenantId', type: '=', value: null },
      { field: 'latestVersion', type: '=', value: true }
    ]),
    othersort: JSON.stringify({ field: 'name', dir: 'asc' })
  })
}

/** Strips the bulk fields immediately so a page's SVGs become garbage at once. */
function toProcessKey(raw: RawBpmnFile): SymphonyProcessKey {
  return {
    name: stripDeployPrefix(raw.name),
    definitionName: raw.name,
    source: 'bpmn',
    version: raw.version,
    status: raw.status,
    tenantId: raw.tenantId,
    description: raw.description ?? null,
    lastModifiedDate: raw.lastModifiedDate
  }
}

/**
 * One process-builder wizard. `document_id` is the process key its runs carry;
 * `process_name` is a human label ("Ammissibilità") and is NOT a key — verified
 * zero overlap with request keys, so it is only used as a description.
 */
type RawProcessBuilder = {
  guid?: string
  document_id?: string
  process_name?: string
  status?: string
  version?: number
  updated_date?: string
  /** Multi-megabyte; dropped on ingest. */
  pages?: unknown
  process_structure?: unknown
  built_page?: unknown
}

function toProcessBuilderKey(raw: RawProcessBuilder): SymphonyProcessKey | null {
  const documentId = raw.document_id
  if (!documentId) {
    return null
  }
  return {
    name: stripDeployPrefix(documentId),
    definitionName: documentId,
    source: 'process-builder',
    version: raw.version ?? 0,
    status: raw.status ?? '',
    tenantId: '',
    description: raw.process_name ?? null,
    lastModifiedDate: (raw.updated_date ?? '').replace('T', ' ').slice(0, 19)
  }
}

/**
 * Process builders are a second source of process keys.
 *
 * The BPMN catalog alone covered only ~48 of 54 keys observed on real requests;
 * builder-spawned processes are not deployed BPMN files, so they never appear
 * there. This endpoint lives on a different base path (`/api/processbuilder/v1`)
 * but takes the same bearer token. It returns ~26MB because every row embeds its
 * pages and structure, so — as with the BPMN SVGs — rows are stripped on ingest.
 *
 * Failure here is non-fatal: the BPMN half of the catalog is still worth having.
 */
async function fetchProcessBuilders(): Promise<SymphonyProcessKey[]> {
  try {
    const raw = await symphonyFetch<RawProcessBuilder[] | { data?: RawProcessBuilder[] }>(
      PB_PATH,
      undefined,
      'json'
    )
    const rows = Array.isArray(raw) ? raw : (raw?.data ?? [])
    return rows.map(toProcessBuilderKey).filter((k): k is SymphonyProcessKey => k != null)
  } catch (err) {
    console.warn('[symphony] process-builder catalog unavailable:', err)
    return []
  }
}

/**
 * One entry per request-facing key. Prefers a deployed BPMN definition over a
 * process-builder row with the same key (the BPMN row carries a real version and
 * tenant), then the higher version.
 */
function dedupeByName(keys: SymphonyProcessKey[]): SymphonyProcessKey[] {
  const byName = new Map<string, SymphonyProcessKey>()
  for (const key of keys) {
    const existing = byName.get(key.name)
    if (!existing) {
      byName.set(key.name, key)
      continue
    }
    const beatsOnSource = existing.source !== 'bpmn' && key.source === 'bpmn'
    const beatsOnVersion = existing.source === key.source && key.version > existing.version
    if (beatsOnSource || beatsOnVersion) {
      byName.set(key.name, key)
    }
  }
  return [...byName.values()].sort((a, b) => a.name.localeCompare(b.name))
}

/**
 * Process keys harvested from real request rows.
 *
 * The two definition catalogs still are not a superset of what appears on
 * requests: the BPMN half is filtered to `latestVersion=true`, so a request
 * started against an older version carries a key no longer in the catalog.
 * (An earlier note here claimed `ml_voltura_data_input` was in neither source —
 * that was measured against a stale v1 cache. Verified live: it is one of 291
 * builder `document_id`s.) Rather than guess at where the remainder is defined,
 * this records what the request list actually returns — by construction that is
 * exactly the set the `name` filter can match.
 *
 * Called from the request-list fetch in client.ts, so the picker simply learns as
 * you browse. Persisting is coalesced because a paging session calls this often.
 */
let observedFlushTimer: NodeJS.Timeout | null = null

export function recordObservedProcessKeys(keys: (string | null | undefined)[]): void {
  const profileId = activeProfileId()
  if (!profileId) {
    return
  }
  const store = load()
  const observed = (store.observed ??= {})
  const forProfile = new Set(observed[profileId] ?? [])
  const before = forProfile.size
  for (const key of keys) {
    if (key) {
      forProfile.add(key)
    }
  }
  if (forProfile.size === before) {
    return
  }
  observed[profileId] = [...forProfile].sort()

  if (!observedFlushTimer) {
    observedFlushTimer = setTimeout(() => {
      observedFlushTimer = null
      persist(load())
    }, 5000)
  }
}

export function getObservedProcessKeys(profileId: string): string[] {
  return load().observed?.[profileId] ?? []
}

export function getCachedCatalog(profileId: string): SymphonyProcessKeyCatalog | null {
  return load().catalogs.find((c) => c.profileId === profileId) ?? null
}

function hasCurrentSchema(catalog: SymphonyProcessKeyCatalog): boolean {
  return (catalog.schemaVersion ?? 1) === SCHEMA_VERSION
}

/**
 * The cached catalog only if the renderer may actually show it.
 *
 * This is what the IPC layer serves, NOT getCachedCatalog. The renderer hands the
 * persisted copy to react-query as initialData with a 12h staleTime keyed off
 * `fetchedAt`, so a returned catalog is treated as fresh and suppresses the
 * network query entirely — meaning isFresh()'s schema check below never runs and
 * a build that adds a source appears to do nothing for up to 12h. That is exactly
 * how the process-builder source stayed invisible after it shipped.
 *
 * A foreign-schema catalog is therefore withheld rather than served stale: its
 * keys are the pre-strip definition names, which the request-list `name` filter
 * matches zero rows for, so showing them is worse than showing nothing for the
 * ~20s a sweep takes. A current-schema catalog is served however old it is — that
 * is the intended instant-render-then-refetch path.
 */
export function getUsableCachedCatalog(profileId: string): SymphonyProcessKeyCatalog | null {
  const catalog = getCachedCatalog(profileId)
  return catalog && hasCurrentSchema(catalog) ? catalog : null
}

function isFresh(catalog: SymphonyProcessKeyCatalog | null): boolean {
  if (!catalog || !catalog.complete) {
    return false
  }
  // A catalog written by an older build is stale regardless of its age.
  if (!hasCurrentSchema(catalog)) {
    return false
  }
  const age = Date.now() - Date.parse(catalog.fetchedAt)
  return Number.isFinite(age) && age >= 0 && age < TTL_MS
}

async function sweep(profileId: string): Promise<SymphonyProcessKeyCatalog> {
  const keys: SymphonyProcessKey[] = []
  let totalPages = 1
  let complete = true

  for (let page = 1; page <= MAX_PAGES; page++) {
    const response = await symphonyFetch<TabulatorPage>(
      '/symphony/restInfo/ajax/tabulator',
      tabulatorParams(page, PAGE_SIZE, null),
      'json'
    )
    totalPages = response.last_page ?? page
    for (const raw of response.data ?? []) {
      if (raw?.name) {
        keys.push(toProcessKey(raw))
      }
    }
    if (page >= totalPages) {
      break
    }
    if (page === MAX_PAGES) {
      complete = false
    }
  }

  // Both sources feed one list; a PB failure must not lose the BPMN half.
  const builderKeys = await fetchProcessBuilders()

  const catalog: SymphonyProcessKeyCatalog = {
    schemaVersion: SCHEMA_VERSION,
    profileId,
    keys: dedupeByName([...keys, ...builderKeys]),
    fetchedAt: new Date().toISOString(),
    totalPages,
    complete
  }

  const store = load()
  // Spread the store: `observed` lives in the same file and a sweep must not drop it.
  persist({
    ...store,
    catalogs: [...store.catalogs.filter((c) => c.profileId !== profileId), catalog]
  })
  return catalog
}

const inFlight = new Map<string, Promise<SymphonyProcessKeyCatalog>>()
const lastFailureAt = new Map<string, number>()

export async function ensureCatalog(
  opts: { force?: boolean } = {}
): Promise<SymphonyProcessKeyCatalog> {
  const profileId = activeProfileId()
  if (!profileId) {
    throw new Error('No active profile — cannot load the Symphony process catalog.')
  }

  const cached = getCachedCatalog(profileId)
  if (!opts.force && isFresh(cached)) {
    return cached as SymphonyProcessKeyCatalog
  }

  const existing = inFlight.get(profileId)
  if (existing) {
    return existing
  }

  if (!opts.force) {
    const failedAt = lastFailureAt.get(profileId)
    if (failedAt && Date.now() - failedAt < MIN_RETRY_MS) {
      if (cached) {
        return cached
      }
      throw new Error('Symphony process catalog is unavailable; retrying later.')
    }
  }

  const promise = sweep(profileId)
    .then((catalog) => {
      lastFailureAt.delete(profileId)
      return catalog
    })
    .catch((err) => {
      lastFailureAt.set(profileId, Date.now())
      throw err
    })
    .finally(() => {
      inFlight.delete(profileId)
    })

  inFlight.set(profileId, promise)
  return promise
}

/**
 * Server-side `like` search — the fallback while the full catalog is cold.
 *
 * Covers BPMN definitions only; process builders have no search endpoint, so a
 * builder-spawned key is suggestable only once the full catalog has loaded.
 * Results are prefix-stripped like the catalog's, so what the user picks is what
 * the request filter matches.
 */
export async function searchProcessKeys(nameLike: string): Promise<SymphonyProcessKey[]> {
  const trimmed = nameLike.trim()
  if (!trimmed) {
    return []
  }
  const response = await symphonyFetch<TabulatorPage>(
    '/symphony/restInfo/ajax/tabulator',
    tabulatorParams(1, SEARCH_PAGE_SIZE, trimmed),
    'json'
  )
  return dedupeByName((response.data ?? []).filter((raw) => raw?.name).map(toProcessKey))
}
