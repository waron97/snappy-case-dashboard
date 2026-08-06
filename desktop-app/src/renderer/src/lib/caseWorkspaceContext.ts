import { createContext } from 'react'
import { matchPath } from 'react-router-dom'

// Historical name: this module started out owning only the case tabs, but every
// page in the app except /settings is now a tab, so the union and route table
// below are the single definition of what the app can display.

export type CaseWorkspaceTab =
  | { kind: 'list' }
  | { kind: 'case'; id: number; label: string; renamed?: boolean }
  | { kind: 'field-config'; model: string; recordId: number; label: string; renamed?: boolean }
  | { kind: 'symphony-list'; label: string; renamed?: boolean }
  | {
      kind: 'symphony-request'
      requestId: string
      // Carried in the tab (and the URL) rather than looked up, so a restored
      // tab needs no async repair before it can fetch. '-' means "unknown" —
      // the detail page then resolves it with an exact requestId lookup.
      processId: string
      label: string
      renamed?: boolean
    }
  | { kind: 'symphony-deep-search'; jobId: string; label: string; renamed?: boolean }
  // `instance` is what makes these two multi-instance: it is part of both the
  // key and the URL, so every RIP logs / MFA list tab keeps its own filters and
  // stays individually addressable. The other kinds are keyed by the record they
  // show (or are singletons), so they de-duplicate naturally.
  | { kind: 'rip-logs'; instance: string; label: string; renamed?: boolean }
  | { kind: 'rip-mfa-list'; instance: string; label: string; renamed?: boolean }
  | { kind: 'rip-mfa'; id: number; label: string; renamed?: boolean }
  | { kind: 'symple-workflow'; id: number; label: string; renamed?: boolean }
  | { kind: 'devops-work-items'; label: string; renamed?: boolean }

/** Every tab except the permanent list tab. */
export type OpenWorkspaceTab = Exclude<CaseWorkspaceTab, { kind: 'list' }>

// Distributing over the union (rather than a bare Omit) keeps each `kind`
// literal, so TabIdentity stays a discriminated union and every exhaustive
// switch below keeps its `never` guard.
type DistributiveOmit<T, K extends PropertyKey> = T extends unknown ? Omit<T, K> : never

/**
 * A tab minus its presentation fields — exactly what a URL can carry. Tabs
 * reconstructed from the address bar are TabIdentity, never CaseWorkspaceTab,
 * because a URL cannot know the user's label and must never overwrite one.
 */
export type TabIdentity = DistributiveOmit<CaseWorkspaceTab, 'label' | 'renamed'>

// The helpers below switch exhaustively on purpose. With an if-chain ending in a
// bare return, adding a variant to CaseWorkspaceTab silently produced a
// `field-config:undefined:undefined` key instead of a compile error. The `never`
// assignment makes every new variant a type error here and at each call site
// that has to handle it.
export function unknownTab(tab: never): never {
  throw new Error(`Unknown workspace tab kind: ${JSON.stringify(tab)}`)
}

export function tabKey(tab: TabIdentity): string {
  switch (tab.kind) {
    case 'list':
      return 'list'
    case 'case':
      return `case:${tab.id}`
    case 'field-config':
      return `field-config:${tab.model}:${tab.recordId}`
    case 'symphony-list':
      return 'symphony-list'
    case 'symphony-request':
      // Deliberately ignores processId, so the placeholder ('-') tab and the
      // resolved one are the same tab.
      return `symphony-request:${tab.requestId}`
    case 'symphony-deep-search':
      return `symphony-deep-search:${tab.jobId}`
    case 'rip-logs':
      return `rip-logs:${tab.instance}`
    case 'rip-mfa-list':
      return `rip-mfa-list:${tab.instance}`
    case 'rip-mfa':
      return `rip-mfa:${tab.id}`
    case 'symple-workflow':
      return `symple-workflow:${tab.id}`
    case 'devops-work-items':
      return 'devops-work-items'
    default:
      return unknownTab(tab)
  }
}

/**
 * The canonical URL for a tab. Not a strict inverse of tabFromPath — labels
 * aren't in the URL and an empty processId canonicalises to NO_PROCESS_ID — but
 * its output must be a *fixpoint*: tabPath(tabFromPath(tabPath(t))) === tabPath(t)
 * for every kind. That is what keeps the address bar and the tab strip in
 * agreement. Nothing enforces it (there is no test runner in this repo), so
 * check it by hand when adding a kind.
 *
 * Note the asymmetry in encoding: Symphony ids are opaque and get
 * encodeURIComponent, while `model` (an Odoo model name like `helpdesk.ticket`)
 * and the numeric ids are interpolated raw.
 */
