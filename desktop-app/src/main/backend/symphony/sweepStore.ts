// Persistence for deep-search sweeps.
//
// WHY NOT THE .enc PATTERN USED BY THE OTHER STORES IN THIS DIRECTORY:
// settings/uiPrefs/savedDomains/savedTabSets each re-serialize, re-encrypt and
// writeFileSync the ENTIRE document on every mutation. A sweep mutates once per
// scanned request — thousands of times — against a document that grows to
// thousands of scanned ids plus up to 2000 hits. That is O(n^2) write
// amplification, and worse, safeStorage.encryptString is synchronous and on
// Linux/libsecret round-trips to the keyring daemon. Thousands of those on the
// main thread would block the event loop, which blocks ipcMain, which freezes
// the whole UI — not just the sweep.
//
// Instead, per job:
//   <userData>/sweeps/<profileId>/<jobId>.job   small header, atomic rewrite, <=1/3s
//   <userData>/sweeps/<profileId>/<jobId>.log   append-only, one framed record per line
//
// ON LOAD THE LOG IS AUTHORITATIVE. The scanned-id set, the hits and every
// counter are replayed from it; the header only contributes immutable config,
// the name, and a cursor floor. That makes "header and log disagree after a
// crash" impossible to matter — worst case the cursor is one page (200 rows)
// stale, and those rows are re-listed and skipped in ~0.8s.
//
// Lines ARE encrypted, individually. safeStorage has no streaming API, so the
// only alternatives are per-line encryption or rewriting the whole blob per
// flush (which defeats the point). Batched, a full sweep is a few hundred
// encrypt calls, not thousands. Encryption is warranted because a hit excerpt
// is by construction the region of a variable value that matched the user's
// query — the single most likely place for the sensitive thing to be. Observed
// sample data contained bearer tokens, codici fiscali and email addresses.

import { app, safeStorage } from 'electron'
import {
  appendFileSync,
  existsSync,
  mkdirSync,
  readdirSync,
  readFileSync,
  renameSync,
  rmSync,
  writeFileSync
} from 'fs'
import { join } from 'path'
import type { SweepHit, SweepJob, SweepSegment } from './sweepTypes'

const ID_PATTERN = /^[A-Za-z0-9._-]{1,64}$/
const LOG_MAGIC_PREFIX = '#snappy-sweep-log v1'
const FLUSH_RECORDS = 25
const FLUSH_MS = 2000
const HEADER_FLUSH_MS = 3000
export const MAX_JOBS_PER_PROFILE = 50

export type SweepLogRecord =
  | { t: 'meta'; at: string; segments: SweepSegment[]; note?: string }
  | { t: 'scan'; at: string; seg: number; off: number; ids: string[] }
  | { t: 'hit'; at: string; hit: SweepHit }
  | { t: 'reqerr'; at: string; requestId: string; message: string }

export class SweepLogCorruptError extends Error {}

// ---------------------------------------------------------------- paths

function sweepsRoot(): string {
  return join(app.getPath('userData'), 'sweeps')
}

/**
 * Reject rather than sanitize: jobId arrives over IPC and profileId comes from a
 * hand-editable settings file, and a silently-rewritten id would split one job
 * across two files.
 */
function assertId(value: string, what: string): string {
  if (!ID_PATTERN.test(value)) {
    throw new Error(`Invalid ${what}: ${JSON.stringify(value)}`)
  }
  return value
}

function profileDir(profileId: string): string {
  return join(sweepsRoot(), assertId(profileId, 'profile id'))
}

function headerPath(profileId: string, jobId: string): string {
  return join(profileDir(profileId), `${assertId(jobId, 'job id')}.job`)
}

function logPath(profileId: string, jobId: string): string {
  return join(profileDir(profileId), `${assertId(jobId, 'job id')}.log`)
}

function ensureDir(profileId: string): void {
  mkdirSync(profileDir(profileId), { recursive: true })
}

// ---------------------------------------------------------------- framing

function encryptionAvailable(): boolean {
  return safeStorage.isEncryptionAvailable()
}

function frame(record: SweepLogRecord): string {
  const json = JSON.stringify(record)
  return encryptionAvailable() ? safeStorage.encryptString(json).toString('base64') : json
}

function unframe(line: string, encrypted: boolean): SweepLogRecord {
  const json = encrypted ? safeStorage.decryptString(Buffer.from(line, 'base64')) : line
  return JSON.parse(json) as SweepLogRecord
}

// ---------------------------------------------------------------- header I/O

/** Atomic: the existing stores writeFileSync in place and are corruption-prone,
 *  which is not acceptable for a file rewritten every few seconds for hours. */
