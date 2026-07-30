import type { SymphonyRequestStatus, SymphonyRequestTreeQuery } from '@/lib/symphony-api'
import type { SweepListFilter } from '@/lib/symphonyDeepSearch'
import { fromSymphonyDateParam, toSymphonyDateParam } from '@/lib/symphonyDates'

/**
 * Flat and JSON-serializable on purpose: a deep-search job snapshots this
 * verbatim, and dates stay as the `string | null` Mantine's inputs hold rather
 * than Date objects.
 *
 * The legacy filter bar also has a "Tenant" dropdown and a "Custom Status Name"
 * field. Both are omitted: a profile already is one tenant (every observed row
 * carries the same tenantId), and Custom Status Name has no known request param.
 */
export type SymphonyFilterState = {
  requestId: string
  processId: string
  processKey: string | null
  referenceId: string
  externalKey: string
  startDate: string | null
  endDate: string | null
  statuses: SymphonyRequestStatus[]
  deadJob: boolean
}

export const ALL_STATUSES: SymphonyRequestStatus[] = [
  'CANCELLED',
  'NEW',
  'COMPLETED',
  'WORKING',
  'FAILED'
]

export const EMPTY_SYMPHONY_FILTERS: SymphonyFilterState = {
  requestId: '',
  processId: '',
  processKey: null,
  referenceId: '',
  externalKey: '',
  startDate: null,
  endDate: null,
  // No status pre-selected. Note this does NOT mean an empty list is sent: see
  // resolveStatuses — the API treats an empty listStatusSelected as "match
  // nothing" (verified: 0 rows), so "none ticked" is sent as "all".
  statuses: [],
  // Dead job is a state like any other — the engine failed to execute a state due
  // to malformation, as opposed to a normal business error such as a 400 from an
  // external call. So it starts unticked with the rest, and "nothing ticked"
  // likewise means "no constraint" rather than "exclude dead jobs".
  deadJob: false
}

/**
 * `listStatusSelected` is an ALLOWLIST, not a hint — sending the five statuses we
 * know about silently drops every other one. Verified on a one-minute window:
 * omitting it returned 7 rows including a `RESUBMIT`, while sending
 * CANCELLED/NEW/COMPLETED/WORKING/FAILED returned 6 and dropped that row.
 * Symphony has at least RESUBMIT beyond the five the legacy filter bar exposes.
 *
 * So "nothing ticked" must OMIT the param rather than expand it, which is the
 * only way to say "any status", including ones this app has never heard of.
 */
export function resolveStatuses(
  statuses: SymphonyRequestStatus[]
): SymphonyRequestStatus[] | undefined {
  return statuses.length > 0 ? statuses : undefined
}

/**
 * `deadJob` is never a no-op either: with no statuses selected, `deadJob: true`
 * narrowed a 7-row window to 0 — it constrains rather than includes. So it is
 * only sent when the box is actually ticked.
 */
export function resolveDeadJob(filters: SymphonyFilterState): boolean | undefined {
  return filters.deadJob ? true : undefined
}

const trimmed = (value: string): string | undefined => {
  const next = value.trim()
  return next ? next : undefined
}

/** Filter state -> the `params` payload the request-list endpoint expects. */
export function toRequestTreeQuery(
  filters: SymphonyFilterState,
  pageSize: number,
  recordsLoaded: number
): SymphonyRequestTreeQuery {
  return {
    name: filters.processKey ?? undefined,
    requestId: trimmed(filters.requestId),
    processId: trimmed(filters.processId),
    referenceId: trimmed(filters.referenceId),
    externalKey: trimmed(filters.externalKey),
    startTimeInitStr: toSymphonyDateParam(filters.startDate),
    startTimeEndStr: toSymphonyDateParam(filters.endDate),
    pageSize: String(pageSize),
    recordsLoaded,
    listStatusSelected: resolveStatuses(filters.statuses),
    deadJob: resolveDeadJob(filters),
    sorters: [{ dir: 'desc', field: 'createdDate' }]
  }
}

/**
 * Snapshot for a deep-search job. Dates are converted to the literal API strings
 * here, once, so a job resumed weeks later re-issues byte-identical queries
 * rather than re-deriving a window from a relative value.
 */
export function toSweepListFilter(filters: SymphonyFilterState): SweepListFilter {
  return {
    processKey: filters.processKey,
    startTimeInitStr: toSymphonyDateParam(filters.startDate) ?? null,
    startTimeEndStr: toSymphonyDateParam(filters.endDate) ?? null,
    // Always null — see the note above. The fields stay on the type so job
    // files written before this decision still load.
    requestId: null,
    processId: null,
    referenceId: null,
    externalKey: null,
    statuses: filters.statuses,
    // Stored as ticked, not resolved: the engine omits it when false, exactly as
    // the request list does.
    deadJob: filters.deadJob
  }
}

/**
 * Snapshot for a deep-search job.
 *
 * The single-record identity fields are deliberately dropped: a sweep exists to
 * scan MANY requests, so pinning it to one request id (or one process instance)
 * makes it pointless — if you already have the id you open that request
 * directly. They are also not shown in the sweep's filter editor, and carrying a
 * value the user cannot see would be an invisible constraint that silently
 * explains "why did my sweep only scan one thing".
 */
export function fromSweepListFilter(filter: SweepListFilter): SymphonyFilterState {
  return {
    requestId: filter.requestId ?? '',
    processId: filter.processId ?? '',
    processKey: filter.processKey,
    referenceId: filter.referenceId ?? '',
    externalKey: filter.externalKey ?? '',
    startDate: fromSymphonyDateParam(filter.startTimeInitStr),
    endDate: fromSymphonyDateParam(filter.startTimeEndStr),
    statuses: filter.statuses,
    deadJob: filter.deadJob
  }
}
