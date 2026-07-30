// The deep-search sweep loop.
//
// Runs in the MAIN process, not the renderer, for three independent reasons:
//  1. Switching profiles does a hard window.location.reload() in the renderer,
//     which would destroy a multi-hour sweep.
//  2. Each scanned request pulls a multi-megabyte variables payload. In the
//     renderer every one of those would be structured-cloned across
//     contextBridge only to be discarded — tens of gigabytes over a full sweep.
//  3. The persistent store is a main-process file.

import { app, type BrowserWindow } from 'electron'
import { randomUUID } from 'crypto'
import { getStore } from '../settings'
import { getHistoricVariables, getRequestTree } from './client'
import {
  appendLog,
  deleteJob as deleteJobFiles,
  flushAll,
  flushLog,
  getHeader,
  listHeaders,
  pruneJobs,
  putHeader,
  replayLog,
  resetLog
} from './sweepStore'
import {
  DEFAULT_SWEEP_OPTIONS,
  type CreateSweepInput,
  type SweepHit,
  isClauseEmpty,
  isPredicateEmpty,
  normalizePredicate,
  type SweepClause,
  type SweepJob,
  type SweepListFilter,
  type SweepOptions,
  type SweepPredicate,
  type SweepProgress,
  type SweepSegment,
  type SweepSnapshot,
  type SweepStringMatch
} from './sweepTypes'
import type { SymphonyRequestRow, SymphonyVariable } from './types'

const LIST_PAGE_SIZE = 200
const PROGRESS_THROTTLE_MS = 500
const RETRY_DELAYS_MS = [1000, 4000, 15_000, 60_000]
/** Consecutive exhausted-retry failures that park the whole job. */
const CIRCUIT_BREAK_AFTER = 5
const MAX_MATCHES_PER_REQUEST = 5
const EXCERPT_BEFORE = 128
const EXCERPT_AFTER = 384

class ProfileChangedError extends Error {
  constructor() {
    super('The active profile changed while this sweep was running.')
  }
}

function isAbort(err: unknown): boolean {
  return err instanceof Error && (err.name === 'AbortError' || err.name === 'TimeoutError')
}

function sleep(ms: number, signal: AbortSignal): Promise<void> {
  if (ms <= 0) return Promise.resolve()
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      signal.removeEventListener('abort', onAbort)
      resolve()
    }, ms)
    function onAbort(): void {
      clearTimeout(timer)
      reject(new DOMException('Aborted', 'AbortError'))
    }
    signal.addEventListener('abort', onAbort, { once: true })
  })
}

function clamp(value: number, min: number, max: number): number {
  return Math.min(max, Math.max(min, value))
}

/** Never trust renderer-supplied throttle knobs. */
function clampOptions(input: Partial<SweepOptions> | undefined): SweepOptions {
  const merged = { ...DEFAULT_SWEEP_OPTIONS, ...(input ?? {}) }
  return {
    concurrency: clamp(Math.round(merged.concurrency), 1, 4),
    delayMs: clamp(Math.round(merged.delayMs), 0, 5000),
    timeoutMs: clamp(Math.round(merged.timeoutMs), 30_000, 600_000),
    excerptBytes: clamp(Math.round(merged.excerptBytes), 64, 4096),
    maxHits: clamp(Math.round(merged.maxHits), 1, 5000)
  }
}

// ---------------------------------------------------------------- predicate

function matches(haystack: string, match: SweepStringMatch, caseSensitive: boolean): number {
  const needle = caseSensitive ? match.value : match.value.toLowerCase()
  const target = caseSensitive ? haystack : haystack.toLowerCase()
  switch (match.op) {
    case 'equals':
      return target === needle ? 0 : -1
    case 'startsWith':
      return target.startsWith(needle) ? 0 : -1
    case 'endsWith':
      return target.endsWith(needle) ? target.length - needle.length : -1
    case 'contains':
    default:
      return target.indexOf(needle)
  }
}

/** Offset of the match within varValue, or -1. Both halves of a clause must hit
 *  the SAME variable — that's the point of testing them together here. */
