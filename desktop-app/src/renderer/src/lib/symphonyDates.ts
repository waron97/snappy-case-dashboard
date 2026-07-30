// Symphony date handling.
//
// Three formats are in play and none of them is ISO:
//   - request params:  dd/MM/yyyy HH:mm          (minute granularity)
//   - list/var/activity responses: dd/MM/yyyy HH:mm:ss.SSS
//   - process-key catalog: yyyy-MM-dd HH:mm:ss
//
// dayjs('29/07/2026 09:43:57.120') is Invalid Date without customParseFormat,
// which ships inside the existing dayjs dependency. This is the app's first
// dayjs.extend, done once here at module scope.

import dayjs, { type Dayjs } from 'dayjs'
import customParseFormat from 'dayjs/plugin/customParseFormat'

dayjs.extend(customParseFormat)

export const SYMPHONY_DATE_FORMAT = 'DD/MM/YYYY HH:mm'
export const SYMPHONY_TIMESTAMP_FORMAT = 'DD/MM/YYYY HH:mm:ss.SSS'
export const SYMPHONY_CATALOG_FORMAT = 'YYYY-MM-DD HH:mm:ss'

const PARSE_FORMATS = [SYMPHONY_TIMESTAMP_FORMAT, SYMPHONY_DATE_FORMAT, SYMPHONY_CATALOG_FORMAT]

/** Returns null rather than an Invalid Date so callers can branch cheaply. */
export function parseSymphonyTimestamp(value: string | null | undefined): Dayjs | null {
  if (!value) {
    return null
  }
  for (const format of PARSE_FORMATS) {
    const parsed = dayjs(value, format, true)
    if (parsed.isValid()) {
      return parsed
    }
  }
  const loose = dayjs(value)
  return loose.isValid() ? loose : null
}

/** Never renders "Invalid Date" — echoes the raw string when parsing fails. */
export function formatSymphonyTimestamp(
  value: string | null | undefined,
  format: string = 'D/M/YY HH:mm:ss'
): string {
  if (!value) {
    return '—'
  }
  const parsed = parseSymphonyTimestamp(value)
  return parsed ? parsed.format(format) : value
}

/** Sort key. Unparseable values sort last regardless of direction's caller. */
export function symphonyTimestampValue(value: string | null | undefined): number {
  return parseSymphonyTimestamp(value)?.valueOf() ?? Number.NEGATIVE_INFINITY
}

/**
 * Mantine 8 date inputs hold `string | null`; the filter state keeps that shape
 * so it stays JSON-serializable and can be snapshotted verbatim into a
 * deep-search job. This is the one-way conversion at query-build time.
 */
export function toSymphonyDateParam(value: string | null | undefined): string | undefined {
  if (!value) {
    return undefined
  }
  const parsed = dayjs(value)
  return parsed.isValid() ? parsed.format(SYMPHONY_DATE_FORMAT) : undefined
}

/**
 * Inverse of toSymphonyDateParam: turns a stored `dd/MM/yyyy HH:mm` API string
 * back into the format Mantine's date inputs hold, so a persisted deep-search
 * filter can be loaded into the shared filter fields for editing.
 */
export function fromSymphonyDateParam(value: string | null | undefined): string | null {
  const parsed = parseSymphonyTimestamp(value)
  return parsed ? parsed.format('YYYY-MM-DD HH:mm:ss') : null
}

/** `now`, truncated to the minute, in the request-param format. */
export function nowAsSymphonyDateParam(): string {
  return dayjs().startOf('minute').format(SYMPHONY_DATE_FORMAT)
}

export function formatDuration(ms: number | string | null | undefined): string {
  const value = typeof ms === 'string' ? Number(ms) : ms
  if (value == null || Number.isNaN(value)) {
    return '—'
  }
  if (value < 1000) {
    return `${value}ms`
  }
  if (value < 60_000) {
    return `${(value / 1000).toFixed(1)}s`
  }
  const minutes = Math.floor(value / 60_000)
  const seconds = Math.floor((value % 60_000) / 1000)
  return `${minutes}m ${String(seconds).padStart(2, '0')}s`
}