function writeHeaderNow(job: SweepJob): void {
  ensureDir(job.profileId)
  const path = headerPath(job.profileId, job.id)
  const tmp = `${path}.tmp`
  writeFileSync(tmp, JSON.stringify(job), 'utf-8')
  renameSync(tmp, path)
}

function readHeader(profileId: string, jobId: string): SweepJob | null {
  const path = headerPath(profileId, jobId)
  if (!existsSync(path)) {
    return null
  }
  try {
    return JSON.parse(readFileSync(path, 'utf-8')) as SweepJob
  } catch {
    return null
  }
}

// ---------------------------------------------------------------- log I/O

type LogBuffer = { records: SweepLogRecord[]; timer: NodeJS.Timeout | null }

const logBuffers = new Map<string, LogBuffer>()
const headerTimers = new Map<string, NodeJS.Timeout>()

function bufferKey(profileId: string, jobId: string): string {
  return `${profileId}/${jobId}`
}

function ensureLogHeader(profileId: string, jobId: string): void {
  const path = logPath(profileId, jobId)
  if (existsSync(path)) {
    return
  }
  ensureDir(profileId)
  writeFileSync(path, `${LOG_MAGIC_PREFIX} enc=${encryptionAvailable() ? 1 : 0}\n`, 'utf-8')
}

export function flushLog(profileId: string, jobId: string): void {
  const key = bufferKey(profileId, jobId)
  const buffer = logBuffers.get(key)
  if (!buffer || buffer.records.length === 0) {
    return
  }
  const records = buffer.records
  buffer.records = []
  if (buffer.timer) {
    clearTimeout(buffer.timer)
    buffer.timer = null
  }
  ensureLogHeader(profileId, jobId)
  appendFileSync(logPath(profileId, jobId), `${records.map(frame).join('\n')}\n`, 'utf-8')
}

export function appendLog(profileId: string, jobId: string, record: SweepLogRecord): void {
  const key = bufferKey(profileId, jobId)
  let buffer = logBuffers.get(key)
  if (!buffer) {
    buffer = { records: [], timer: null }
    logBuffers.set(key, buffer)
  }
  buffer.records.push(record)
  if (buffer.records.length >= FLUSH_RECORDS) {
    flushLog(profileId, jobId)
    return
  }
  if (!buffer.timer) {
    buffer.timer = setTimeout(() => flushLog(profileId, jobId), FLUSH_MS)
  }
}

export type ReplayResult = {
  scannedIds: Set<string>
  hits: SweepHit[]
  segments: SweepSegment[] | null
  requestErrors: number
  /** Highest (segment, offset) whose page completed — the cursor floor. */
  cursor: { seg: number; off: number } | null
  corrupted: string | null
}

/**
 * Streams the log and rebuilds every derived value. Reads line-by-line off one
 * buffer rather than splitting a giant string, so a long sweep's log stays
 * bounded in memory.
 */
export function replayLog(profileId: string, jobId: string): ReplayResult {
  const result: ReplayResult = {
    scannedIds: new Set<string>(),
    hits: [],
    segments: null,
    requestErrors: 0,
    cursor: null,
    corrupted: null
  }

  const path = logPath(profileId, jobId)
  if (!existsSync(path)) {
    return result
  }

  const content = readFileSync(path, 'utf-8')
  const lines = content.split('\n')
  const magic = lines[0] ?? ''
  if (!magic.startsWith(LOG_MAGIC_PREFIX)) {
    result.corrupted = 'log header missing or unrecognized'
    return result
  }
  const encrypted = magic.includes('enc=1')
  if (encrypted && !encryptionAvailable()) {
    result.corrupted = 'log was written encrypted but no OS keychain provider is available'
    return result
  }

  for (let i = 1; i < lines.length; i++) {
    const line = lines[i]
    if (!line) {
      continue
    }
    let record: SweepLogRecord
    try {
      record = unframe(line, encrypted)
    } catch {
      // A torn FINAL line is expected after a crash mid-append. A torn line in
      // the middle is not: silently dropping it would under-report the scanned
      // set (re-fetching megabytes already processed) and drop hits the user has
      // already seen, so surface it instead of truncating.
      const isFinalRecord = lines.slice(i + 1).every((rest) => rest === '')
      if (!isFinalRecord) {
        result.corrupted = `log corrupted at line ${i + 1}`
      }
      break
    }

    switch (record.t) {
      case 'meta':
        result.segments = record.segments
        break
      case 'scan':
        record.ids.forEach((id) => result.scannedIds.add(id))
        result.cursor = { seg: record.seg, off: record.off }
        break
      case 'hit':
        result.hits.push(record.hit)
        break
      case 'reqerr':
        result.requestErrors++
        break
    }
  }

  return result
}