function testClause(
  variable: SymphonyVariable,
  clause: SweepClause,
  caseSensitive: boolean
): number {
  const { name, value } = clause
  if (name?.value && matches(variable.varName, name, caseSensitive) === -1) {
    return -1
  }
  if (!value?.value) {
    return 0
  }
  return matches(variable.varValue ?? '', value, caseSensitive)
}

type ClauseMatch = { clauseIndex: number; variable: SymphonyVariable; offset: number }

/**
 * Evaluates the whole predicate against one process instance's variables.
 *
 * Clause-to-variable is many-to-many on purpose: under `all`, each clause may be
 * satisfied by a *different* variable of the same process (that's what makes
 * "contractId = X" + "value contains Y" useful), while within one clause the
 * name and value still have to land on the same variable.
 */
function evaluatePredicate(
  variables: SymphonyVariable[],
  predicate: SweepPredicate
): ClauseMatch[] | null {
  const clauses = predicate.clauses.filter((c) => !isClauseEmpty(c))
  if (clauses.length === 0) {
    return null
  }

  // Evidence is collected in two tiers so the cap can't hide a whole clause.
  // Filling one flat list in variable order biased it badly: with clause A
  // matching late-sorted variables and clause B early ones, every recorded hit
  // came from B and an "A AND B" match showed no A evidence at all.
  const firstPerClause = new Array<ClauseMatch | null>(clauses.length).fill(null)
  const extras: ClauseMatch[] = []
  const satisfied = new Array<boolean>(clauses.length).fill(false)

  for (const variable of variables) {
    for (let i = 0; i < clauses.length; i++) {
      const offset = testClause(variable, clauses[i], predicate.caseSensitive)
      if (offset === -1) {
        continue
      }
      // Evaluation is never capped — `satisfied` must keep filling in so an
      // `all` predicate is judged on the full variable set.
      satisfied[i] = true
      if (!firstPerClause[i]) {
        firstPerClause[i] = { clauseIndex: i, variable, offset }
      } else if (extras.length < MAX_MATCHES_PER_REQUEST) {
        extras.push({ clauseIndex: i, variable, offset })
      }
    }
  }

  const passes = predicate.mode === 'any' ? satisfied.some(Boolean) : satisfied.every(Boolean)
  if (!passes) {
    return null
  }

  // One match per satisfied clause first, then extras up to the cap.
  const primary = firstPerClause.filter((m): m is ClauseMatch => m != null)
  return [...primary, ...extras.slice(0, Math.max(0, MAX_MATCHES_PER_REQUEST - primary.length))]
}

/** Masks the two token shapes that actually turned up in sample variable data.
 *  Applied ONLY to the persisted excerpt, never to what the detail tab shows —
 *  redacting there would break the feature. */
function redact(text: string): string {
  return text
    .replace(/Bearer\s+[\w-]+\.[\w-]+\.[\w-]+/gi, 'Bearer ***')
    .replace(/eyJ[\w-]{20,}/g, 'eyJ***')
}

/** Truncates by byte length at a code-point boundary: a split surrogate pair
 *  would break JSON.parse when the log is replayed. */
function truncateBytes(text: string, maxBytes: number): string {
  if (Buffer.byteLength(text, 'utf-8') <= maxBytes) {
    return text
  }
  let out = ''
  let bytes = 0
  for (const char of text) {
    const size = Buffer.byteLength(char, 'utf-8')
    if (bytes + size > maxBytes) break
    out += char
    bytes += size
  }
  return out
}

function buildExcerpt(value: string, offset: number, maxBytes: number): string {
  const start = Math.max(0, offset - EXCERPT_BEFORE)
  const end = Math.min(value.length, offset + EXCERPT_AFTER)
  const slice = value.slice(start, end)
  const prefix = start > 0 ? '…' : ''
  const suffix = end < value.length ? '…' : ''
  return truncateBytes(`${prefix}${redact(slice)}${suffix}`, maxBytes)
}

// ---------------------------------------------------------------- segmentation

const MS_PER_DAY = 24 * 60 * 60 * 1000
const SEGMENT_THRESHOLD_DAYS = 3

function parseParamDate(value: string | null): number | null {
  if (!value) return null
  const m = /^(\d{2})\/(\d{2})\/(\d{4}) (\d{2}):(\d{2})$/.exec(value)
  if (!m) return null
  const [, dd, mm, yyyy, hh, mi] = m
  return new Date(Number(yyyy), Number(mm) - 1, Number(dd), Number(hh), Number(mi)).getTime()
}

