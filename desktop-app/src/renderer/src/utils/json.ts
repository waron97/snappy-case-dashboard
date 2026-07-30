// Best-effort JSON parsing for values that are frequently JSON-inside-a-string.
//
// Symphony variable values look like
//   '{"code":200,"body":"[{\\"active\\": true, \\"toponym_id\\": [605, \\"VIA\\"]}]"}'
// where the interesting part is a JSON document escaped into a string field.
// parseJsonDeep unwraps those so a JSON viewer can render the whole thing.

export type ParsedJson =
  { kind: 'json'; value: unknown; didUnwrap: boolean } | { kind: 'text'; value: string }

const MAX_UNWRAP_LENGTH = 2_000_000

function looksLikeJson(value: string): boolean {
  const trimmed = value.trimStart()
  return trimmed.startsWith('{') || trimmed.startsWith('[')
}

/** Re-parses string leaves that themselves look like JSON. Returns whether it
 *  changed anything so the UI can offer a raw/parsed toggle. */
function unwrap(value: unknown, depth: number, state: { didUnwrap: boolean }): unknown {
  if (depth <= 0) {
    return value
  }
  if (typeof value === 'string') {
    if (value.length > MAX_UNWRAP_LENGTH || !looksLikeJson(value)) {
      return value
    }
    try {
      const parsed = JSON.parse(value)
      state.didUnwrap = true
      return unwrap(parsed, depth - 1, state)
    } catch {
      return value
    }
  }
  if (Array.isArray(value)) {
    return value.map((item) => unwrap(item, depth, state))
  }
  if (value && typeof value === 'object') {
    const out: Record<string, unknown> = {}
    for (const [key, item] of Object.entries(value)) {
      out[key] = unwrap(item, depth, state)
    }
    return out
  }
  return value
}

export function parseJsonDeep(input: string, maxDepth: number = 3): ParsedJson {
  // Fast path: scalars ('true', '42', bare strings) are never worth parsing as
  // a tree, and this keeps the common case out of JSON.parse entirely.
  if (!looksLikeJson(input)) {
    return { kind: 'text', value: input }
  }

  let root: unknown
  try {
    root = JSON.parse(input)
  } catch {
    return { kind: 'text', value: input }
  }

  const state = { didUnwrap: false }
  const value = unwrap(root, maxDepth, state)
  return { kind: 'json', value, didUnwrap: state.didUnwrap }
}
