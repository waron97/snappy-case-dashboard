import type { SymphonyRequestStatus } from './types'

export type SweepStatus = 'draft' | 'queued' | 'running' | 'paused' | 'done' | 'error'

export type SweepPauseReason =
  'user' | 'app-quit' | 'profile-switch' | 'server-errors' | 'not-configured'

export type SweepStringOp = 'contains' | 'equals' | 'startsWith' | 'endsWith'

export type SweepStringMatch = {
  op: SweepStringOp
  value: string
}

/**
 * One variable condition.
 *
 * When both name and value are present, BOTH must match the SAME variable —
 * otherwise "name contains X and value contains Y" would hit on two unrelated
 * variables in the same process.
 */
export type SweepClause = {
  /** Stable across edits so the UI can key rows without reordering surprises. */
  id: string
  name: SweepStringMatch | null
  value: SweepStringMatch | null
}

/** How multiple clauses combine across a process instance's variables. */
export type SweepClauseMode = 'all' | 'any'

/**
 * Several clauses are evaluated against ONE process instance's variable set.
 *
 * - `all`: every clause must match, each against *some* variable — so
 *   "name=contractId" + "value contains 2d50" can be satisfied by two different
 *   variables of the same process. This narrows.
 * - `any`: at least one clause matches. This broadens.
 *
 * Within a single clause, name and value still have to hit the same variable.
 *
 * There is deliberately no regex option: a user-supplied pattern evaluated
 * against a 1MB variable value in the main process is a ReDoS that freezes every
 * IPC channel with no way to interrupt it (a running JS regex cannot be
 * time-budgeted). All four ops are linear indexOf/startsWith/endsWith.
 */
export type SweepPredicate = {
  clauses: SweepClause[]
  mode: SweepClauseMode
  caseSensitive: boolean
}

/** The pre-multi-clause shape, still on disk in jobs created before it. */
type LegacySweepPredicate = {
  name?: SweepStringMatch | null
  value?: SweepStringMatch | null
  caseSensitive?: boolean
}

export function isClauseEmpty(clause: SweepClause): boolean {
  return !clause.name?.value && !clause.value?.value
}

/**
 * Accepts either predicate shape and returns the current one.
 *
 * Job headers are plain JSON on disk with no version field, so this is what
 * keeps a sweep created before multi-clause support loadable — it must stay
 * tolerant of a missing/!array `clauses` rather than assuming the new shape.
 */
export function normalizePredicate(raw: unknown): SweepPredicate {
  const candidate = (raw ?? {}) as Partial<SweepPredicate> & LegacySweepPredicate
  const caseSensitive = candidate.caseSensitive === true

  if (Array.isArray(candidate.clauses)) {
    const clauses = candidate.clauses
      .filter((c): c is SweepClause => c != null && typeof c === 'object')
      .map((c, i) => ({
        id: typeof c.id === 'string' && c.id ? c.id : `clause-${i}`,
        name: c.name?.value ? c.name : null,
        value: c.value?.value ? c.value : null
      }))
    return {
      clauses,
      mode: candidate.mode === 'any' ? 'any' : 'all',
      caseSensitive
    }
  }

  // Legacy single clause.
  const name = candidate.name?.value ? candidate.name : null
  const value = candidate.value?.value ? candidate.value : null
  return {
    clauses: name || value ? [{ id: 'clause-0', name, value }] : [],
    mode: 'all',
    caseSensitive
  }
}

/** True when the predicate would match everything, i.e. nothing to search for. */
export function isPredicateEmpty(predicate: SweepPredicate): boolean {
  return predicate.clauses.filter((c) => !isClauseEmpty(c)).length === 0
}

/**
 * Literal request-list params, frozen at job creation. Kept as the exact
 * `dd/MM/yyyy HH:mm` strings the API takes rather than Dates, so a resumed job
 * re-issues byte-identical queries months later.
 */
export type SweepListFilter = {
  processKey: string | null
  startTimeInitStr: string | null
  startTimeEndStr: string | null
  requestId: string | null
  processId: string | null
  referenceId: string | null
  externalKey: string | null
  statuses: SymphonyRequestStatus[]
  deadJob: boolean
}

export type SweepSegment = {
  startTimeInitStr: string | null
  startTimeEndStr: string | null
  /** Page-boundary granularity only — see the cursor note in sweepEngine.ts. */
  recordsLoaded: number
  /**
   * The server's `maximumRecordsNumber` for this window — its enumeration CAP,
   * NOT a count of matching rows (it is a constant 10000). Kept for the
   * truncation check only; it must never be used as a progress denominator.
   */
  reportedTotal: number | null
  /** Drift fingerprint: the head of page 0 when the segment started. */
  headRequestId: string | null
  listComplete: boolean
  /** The server refused to enumerate past its cap in this window. */
  truncated: boolean
}

export type SweepCounters = {
  listed: number
  scanned: number
  skipped: number
  hits: number
  requestErrors: number
}

export type SweepOptions = {
  concurrency: number
  delayMs: number
  timeoutMs: number
  excerptBytes: number
  maxHits: number
}

export const DEFAULT_SWEEP_OPTIONS: SweepOptions = {
  // The observed variable fetch is ~2.7s and ~3.4MB. Concurrency 1 would take
  // ~7.5h for 10k requests, 2 takes ~3.7h, 4 halves that again but doubles
  // sustained load on a shared service whose bottleneck is its own database.
  concurrency: 2,
  delayMs: 250,
  timeoutMs: 120_000,
  excerptBytes: 512,
  maxHits: 2000
}

export type SweepHit = {
  /** Monotonic within the job; equals log append order. */
  seq: number
  /** Which predicate clause this variable satisfied. 0 for pre-multi-clause hits. */
  clauseIndex?: number
  requestId: string
  processId: string
  processKey: string | null
  status: string | null
  /** Raw `dd/MM/yyyy HH:mm:ss.SSS` from the list row, unparsed. */
  createdDate: string | null
  varName: string
  varType: string | null
  /** Full value length, so the UI can say "match at 40912 of 1064221". */
  valueLength: number
  matchOffset: number
  /** Bounded and redacted — never the full value. */
  excerpt: string
  foundAt: string
}

export type SweepJob = {
  id: string
  profileId: string
  name: string
  predicate: SweepPredicate
  filter: SweepListFilter
  options: SweepOptions
  segments: SweepSegment[]
  segmentIndex: number
  status: SweepStatus
  pauseReason: SweepPauseReason | null
  error: string | null
  counters: SweepCounters
  /** True when maxHits was reached; scanning and counting continue. */
  hitsTruncated: boolean
  /** True when any segment hit the server's enumeration cap. */
  truncated: boolean
  driftDetected: boolean
  createdAt: string
  updatedAt: string
  startedAt: string | null
  finishedAt: string | null
}

export type SweepProgress = {
  jobId: string
  /** Renderer refetches the full snapshot when it sees a gap here. */
  seq: number
  job: SweepJob
  /** Appended since the previous delta — never resent. */
  newHits: SweepHit[]
}

export type SweepSnapshot = {
  job: SweepJob
  hits: SweepHit[]
}

export type CreateSweepInput = {
  name: string
  predicate: SweepPredicate
  filter: SweepListFilter
  options?: Partial<SweepOptions>
}