function formatParamDate(ms: number): string {
  const d = new Date(ms)
  const p = (n: number): string => String(n).padStart(2, '0')
  return `${p(d.getDate())}/${p(d.getMonth() + 1)}/${d.getFullYear()} ${p(d.getHours())}:${p(d.getMinutes())}`
}

/**
 * Splits a wide window into per-day sub-windows.
 *
 * This is the structural answer to the server's 10000-result enumeration cap:
 * the cap is per query, so a per-day query essentially never trips it while a
 * month-wide query on a busy tenant is guaranteed to. Costs nothing — the API
 * already takes the window as parameters.
 */
function buildSegments(startStr: string | null, endStr: string | null): SweepSegment[] {
  const blank = (): SweepSegment[] => [
    {
      startTimeInitStr: startStr,
      startTimeEndStr: endStr,
      recordsLoaded: 0,
      reportedTotal: null,
      headRequestId: null,
      listComplete: false,
      truncated: false
    }
  ]

  const start = parseParamDate(startStr)
  const end = parseParamDate(endStr)
  if (start == null || end == null || end <= start) {
    return blank()
  }
  if (end - start <= SEGMENT_THRESHOLD_DAYS * MS_PER_DAY) {
    return blank()
  }

  const segments: SweepSegment[] = []
  for (let from = start; from < end; from += MS_PER_DAY) {
    const to = Math.min(from + MS_PER_DAY, end)
    segments.push({
      startTimeInitStr: formatParamDate(from),
      startTimeEndStr: formatParamDate(to),
      recordsLoaded: 0,
      reportedTotal: null,
      headRequestId: null,
      listComplete: false,
      truncated: false
    })
  }
  return segments
}

/**
 * "No status ticked" means "don't filter by status", but the API reads an empty
 * listStatusSelected as "match nothing" (0 rows). Expand it here so a job saved
 * with no statuses sweeps everything rather than silently nothing.
 */
/**
 * Omit rather than expand — `listStatusSelected` is an allowlist that drops
 * statuses it isn't told about (RESUBMIT, at least). A sweep with no status
 * selected must cover everything, including statuses this app doesn't know.
 */
function resolveJobStatuses(job: SweepJob): SweepJob['filter']['statuses'] | undefined {
  return job.filter.statuses.length > 0 ? job.filter.statuses : undefined
}

/** Only sent when ticked: `deadJob: true` constrains, it does not include. */
function resolveJobDeadJob(job: SweepJob): boolean | undefined {
  return job.filter.deadJob ? true : undefined
}

// ---------------------------------------------------------------- engine state

type RunState = {
  controller: AbortController
  scannedIds: Set<string>
  hitSeq: number
  pendingHits: SweepHit[]
  progressSeq: number
  lastProgressAt: number
  progressTimer: NodeJS.Timeout | null
  consecutiveFailures: number
  /** Newest header, so a coalesced progress tick never emits a stale snapshot. */
  latestJob: SweepJob | null
}

const runs = new Map<string, RunState>()
let getWindowRef: (() => BrowserWindow | null) | null = null
let queue: string[] = []
let activeJobId: string | null = null

function activeProfileId(): string {
  const id = getStore().activeProfileId
  if (!id) {
    throw new Error('No active profile.')
  }
  return id
}

function assertJobProfile(job: SweepJob): void {
  // Synchronous, and called immediately before every fetch: the base URL and
  // the Keycloak token are both resolved from the ACTIVE profile at request
  // time, so a profile switch mid-sweep would otherwise issue tenant-A queries
  // against tenant B with tenant B's token and write the results into a
  // tenant-A job file.
  if (getStore().activeProfileId !== job.profileId) {
    throw new ProfileChangedError()
  }
}

function touch(job: SweepJob): SweepJob {
  return { ...job, updatedAt: new Date().toISOString() }
}

/**
 * Pushes deltas rather than letting the renderer poll: a polled getter would
 * have to resend every hit each tick (2000 hits is ~1.4MB) or grow a cursor
 * protocol, which is deltas with worse latency. `seq` lets the renderer detect a
 * dropped delta (it reloads on profile switch and HMR) and resync via snapshot.
 */