export function tabPath(tab: TabIdentity): string {
  switch (tab.kind) {
    case 'list':
      return '/'
    case 'case':
      return `/helpdesk.ticket/${tab.id}`
    case 'field-config':
      return `/full-field-config/${tab.model}/${tab.recordId}`
    case 'symphony-list':
      return '/symphony/requests'
    case 'symphony-request':
      return `/symphony/request/${encodeURIComponent(tab.requestId)}/${encodeURIComponent(tab.processId || NO_PROCESS_ID)}`
    case 'symphony-deep-search':
      return `/symphony/deep-search/${encodeURIComponent(tab.jobId)}`
    case 'rip-logs':
      return `/rip/logs/${tab.instance}`
    case 'rip-mfa-list':
      return `/rip/mfa/list/${tab.instance}`
    case 'rip-mfa':
      return `/rip/mfa/${tab.id}`
    case 'symple-workflow':
      return `/symple.workflow/${tab.id}`
    case 'devops-work-items':
      return '/devops/work-items'
    default:
      return unknownTab(tab)
  }
}

/** The label a tab gets when nothing better is known yet. Pages that can resolve
 *  a real name report it later via onNameResolved -> setLabel. */
export function defaultLabel(tab: TabIdentity): string {
  switch (tab.kind) {
    case 'list':
      return 'Cases'
    case 'case':
      return `Case #${tab.id}`
    case 'field-config':
      return `${tab.model} #${tab.recordId}`
    case 'symphony-list':
      return 'Symphony'
    case 'symphony-request':
      return `Req ${tab.requestId.slice(0, 10)}`
    case 'symphony-deep-search':
      return 'Deep search'
    case 'rip-logs':
      return 'RIP logs'
    case 'rip-mfa-list':
      return 'MFA'
    case 'rip-mfa':
      return `MFA #${tab.id}`
    case 'symple-workflow':
      return `Workflow #${tab.id}`
    case 'devops-work-items':
      return 'Work items'
    default:
      return unknownTab(tab)
  }
}

type TabRoute = {
  pattern: string
  toTab: (params: Readonly<Record<string, string | undefined>>) => TabIdentity | null
}

function intParam(value: string | undefined): number | null {
  if (!value) return null
  const parsed = Number.parseInt(value, 10)
  return Number.isInteger(parsed) ? parsed : null
}

/** decodeURIComponent throws URIError on a malformed escape (e.g. a hand-typed
 *  '%zz'), which would otherwise take down the whole URL -> tab effect. */
function decodeParam(value: string | undefined): string | null {
  if (!value) return null
  try {
    return decodeURIComponent(value)
  } catch {
    return null
  }
}

/**
 * The one place URLs are mapped to tabs. Keyed by kind rather than an ordered
 * array so that a new union member without a route is a compile error.
 *
 * Two invariants hold this together:
 *
 * 1. Every pattern is matched with `end: true`, which makes them mutually
 *    exclusive and therefore makes iteration order irrelevant — `/rip/mfa/:id`
 *    (2 segments) cannot swallow `/rip/mfa/list/:instance` (3), and
 *    `/symphony/requests` cannot swallow `/symphony/request/x/y`. Anyone who
 *    sets `end: false` or appends `/*` makes ordering load-bearing.
 * 2. `toTab` returns null for anything it can't parse, so a junk URL produces no
 *    tab at all instead of one keyed `case:NaN`.
 *
 * The decodeParam calls are required, not redundant: useMatch decodes the
 * pathname before matching, bare matchPath does not (it only un-escapes %2F).
 */
const TAB_ROUTES: Record<TabIdentity['kind'], TabRoute> = {
  list: {
    pattern: '/',
    toTab: () => LIST_TAB
  },
  case: {
    pattern: '/helpdesk.ticket/:id',
    toTab: (p) => {
      const id = intParam(p.id)
      return id === null ? null : { kind: 'case', id }
    }
  },
  'field-config': {
    pattern: '/full-field-config/:model/:record',
    toTab: (p) => {
      const recordId = intParam(p.record)
      return p.model && recordId !== null
        ? { kind: 'field-config', model: p.model, recordId }
        : null
    }
  },
  'symphony-list': {
    pattern: '/symphony/requests',
    toTab: () => ({ kind: 'symphony-list' })
  },
  'symphony-request': {
    pattern: '/symphony/request/:requestId/:processId',
    toTab: (p) => {
      const requestId = decodeParam(p.requestId)
      const processId = decodeParam(p.processId)
      return requestId && processId ? { kind: 'symphony-request', requestId, processId } : null
    }
  },
  'symphony-deep-search': {
    pattern: '/symphony/deep-search/:jobId',
    toTab: (p) => {
      const jobId = decodeParam(p.jobId)
      return jobId ? { kind: 'symphony-deep-search', jobId } : null
    }
  },
  'rip-logs': {
    pattern: '/rip/logs/:instance',
    toTab: (p) => (p.instance ? { kind: 'rip-logs', instance: p.instance } : null)
  },
  'rip-mfa-list': {
    pattern: '/rip/mfa/list/:instance',
    toTab: (p) => (p.instance ? { kind: 'rip-mfa-list', instance: p.instance } : null)
  },
  'rip-mfa': {
    pattern: '/rip/mfa/:id',
    toTab: (p) => {
      const id = intParam(p.id)
      return id === null ? null : { kind: 'rip-mfa', id }
    }
  },
  'symple-workflow': {
    pattern: '/symple.workflow/:id',
    toTab: (p) => {
      const id = intParam(p.id)
      return id === null ? null : { kind: 'symple-workflow', id }
    }
  },
  'devops-work-items': {
    pattern: '/devops/work-items',
    toTab: () => ({ kind: 'devops-work-items' })
  }
}

