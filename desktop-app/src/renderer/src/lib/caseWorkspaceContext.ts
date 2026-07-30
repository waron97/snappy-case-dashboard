import { createContext } from 'react'

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

/** Every tab except the permanent list tab. */
export type OpenWorkspaceTab = Exclude<CaseWorkspaceTab, { kind: 'list' }>

// Both helpers switch exhaustively on purpose. With an if-chain ending in a
// bare return, adding a variant to CaseWorkspaceTab silently produced a
// `field-config:undefined:undefined` key instead of a compile error. The `never`
// assignment makes every new variant a type error here and at each call site
// that has to handle it.
function unknownTab(tab: never): never {
  throw new Error(`Unknown workspace tab kind: ${JSON.stringify(tab)}`)
}

export function tabKey(tab: CaseWorkspaceTab): string {
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
      return `symphony-request:${tab.requestId}`
    case 'symphony-deep-search':
      return `symphony-deep-search:${tab.jobId}`
    default:
      return unknownTab(tab)
  }
}

export function tabPath(tab: CaseWorkspaceTab): string {
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
    default:
      return unknownTab(tab)
  }
}

export type CaseTabsContextValue = {
  tabs: CaseWorkspaceTab[]
  activeKey: string
  openCase: (id: number) => void
  openFieldConfig: (model: string, recordId: number) => void
  openSymphonyList: () => void
  openSymphonyRequest: (requestId: string, processId: string, label?: string) => void
  openDeepSearch: (jobId: string, label?: string) => void
  closeTab: (key: string) => void
  closeAll: () => void
  loadTabs: (tabs: CaseWorkspaceTab[]) => void
  setActive: (key: string) => void
  setLabel: (key: string, label: string) => void
  renameTab: (key: string, label: string) => void
}

export const CaseTabsContext = createContext<CaseTabsContextValue | null>(null)

export const LIST_TAB: CaseWorkspaceTab = { kind: 'list' }

/** URL placeholder for a Symphony request whose process-instance id isn't known
 *  yet (execution-tree child links don't carry one). Keeps the route arity
 *  static so tabPath stays a lossless inverse of the URL. */
export const NO_PROCESS_ID = '-'

// Per-kind field checks for sanitizeTabs. Anything not listed here — or failing
// its check — is dropped. That silent drop is deliberate: it's what makes
// version skew safe in both directions (an older build loading a tab set saved
// by a newer one, and vice versa).
const TAB_VALIDATORS: Record<string, (t: Record<string, unknown>) => boolean> = {
  case: (t) => typeof t.id === 'number',
  'field-config': (t) => typeof t.model === 'string' && typeof t.recordId === 'number',
  'symphony-list': () => true,
  'symphony-request': (t) => typeof t.requestId === 'string' && typeof t.processId === 'string',
  'symphony-deep-search': (t) => typeof t.jobId === 'string'
}

/**
 * Validates untrusted tab arrays — both the persisted open-tabs uiPref and
 * saved tab sets, which arrive from disk as `unknown[]`. The list tab is never
 * included; callers prepend LIST_TAB themselves.
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
      const validate = TAB_VALIDATORS[candidate.kind as string]
      return validate ? validate(candidate) : false
    })
    .map((t) => ({ ...t, renamed: t.renamed === true }))
}