function emitProgress(state: RunState, force: boolean): void {
  const send = (): void => {
    const job = state.latestJob
    if (!job) {
      return
    }
    state.lastProgressAt = Date.now()
    state.progressSeq++
    const newHits = state.pendingHits
    state.pendingHits = []
    const payload: SweepProgress = { jobId: job.id, seq: state.progressSeq, job, newHits }
    const win = getWindowRef?.()
    // A send to a destroyed/reloading webContents is silently dropped, which is
    // harmless: the log is the durable record and `seq` triggers a resync.
    if (win && !win.isDestroyed() && !win.webContents.isDestroyed()) {
      win.webContents.send('symphony:deepSearch:progress', payload)
    }
  }

  if (force) {
    if (state.progressTimer) {
      clearTimeout(state.progressTimer)
      state.progressTimer = null
    }
    send()
    return
  }

  const elapsed = Date.now() - state.lastProgressAt
  if (elapsed >= PROGRESS_THROTTLE_MS) {
    send()
    return
  }
  if (!state.progressTimer) {
    state.progressTimer = setTimeout(() => {
      state.progressTimer = null
      send()
    }, PROGRESS_THROTTLE_MS - elapsed)
  }
}

function save(job: SweepJob, state: RunState | null, immediate = false): void {
  putHeader(job, immediate)
  if (state) {
    state.latestJob = job
    emitProgress(state, immediate)
  }
}

/** Retries transient failures. Aborts are never retried and never counted as
 *  errors — conflating our own pause with a failure is what produces jobs that
 *  "finish with 10000 errors". */
async function withRetry<T>(op: () => Promise<T>, signal: AbortSignal): Promise<T> {
  let lastError: unknown
  for (let attempt = 0; attempt <= RETRY_DELAYS_MS.length; attempt++) {
    try {
      return await op()
    } catch (err) {
      if (isAbort(err) || err instanceof ProfileChangedError) {
        throw err
      }
      lastError = err
      if (attempt === RETRY_DELAYS_MS.length) {
        break
      }
      const base = RETRY_DELAYS_MS[attempt]
      await sleep(Math.random() * base, signal)
    }
  }
  throw lastError
}

// ---------------------------------------------------------------- the loop

async function scanRequest(
  job: SweepJob,
  row: SymphonyRequestRow,
  state: RunState
): Promise<SweepHit[]> {
  // A request with no process instance has no variables to search.
  if (!row.processId) {
    return []
  }
  assertJobProfile(job)
  const page = await withRetry(
    () =>
      getHistoricVariables(row.processId, 1, 1000, state.controller.signal).then((r) => {
        // Re-check after the round trip: an in-flight request against the old
        // host is harmless as long as its result is discarded.
        assertJobProfile(job)
        return r
      }),
    state.controller.signal
  )

  const variables = page.data ?? []
  const matched = evaluatePredicate(variables, job.predicate)
  const hits: SweepHit[] = (matched ?? []).map(({ clauseIndex, variable, offset }) => {
    const value = variable.varValue ?? ''
    return {
      seq: 0, // assigned by the caller, which owns the counter
      clauseIndex,
      requestId: row.requestId,
      processId: row.processId,
      processKey: row.processKey ?? null,
      status: row.status ?? null,
      createdDate: row.createdDate ?? null,
      varName: variable.varName,
      varType: variable.varType ?? null,
      valueLength: value.length,
      matchOffset: Math.max(0, offset),
      excerpt: buildExcerpt(value, Math.max(0, offset), job.options.excerptBytes),
      foundAt: new Date().toISOString()
    }
  })
  // `variables` and every varValue in it go out of scope here. Nothing above
  // this line is retained — only the bounded excerpts leave.
  return hits
}

/** N workers pulling from a shared index over one page, with a minimum gap
 *  between starts. Hand-rolled rather than adding p-limit for 15 lines. */