// ---------------------------------------------------------------- header cache

const headers = new Map<string, SweepJob>()

export function putHeader(job: SweepJob, immediate: boolean = false): void {
  const key = bufferKey(job.profileId, job.id)
  headers.set(key, job)
  if (immediate) {
    const timer = headerTimers.get(key)
    if (timer) {
      clearTimeout(timer)
      headerTimers.delete(key)
    }
    writeHeaderNow(job)
    return
  }
  if (headerTimers.has(key)) {
    return
  }
  headerTimers.set(
    key,
    setTimeout(() => {
      headerTimers.delete(key)
      const latest = headers.get(key)
      if (latest) {
        writeHeaderNow(latest)
      }
    }, HEADER_FLUSH_MS)
  )
}

export function getHeader(profileId: string, jobId: string): SweepJob | null {
  const key = bufferKey(profileId, jobId)
  const cached = headers.get(key)
  if (cached) {
    return cached
  }
  const loaded = readHeader(profileId, jobId)
  if (loaded) {
    headers.set(key, loaded)
  }
  return loaded
}

export function listHeaders(profileId: string): SweepJob[] {
  const dir = profileDir(profileId)
  if (!existsSync(dir)) {
    return []
  }
  const jobIds = readdirSync(dir)
    .filter((f) => f.endsWith('.job'))
    .map((f) => f.slice(0, -'.job'.length))

  return jobIds
    .map((jobId) => getHeader(profileId, jobId))
    .filter((job): job is SweepJob => job != null)
    .sort((a, b) => b.createdAt.localeCompare(a.createdAt))
}

export function deleteJob(profileId: string, jobId: string): void {
  const key = bufferKey(profileId, jobId)
  const timer = headerTimers.get(key)
  if (timer) {
    clearTimeout(timer)
    headerTimers.delete(key)
  }
  const buffer = logBuffers.get(key)
  if (buffer?.timer) {
    clearTimeout(buffer.timer)
  }
  logBuffers.delete(key)
  headers.delete(key)
  rmSync(headerPath(profileId, jobId), { force: true })
  rmSync(logPath(profileId, jobId), { force: true })
}

/**
 * Discards a job's results log, keeping its header.
 *
 * Needed when the request filter changes: the scanned-id set, cursor and hits
 * all describe the OLD query, so carrying them over would silently skip requests
 * the new filter wants and report matches from outside it. Since the log is
 * authoritative on load, clearing it is what actually resets the job.
 */
export function resetLog(profileId: string, jobId: string): void {
  const key = bufferKey(profileId, jobId)
  const buffer = logBuffers.get(key)
  if (buffer?.timer) {
    clearTimeout(buffer.timer)
  }
  logBuffers.delete(key)
  rmSync(logPath(profileId, jobId), { force: true })
}

/** Keeps disk bounded (~1.4MB/job) by dropping the oldest finished jobs. */
export function pruneJobs(profileId: string): void {
  const jobs = listHeaders(profileId)
  if (jobs.length <= MAX_JOBS_PER_PROFILE) {
    return
  }
  const removable = jobs
    .filter((j) => j.status === 'done' || j.status === 'error')
    .sort((a, b) => a.createdAt.localeCompare(b.createdAt))
  const excess = jobs.length - MAX_JOBS_PER_PROFILE
  removable.slice(0, excess).forEach((j) => deleteJob(profileId, j.id))
}

/**
 * Called at startup, before the window exists: a header left `running` or
 * `queued` by a crash or a quit would otherwise render as a phantom job with a
 * frozen progress bar. A directory scan plus <=50 small reads, no network.
 */
export function demoteInterruptedJobs(): void {
  const root = sweepsRoot()
  if (!existsSync(root)) {
    return
  }
  for (const profileId of readdirSync(root)) {
    if (!ID_PATTERN.test(profileId)) {
      continue
    }
    for (const job of listHeaders(profileId)) {
      if (job.status === 'running' || job.status === 'queued') {
        putHeader(
          {
            ...job,
            status: 'paused',
            pauseReason: 'app-quit',
            updatedAt: new Date().toISOString()
          },
          true
        )
      }
    }
  }
}

/** Synchronous on purpose — async writes in `before-quit` are unreliable. */
export function flushAll(): void {
  for (const key of [...logBuffers.keys()]) {
    const [profileId, jobId] = key.split('/')
    flushLog(profileId, jobId)
  }
  for (const [key, timer] of [...headerTimers.entries()]) {
    clearTimeout(timer)
    headerTimers.delete(key)
    const job = headers.get(key)
    if (job) {
      writeHeaderNow(job)
    }
  }
}
