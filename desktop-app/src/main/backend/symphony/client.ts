// HTTP client for the Bit2win Symphony web app.
//
// Deliberately NOT reusing odoo.ts's callBit2win: that helper hardcodes an
// `output: all` header, always parses the response as JSON, and rejects any
// status other than 200. All three are wrong here — the execution-tree detail
// endpoint returns text/html, and the verified Symphony calls do not send
// `output: all`. Threading a parse mode through callBit2win would make its
// already-`any` return type ambiguous for its existing caller, so the ~25 lines
// of fetch + 401-retry are duplicated instead.
//
// Auth is the same Keycloak service-account bearer used everywhere else. The
// browser talks to these endpoints with a session cookie, but they accept
// Bearer too (verified live against every endpoint used here).

import { getSettings } from '../settings'
import { ConnectError, getCachedToken, invalidateToken } from '../keycloak'
import { AuthError } from '../odoo'
import type {
  SymphonyActivitiesPage,
  SymphonyExecutionNodeQuery,
  SymphonyRequestDetailOptions,
  SymphonyRequestRow,
  SymphonyRequestTreePage,
  SymphonyRequestTreeQuery,
  SymphonyVariablesPage
} from './types'
import { SYMPHONY_STATUSES } from './types'
import { recordObservedProcessKeys } from './catalog'

/** No default timeout exists on Node's fetch; one hung socket would otherwise
 *  stall a deep-search worker for the rest of a multi-hour sweep. */
const DEFAULT_TIMEOUT_MS = 120_000

/**
 * Symphony lives on the same host as Bit2win, so `symphonyUrl` is optional and
 * only needed if the two ever diverge. Note that profiles saved before this
 * field existed have it `undefined` at runtime despite the non-optional type —
 * settings.ts's migrate() only backfills legacy flat stores — hence the falsy
 * check rather than a store migration.
 */
export function symphonyBaseUrl(): string {
  const { symphonyUrl, b2wUrl } = getSettings()
  if (symphonyUrl) {
    return symphonyUrl.replace(/\/+$/, '')
  }
  if (b2wUrl) {
    return new URL(b2wUrl).origin
  }
  throw new Error('Symphony URL is not configured. Set the Bit2win URL in Settings.')
}

async function symphonyFetch<T>(
  path: string,
  params: URLSearchParams | undefined,
  parse: 'json' | 'text',
  signal?: AbortSignal,
  timeoutMs: number = DEFAULT_TIMEOUT_MS
): Promise<T> {
  const op = async (token: string): Promise<T> => {
    const query = params ? `?${params.toString()}` : ''
    const url = `${symphonyBaseUrl()}${path}${query}`

    const response = await fetch(url, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
        accept: parse === 'json' ? 'application/json' : '*/*'
      },
      signal: signal
        ? AbortSignal.any([signal, AbortSignal.timeout(timeoutMs)])
        : AbortSignal.timeout(timeoutMs)
    })

    if (response.status === 401) {
      throw new AuthError()
    }
    if (response.status !== 200) {
      throw new ConnectError(response, await response.text())
    }

    return (parse === 'json' ? await response.json() : await response.text()) as T
  }

  const token = await getCachedToken()
  try {
    return await op(token)
  } catch (err) {
    if (err instanceof AuthError) {
      invalidateToken()
      return op(await getCachedToken())
    }
    throw err
  }
}

/** The raw wire shape — `dataList` is JSON nested inside JSON. */
type RawRequestTreeResponse = {
  pageSize: number
  maximumRecordsNumber: number
  moreRecords: boolean
  tableLimit: boolean
  dataList: string | SymphonyRequestRow[] | null
}