async function scanPage(
  job: SweepJob,
  rows: SymphonyRequestRow[],
  state: RunState,
  onJob: (next: SweepJob) => SweepJob
): Promise<SweepJob> {
  let current = job
  let index = 0
  let lastStart = 0

  const worker = async (): Promise<void> => {
    for (;;) {
      if (state.controller.signal.aborted) return
      const i = index++
      if (i >= rows.length) return
      const row = rows[i]

      const gap = current.options.delayMs - (Date.now() - lastStart)
      if (gap > 0) {
        await sleep(gap, state.controller.signal)
      }
      lastStart = Date.now()

      try {
        const hits = await scanRequest(current, row, state)
        state.consecutiveFailures = 0
        state.scannedIds.add(row.requestId)

        const counters = {
          ...current.counters,
          scanned: current.counters.scanned + 1,
          hits: current.counters.hits + hits.length
        }
        let hitsTruncated = current.hitsTruncated
        for (const hit of hits) {
          if (state.hitSeq >= current.options.maxHits) {
            // Stop recording, keep counting — a capped counter would be a lie.
            hitsTruncated = true
            break
          }
          const stored: SweepHit = { ...hit, seq: state.hitSeq++ }
          appendLog(current.profileId, current.id, {
            t: 'hit',
            at: stored.foundAt,
            hit: stored
          })
          state.pendingHits.push(stored)
        }
        current = onJob(touch({ ...current, counters, hitsTruncated }))
      } catch (err) {
        if (isAbort(err) || err instanceof ProfileChangedError) {
          throw err
        }
        state.consecutiveFailures++
        const message = err instanceof Error ? err.message : String(err)
        appendLog(current.profileId, current.id, {
          t: 'reqerr',
          at: new Date().toISOString(),
          requestId: row.requestId,
          message
        })
        current = onJob(
          touch({
            ...current,
            counters: { ...current.counters, requestErrors: current.counters.requestErrors + 1 }
          })
        )
        // One bad process instance must not kill a 4-hour sweep, but a server
        // that is down should stop the job rather than grind for hours.
        if (state.consecutiveFailures >= CIRCUIT_BREAK_AFTER) {
          throw new CircuitBreakError(message)
        }
      }
    }
  }

  const workers = Array.from({ length: current.options.concurrency }, () => worker())
  await Promise.all(workers)
  return current
}

class CircuitBreakError extends Error {}

