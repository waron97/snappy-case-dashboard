// Shared Symphony types. The renderer imports these type-only across the
// main/renderer boundary (see lib/symphony-api.ts), the same way odoo-api.ts
// re-exports OneToMany/OdooDomain/Asset from backend/odoo.

export type SymphonyRequestStatus = 'CANCELLED' | 'NEW' | 'COMPLETED' | 'WORKING' | 'FAILED'

export const SYMPHONY_STATUSES: SymphonyRequestStatus[] = [
  'CANCELLED',
  'NEW',
  'COMPLETED',
  'WORKING',
  'FAILED'
]

export type SymphonySorter = { dir: 'asc' | 'desc'; field: string }

/**
 * Query for the request-list endpoint. Serialized whole into the `params` query
 * arg as JSON.
 *
 * Date strings are `dd/MM/yyyy HH:mm` (minute granularity — the server has no
 * seconds in this param even though it returns millisecond timestamps).
 *
 * `recordsLoaded` is an OFFSET, not a page number.
 *
 * There is deliberately no `parentId` field: the server accepts it and then
 * silently ignores it, returning an unrelated page of rows. Child requests are
 * only reachable through the execution-tree HTML endpoint.
 */
export type SymphonyRequestTreeQuery = {
  name?: string
  startTimeInitStr?: string
  startTimeEndStr?: string
  processId?: string
  requestId?: string
  referenceId?: string
  externalKey?: string
  pageSize?: string
  recordsLoaded?: number
  listStatusSelected?: SymphonyRequestStatus[]
  deadJob?: boolean
  sorters?: SymphonySorter[]
}

export type SymphonyIconConfig = {
  status: string
  iconType: string
  iconColor: string
  iconTitle: string
}

export type SymphonyRequestRow = {
  requestId: string
  tenantId: string
  status: string
  iconConfig: SymphonyIconConfig | null
  processKey: string
  /** The process-instance id — feeds the variables and activities endpoints. */
  processId: string
  /** `dd/MM/yyyy HH:mm:ss.SSS` */
  createdDate: string
  type: string
  completed: boolean
  lastModifiedDate: string
  deadJob: boolean
  hasChilds: boolean
  hasBCRChilds: boolean
  parentId: string | null
  childs: number
  fileFk: string | null
}

export type SymphonyRequestTreePage = {
  pageSize: number
  /** Server-side enumeration cap — 10000 in practice. */
  maximumRecordsNumber: number
  moreRecords: boolean
  /** True when the server refused to enumerate further because of the cap. */
  tableLimit: boolean
  rows: SymphonyRequestRow[]
}

/**
 * Observed `varType` values: stringCipher, longStringCipher, boolean, integer,
 * long, double. Typed as string because a 172-row sample is not exhaustive.
 *
 * `tooLarge` and `downloadUrl` are unreliable and must not be used: a full
 * sample reported tooLarge:"True" on every row *except* the one 1.4MB value,
 * and the download URL 404s. `varValue` always holds the complete value.
 * `varMin` is a ~103-char preview.
 */
export type SymphonyVariable = {
  varName: string
  varType: string
  varValue: string
  size: string
  tooLarge: string
  downloadUrl: string
  varMin: string
  /** `dd/MM/yyyy HH:mm:ss.SSS` */
  varDate: string
  varProcId: string
}

export type SymphonyVariablesPage = {
  last_page: number
  data: SymphonyVariable[]
}

export type SymphonyActivity = {
  activityId: string
  activityName: string
  activityType: string
  startTime: string
  endTime: string
  durationInMillis: string
  processInstanceId: string
  tenantId: string
  deleteReason: string | null
}

export type SymphonyActivitiesPage = {
  last_page: number
  data: SymphonyActivity[]
}

export type SymphonyRequestDetailOptions = {
  onlyContent?: boolean
  statuses?: SymphonyRequestStatus[]
  deadJob?: boolean
}

// ---- Process-key catalog ----

export type SymphonyProcessKeySource = 'bpmn' | 'process-builder'

export type SymphonyProcessKey = {
  /**
   * The key as it appears on requests, i.e. what getRequestTree's `name` param
   * matches — the deployment prefix already stripped. VERIFIED: a request shows
   * `async_case_engine` while the BPMN definition is `B2WA_async_case_engine`,
   * and filtering by the prefixed form returns zero rows.
   */
  name: string
  /** The undecorated definition name, for display when it differs from `name`. */
  definitionName: string
  source: SymphonyProcessKeySource
  version: number
  status: string
  tenantId: string
  description: string | null
  /** `yyyy-MM-dd HH:mm:ss` — a different format from the request endpoints. */
  lastModifiedDate: string
}

export type SymphonyProcessKeyCatalog = {
  /**
   * Bumped whenever what we store changes shape or gains a source. Without it a
   * catalog cached by an older build is served as "fresh" for the whole TTL, so
   * an upgrade that adds keys appears to do nothing — which is exactly what
   * happened when the process-builder source was added.
   */
  schemaVersion?: number
  profileId: string
  keys: SymphonyProcessKey[]
  /** ISO timestamp of the last successful sweep. */
  fetchedAt: string
  totalPages: number
  /** False when a page failed mid-sweep, so the list may be short. */
  complete: boolean
}