/** Must stay pure: it is called from an effect that React may invoke twice under
 *  StrictMode, so it can never mint an id or read a clock. */
export function tabFromPath(pathname: string): TabIdentity | null {
  for (const route of Object.values(TAB_ROUTES)) {
    const match = matchPath({ path: route.pattern, end: true }, pathname)
    if (!match) continue
    const tab = route.toTab(match.params)
    // A pattern can match while its params don't parse (`/rip/mfa/list` matches
    // `/rip/mfa/:id`), so keep looking rather than bailing out.
    if (tab) return tab
  }
  return null
}

/** Paths that render outside the tab workspace. They must not be redirected away
 *  by the URL -> tab effect, and tab shortcuts must not fire on them. */
export const NON_TAB_PATHS: readonly string[] = ['/settings']

export function isNonTabPath(pathname: string): boolean {
  return NON_TAB_PATHS.includes(pathname)
}

/**
 * Mints the next instance of a multi-instance kind, plus its numbered label, so
 * the URL and the label agree (`/rip/logs/2` <-> "RIP logs 2"). This is the
 * impure counterpart to tabFromPath and belongs in an event handler only.
 */
export function newInstance(
  kind: 'rip-logs' | 'rip-mfa-list',
  tabs: readonly CaseWorkspaceTab[]
): [TabIdentity, string] {
  const used = tabs.flatMap((t) =>
    (t.kind === 'rip-logs' || t.kind === 'rip-mfa-list') && t.kind === kind
      ? [Number.parseInt(t.instance, 10)]
      : []
  )
  const numbers = used.filter((n) => Number.isInteger(n))
  const next = numbers.length ? Math.max(...numbers) + 1 : 1
  const tab: TabIdentity = { kind, instance: String(next) }
  return [tab, next > 1 ? `${defaultLabel(tab)} ${next}` : defaultLabel(tab)]
}

export type CaseTabsContextValue = {
  tabs: CaseWorkspaceTab[]
  activeKey: string
  /** Opens or focuses a tab and moves the URL to match. */
  openTab: (tab: TabIdentity, label?: string) => void
  closeTab: (key: string) => void
  closeAll: () => void
  loadTabs: (tabs: CaseWorkspaceTab[]) => void
  setLabel: (key: string, label: string) => void
  renameTab: (key: string, label: string) => void
}

export const CaseTabsContext = createContext<CaseTabsContextValue | null>(null)

export const LIST_TAB: CaseWorkspaceTab = { kind: 'list' }

/** URL placeholder for a Symphony request whose process-instance id isn't known
 *  yet (execution-tree child links don't carry one). Keeps the route arity
 *  static so tabPath stays the canonical form of the URL. */
export const NO_PROCESS_ID = '-'

// Per-kind field checks for sanitizeTabs. Keyed by kind so a new variant without
// a validator is a compile error: it used to be Record<string, …>, which meant a
// forgotten entry made the tab work perfectly all session and then vanish on
// restart (and from every saved tab set) — the one silent failure in this file.
// Number.isInteger rather than typeof === 'number' because NaN is a number.
const TAB_VALIDATORS: Record<OpenWorkspaceTab['kind'], (t: Record<string, unknown>) => boolean> = {
  case: (t) => Number.isInteger(t.id),
  'field-config': (t) => typeof t.model === 'string' && Number.isInteger(t.recordId),
  'symphony-list': () => true,
  'symphony-request': (t) => typeof t.requestId === 'string' && typeof t.processId === 'string',
  'symphony-deep-search': (t) => typeof t.jobId === 'string',
  'rip-logs': (t) => typeof t.instance === 'string',
  'rip-mfa-list': (t) => typeof t.instance === 'string',
  'rip-mfa': (t) => Number.isInteger(t.id),
  'symple-workflow': (t) => Number.isInteger(t.id),
  'devops-work-items': () => true
}

/**
 * Validates untrusted tab arrays — both the persisted open-tabs uiPref and
 * saved tab sets, which arrive from disk as `unknown[]`. The list tab is never
 * included; callers prepend LIST_TAB themselves.
 *
 * Anything not listed in TAB_VALIDATORS — or failing its check, or missing a
 * string `label` — is dropped. That keeps version skew from *crashing*: an older
 * build can load a set written by a newer one. It does not keep it from losing
 * data, though: the caller then persists the sanitized array, so the dropped
 * tabs are gone for good. Same for a saved set that is loaded and then updated.
 */
export function sanitizeTabs(input: unknown): OpenWorkspaceTab[] {
  if (!Array.isArray(input)) {
    return []
  }
  return input
    .filter((t): t is OpenWorkspaceTab => {
      if (!t || typeof t !== 'object') return false
      const candidate = t as Record<string, unknown>
      if (typeof candidate.label !== 'string') return false
      const validate = TAB_VALIDATORS[candidate.kind as OpenWorkspaceTab['kind']]
      return validate ? validate(candidate) : false
    })
    .map((t) => ({ ...t, renamed: t.renamed === true }))
}