async function runJob(jobId: string, profileId: string): Promise<void> {
  const initial = getHeader(profileId, jobId)
  if (!initial) {
    return
  }

  const replay = replayLog(profileId, jobId)
  if (replay.corrupted) {
    save(
      touch({
        ...initial,
        status: 'error',
        error: replay.corrupted,
        finishedAt: new Date().toISOString()
      }),
      null,
      true
    )
    return
  }

  const state: RunState = {
    controller: new AbortController(),
    scannedIds: replay.scannedIds,
    hitSeq: replay.hits.length,
    pendingHits: [],
    progressSeq: 0,
    lastProgressAt: 0,
    progressTimer: null,
    consecutiveFailures: 0,
    latestJob: null
  }
  runs.set(jobId, state)
  activeJobId = jobId

  // The log is authoritative — counters come from the replay, not the header.
  let job = touch({
    ...initial,
    // Legacy headers carry the single-clause predicate shape; normalize on load.
    predicate: normalizePredicate(initial.predicate),
    segments: replay.segments ?? initial.segments,
    status: 'running',
    pauseReason: null,
    error: null,
    startedAt: initial.startedAt ?? new Date().toISOString(),
    counters: {
      ...initial.counters,
      scanned: replay.scannedIds.size,
      hits: replay.hits.length,
      requestErrors: replay.requestErrors
    }
  })
  save(job, state, true)

  const onJob = (next: SweepJob): SweepJob => {
    job = next
    save(job, state)
    return job
  }

  try {
    for (let segIndex = job.segmentIndex; segIndex < job.segments.length; segIndex++) {
      job = onJob({ ...job, segmentIndex: segIndex })

      for (;;) {
        if (state.controller.signal.aborted) {
          throw new DOMException('Aborted', 'AbortError')
        }
        const segment = job.segments[segIndex]
        if (segment.listComplete) {
          break
        }

        assertJobProfile(job)
        const page = await withRetry(
          () =>
            getRequestTree(
              {
                name: job.filter.processKey ?? undefined,
                requestId: job.filter.requestId ?? undefined,
                processId: job.filter.processId ?? undefined,
                referenceId: job.filter.referenceId ?? undefined,
                externalKey: job.filter.externalKey ?? undefined,
                startTimeInitStr: segment.startTimeInitStr ?? undefined,
                startTimeEndStr: segment.startTimeEndStr ?? undefined,
                pageSize: String(LIST_PAGE_SIZE),
                recordsLoaded: segment.recordsLoaded,
                listStatusSelected: resolveJobStatuses(job),
                deadJob: resolveJobDeadJob(job),
                sorters: [{ dir: 'desc', field: 'createdDate' }]
              },
              state.controller.signal
            ),
          state.controller.signal
        )

        const rows = page.rows ?? []
        let driftDetected = job.driftDetected
        let headRequestId = segment.headRequestId
        if (segment.recordsLoaded === 0) {
          headRequestId = rows[0]?.requestId ?? null
        } else if (headRequestId && rows.length > 0) {
          // The frozen end-of-window should make the result set stable. If the
          // head moved anyway, offset paging can't be trusted — fall back
          // entirely on the scanned-id set, which is the real correctness
          // mechanism, and restart this segment.
          const check = await withRetry(
            () =>
              getRequestTree(
                {
                  name: job.filter.processKey ?? undefined,
                  startTimeInitStr: segment.startTimeInitStr ?? undefined,
                  startTimeEndStr: segment.startTimeEndStr ?? undefined,
                  pageSize: '1',
                  recordsLoaded: 0,
                  listStatusSelected: resolveJobStatuses(job),
                  deadJob: resolveJobDeadJob(job),
                  sorters: [{ dir: 'desc', field: 'createdDate' }]
                },
                state.controller.signal
              ),
            state.controller.signal
          )
          const currentHead = check.rows[0]?.requestId ?? null
          if (currentHead && currentHead !== headRequestId) {
            driftDetected = true
            appendLog(job.profileId, job.id, {
              t: 'meta',
              at: new Date().toISOString(),
              segments: job.segments,
              note: `head drift in segment ${segIndex}: ${headRequestId} -> ${currentHead}`
            })
            headRequestId = currentHead
            job = onJob(
              touch({
                ...job,
                driftDetected,
                segments: job.segments.map((s, i) =>
                  i === segIndex ? { ...s, recordsLoaded: 0, headRequestId } : s
                )
              })
            )
            continue
          }
        }

        const fresh = rows.filter((row) => !state.scannedIds.has(row.requestId))
        const skipped = rows.length - fresh.length
        const truncated =
          page.tableLimit ||
          (page.moreRecords && segment.recordsLoaded + LIST_PAGE_SIZE >= page.maximumRecordsNumber)

        job = onJob(
          touch({
            ...job,
            driftDetected,
            counters: {
              ...job.counters,
              listed: job.counters.listed + rows.length,
              skipped: job.counters.skipped + skipped
            },
            segments: job.segments.map((s, i) =>
              i === segIndex
                ? { ...s, headRequestId, reportedTotal: page.maximumRecordsNumber, truncated }
                : s
            ),
            truncated: job.truncated || truncated
          })
        )

        job = await scanPage(job, fresh, state, onJob)

        // The cursor only advances at a page boundary, after every row on the
        // page has been scanned AND its scan record flushed. A crash mid-page
        // re-lists the page and the scanned-id set skips what's done.
        const nextOffset = segment.recordsLoaded + rows.length
        const listComplete = !page.moreRecords || truncated || rows.length === 0
        appendLog(job.profileId, job.id, {
          t: 'scan',
          at: new Date().toISOString(),
          seg: segIndex,
          off: nextOffset,
          ids: rows.map((r) => r.requestId)
        })
        flushLog(job.profileId, job.id)

        job = onJob(
          touch({
            ...job,
            segments: job.segments.map((s, i) =>
              i === segIndex ? { ...s, recordsLoaded: nextOffset, listComplete } : s
            )
          })
        )

        if (listComplete) {
          break
        }
        await sleep(500, state.controller.signal)
      }
    }

    flushLog(job.profileId, job.id)
    save(
      touch({ ...job, status: 'done', pauseReason: null, finishedAt: new Date().toISOString() }),
      state,
      true
    )
  } catch (err) {
    flushLog(job.profileId, job.id)
    if (isAbort(err)) {
      save(touch({ ...job, status: 'paused', pauseReason: job.pauseReason ?? 'user' }), state, true)
    } else if (err instanceof ProfileChangedError) {
      save(touch({ ...job, status: 'paused', pauseReason: 'profile-switch' }), state, true)
    } else if (err instanceof CircuitBreakError) {
      save(
        touch({ ...job, status: 'paused', pauseReason: 'server-errors', error: err.message }),
        state,
        true
      )
    } else {
      save(
        touch({
          ...job,
          status: 'error',
          error: err instanceof Error ? err.message : String(err),
          finishedAt: new Date().toISOString()
        }),
        state,
        true
      )
    }
  } finally {
    runs.delete(jobId)
    if (activeJobId === jobId) {
      activeJobId = null
    }
    promoteQueue()
  }
}