export async function getRequestTree(
  query: SymphonyRequestTreeQuery,
  signal?: AbortSignal
): Promise<SymphonyRequestTreePage> {
  const params = new URLSearchParams({ params: JSON.stringify(query) })
  const raw = await symphonyFetch<RawRequestTreeResponse>(
    '/symphony/restInfo/ajax/getRequestTree',
    params,
    'json',
    signal
  )

  let rows: SymphonyRequestRow[] = []
  if (typeof raw.dataList === 'string') {
    rows = JSON.parse(raw.dataList) as SymphonyRequestRow[]
  } else if (Array.isArray(raw.dataList)) {
    rows = raw.dataList
  }

  // Learn the process keys that actually occur, since the definition catalogs
  // don't cover all of them. Deliberately fire-and-forget: a bookkeeping failure
  // must never break the list.
  try {
    recordObservedProcessKeys(rows.map((r) => r.processKey))
  } catch (err) {
    console.warn('[symphony] could not record observed process keys:', err)
  }

  return {
    pageSize: raw.pageSize,
    maximumRecordsNumber: raw.maximumRecordsNumber,
    moreRecords: raw.moreRecords,
    tableLimit: raw.tableLimit,
    rows
  }
}

export async function getHistoricVariables(
  processInstanceId: string,
  page: number = 1,
  size: number = 1000,
  signal?: AbortSignal
): Promise<SymphonyVariablesPage> {
  const params = new URLSearchParams({
    processInstanceId,
    page: String(page),
    size: String(size)
  })
  return symphonyFetch<SymphonyVariablesPage>(
    '/symphony/restInfo/ajax/historic_variable',
    params,
    'json',
    signal
  )
}

export async function getHistoricActivities(
  processInstanceId: string,
  page: number = 1,
  size: number = 1000,
  signal?: AbortSignal
): Promise<SymphonyActivitiesPage> {
  const params = new URLSearchParams({
    processInstanceId,
    page: String(page),
    size: String(size),
    sort: 'startTime',
    direction: 'desc'
  })
  return symphonyFetch<SymphonyActivitiesPage>(
    '/symphony/restInfo/ajax/historic_activity',
    params,
    'json',
    signal
  )
}

/**
 * Returns an HTML fragment, not JSON. `onlyContent: true` gives just the
 * right-hand detail pane (~10KB); false additionally embeds the execution tree
 * (~34KB). Parsed in the renderer with DOMParser — see lib/symphonyDetailHtml.
 *
 * The repeated `status=` params are built here rather than in the renderer
 * because URLSearchParams doesn't survive contextBridge.
 */
export async function getRequestDetailHtml(
  requestId: string,
  parentId: string | null,
  opts: SymphonyRequestDetailOptions = {},
  signal?: AbortSignal
): Promise<string> {
  const { onlyContent = false, statuses = SYMPHONY_STATUSES, deadJob = true } = opts

  const params = new URLSearchParams()
  params.set('onlyContent', String(onlyContent))
  statuses.forEach((status) => params.append('status', status))
  params.set('deadJob', String(deadJob))

  const parent = parentId ? encodeURIComponent(parentId) : 'null'
  const path = `/symphony/execution-tree/detail/${encodeURIComponent(requestId)}/${parent}`

  return symphonyFetch<string>(path, params, 'text', signal)
}

/**
 * Expands one execution-tree node's children — the call the legacy UI makes
 * when a `has-children` node is toggled. Returns an HTML fragment (that one
 * node, re-rendered with its `.children-container` now populated one level
 * deep), parsed the same way as `getRequestDetailHtml` in
 * lib/symphonyDetailHtml.ts.
 *
 * `processKey`/`rootId` must be the TREE ROOT's, not the expanding node's own
 * — verified live against a nested subprocess node.
 */
export async function getExecutionTreeNode(
  nodeId: string,
  query: SymphonyExecutionNodeQuery,
  signal?: AbortSignal
): Promise<string> {
  const params = new URLSearchParams()
  params.set('processKey', query.processKey)
  params.set('rootId', query.rootId)
  params.set('viewType', query.viewType ?? 'PROCESS')
  params.set('deadJob', String(query.deadJob ?? false))
  if (query.idSelected) {
    params.set('idSelected', query.idSelected)
  }

  const path = `/symphony/execution-tree/node/${encodeURIComponent(nodeId)}`
  return symphonyFetch<string>(path, params, 'text', signal)
}

/** Used by catalog.ts, which needs the same auth/retry/timeout behaviour. */
export { symphonyFetch }