function promoteQueue(): void {
  if (activeJobId || queue.length === 0) {
    return
  }
  const nextId = queue.shift() as string
  const profileId = getStore().activeProfileId
  if (!profileId) {
    return
  }
  const job = getHeader(profileId, nextId)
  if (!job || job.status !== 'queued') {
    promoteQueue()
    return
  }
  void runJob(nextId, profileId)
}

// ---------------------------------------------------------------- public API

export function initDeepSearch(getWindow: () => BrowserWindow | null): void {
  getWindowRef = getWindow
  app.on('before-quit', () => {
    for (const state of runs.values()) {
      state.controller.abort()
    }
    for (const profileId of new Set([getStore().activeProfileId].filter(Boolean) as string[])) {
      for (const job of listHeaders(profileId)) {
        if (job.status === 'running' || job.status === 'queued') {
          putHeader({ ...job, status: 'paused', pauseReason: 'app-quit' }, false)
        }
      }
    }
    flushAll()
  })
}

export function listSweeps(): SweepJob[] {
  const profileId = getStore().activeProfileId
  if (!profileId) {
    return []
  }
  return listHeaders(profileId).map((job) => ({
    ...job,
    predicate: normalizePredicate(job.predicate)
  }))
}

export function getSweepSnapshot(jobId: string): SweepSnapshot | null {
  const profileId = activeProfileId()
  const job = getHeader(profileId, jobId)
  if (!job) {
    return null
  }
  const replay = replayLog(profileId, jobId)
  return { job: { ...job, predicate: normalizePredicate(job.predicate) }, hits: replay.hits }
}

export function createSweep(input: CreateSweepInput): SweepJob {
  const profileId = activeProfileId()
  const now = new Date().toISOString()
  // Freeze the end of the window at creation: with createdDate-desc offset
  // paging, requests arriving mid-sweep would shift every row right, causing
  // re-scans and skips. This is layer one of four (see buildSegments and the
  // scanned-id set).
  const filter = {
    ...input.filter,
    startTimeEndStr: input.filter.startTimeEndStr ?? formatParamDate(Date.now())
  }
  const job: SweepJob = {
    id: randomUUID(),
    profileId,
    name: input.name.trim() || 'Deep search',
    predicate: normalizePredicate(input.predicate),
    filter,
    options: clampOptions(input.options),
    segments: buildSegments(filter.startTimeInitStr, filter.startTimeEndStr),
    segmentIndex: 0,
    status: 'draft',
    pauseReason: null,
    error: null,
    counters: { listed: 0, scanned: 0, skipped: 0, hits: 0, requestErrors: 0 },
    hitsTruncated: false,
    truncated: false,
    driftDetected: false,
    createdAt: now,
    updatedAt: now,
    startedAt: null,
    finishedAt: null
  }
  putHeader(job, true)
  pruneJobs(profileId)
  return job
}

export type UpdateSweepPatch = {
  name?: string
  predicate?: SweepPredicate
  filter?: SweepListFilter
  options?: Partial<SweepOptions>
}

/** True when the two filters would enumerate a different set of requests. */
function filterChanged(a: SweepListFilter, b: SweepListFilter): boolean {
  const key = (f: SweepListFilter): string =>
    JSON.stringify([
      f.processKey,
      f.startTimeInitStr,
      f.startTimeEndStr,
      f.requestId,
      f.processId,
      f.referenceId,
      f.externalKey,
      [...f.statuses].sort(),
      f.deadJob
    ])
  return key(a) !== key(b)
}

export function updateSweep(jobId: string, patch: UpdateSweepPatch): SweepJob {
  const profileId = activeProfileId()
  const job = getHeader(profileId, jobId)
  if (!job) {
    throw new Error('Sweep not found.')
  }
  if (job.status === 'running' || job.status === 'queued') {
    throw new Error('Pause the sweep before changing it.')
  }

  let next = touch({
    ...job,
    name: patch.name?.trim() || job.name,
    predicate: patch.predicate ? normalizePredicate(patch.predicate) : job.predicate,
    options: patch.options ? clampOptions({ ...job.options, ...patch.options }) : job.options
  })

  if (patch.filter && filterChanged(job.filter, patch.filter)) {
    // Re-freeze the window end, exactly as createSweep does — otherwise an
    // open-ended filter would drift while the sweep runs.
    const filter: SweepListFilter = {
      ...patch.filter,
      startTimeEndStr: patch.filter.startTimeEndStr ?? formatParamDate(Date.now())
    }
    // Everything already recorded describes the old query, so it has to go. The
    // log is authoritative on load, so clearing it is the actual reset.
    resetLog(profileId, jobId)
    next = touch({
      ...next,
      filter,
      segments: buildSegments(filter.startTimeInitStr, filter.startTimeEndStr),
      segmentIndex: 0,
      status: 'draft',
      pauseReason: null,
      error: null,
      counters: { listed: 0, scanned: 0, skipped: 0, hits: 0, requestErrors: 0 },
      hitsTruncated: false,
      truncated: false,
      driftDetected: false,
      startedAt: null,
      finishedAt: null
    })
  }

  putHeader(next, true)
  return next
}

export function startSweep(jobId: string): SweepJob {
  const profileId = activeProfileId()
  const job = getHeader(profileId, jobId)
  if (!job) {
    throw new Error('Sweep not found.')
  }
  if (job.profileId !== profileId) {
    throw new Error('This sweep belongs to a different profile.')
  }
  if (isPredicateEmpty(normalizePredicate(job.predicate))) {
    throw new Error('Add at least one variable condition to search for.')
  }
  if (job.status === 'running' || job.status === 'queued') {
    return job
  }

  // One sweep at a time: a single job at concurrency 2 already pulls ~2.5MB/s
  // sustained from a shared internal service. A second would also multiply the
  // transient parsed-JSON peak.
  if (activeJobId) {
    const queued = touch({ ...job, status: 'queued', pauseReason: null, error: null })
    putHeader(queued, true)
    queue.push(jobId)
    return queued
  }

  const starting = touch({ ...job, status: 'running', pauseReason: null, error: null })
  putHeader(starting, true)
  void runJob(jobId, profileId)
  return starting
}

export function pauseSweep(jobId: string): SweepJob {
  const profileId = activeProfileId()
  const job = getHeader(profileId, jobId)
  if (!job) {
    throw new Error('Sweep not found.')
  }
  queue = queue.filter((id) => id !== jobId)
  const state = runs.get(jobId)
  const paused = touch({ ...job, status: 'paused', pauseReason: 'user' })
  putHeader(paused, true)
  state?.controller.abort()
  return paused
}

export function deleteSweep(jobId: string): void {
  const profileId = activeProfileId()
  queue = queue.filter((id) => id !== jobId)
  runs.get(jobId)?.controller.abort()
  deleteJobFiles(profileId, jobId)
}

/** Called from ipc.ts BEFORE the active profile actually changes. */
export function pauseAllForProfileSwitch(): void {
  queue = []
  const profileId = getStore().activeProfileId
  if (profileId) {
    for (const job of listHeaders(profileId)) {
      if (job.status === 'running' || job.status === 'queued') {
        putHeader({ ...job, status: 'paused', pauseReason: 'profile-switch' }, true)
      }
    }
  }
  for (const state of runs.values()) {
    state.controller.abort()
  }
  flushAll()
}
