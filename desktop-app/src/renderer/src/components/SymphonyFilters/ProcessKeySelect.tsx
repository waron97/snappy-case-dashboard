import { Autocomplete, Loader, type ComboboxItem, type OptionsFilter } from '@mantine/core'
import { useDebouncedValue } from '@mantine/hooks'
import { useQuery } from '@tanstack/react-query'
import { searchProcessKeys, useSymphonyProcessKeys } from '@/lib/symphonyProcessKeys'

type Props = {
  value: string | null
  onChange: (value: string | null) => void
  disabled?: boolean
}

const MIN_SEARCH_LENGTH = 3

/**
 * Options already arrive prefix-stripped (the catalog stores the request-facing
 * key), but a user may still type the full definition name they know from the
 * BPMN editor — so matching also ignores these prefixes in the QUERY.
 */
const IGNORED_PREFIXES = ['B2WA_', 'B2W_']

function stripPrefix(name: string): string {
  const lower = name.toLowerCase()
  for (const prefix of IGNORED_PREFIXES) {
    if (lower.startsWith(prefix.toLowerCase())) {
      return name.slice(prefix.length)
    }
  }
  return name
}

/**
 * Matches on the raw name and on the prefix-stripped name, and ranks entries
 * whose (stripped) name *starts* with the query above mere substring hits — so
 * "activate" surfaces "B2WA_activate_sdd" before "…_reactivate_…".
 */
const processKeyFilter: OptionsFilter = ({ options, search, limit }) => {
  // Strip the prefix from the QUERY too, so pasting "B2WA_async_case_engine"
  // still finds the "async_case_engine" option.
  const query = stripPrefix(search.trim()).toLowerCase()
  if (!query) {
    return options.slice(0, limit)
  }

  const scored: { option: ComboboxItem; rank: number }[] = []
  for (const option of options) {
    // Groups are never produced here (data is a flat string[]), but skip them
    // rather than mis-handling them if that ever changes.
    if (!('value' in option)) {
      continue
    }
    const item = option as ComboboxItem
    const raw = item.label.toLowerCase()
    const stripped = stripPrefix(item.label).toLowerCase()

    if (stripped.startsWith(query) || raw.startsWith(query)) {
      scored.push({ option: item, rank: 0 })
    } else if (stripped.includes(query) || raw.includes(query)) {
      scored.push({ option: item, rank: 1 })
    }
  }

  return scored
    .sort((a, b) => a.rank - b.rank || a.option.label.localeCompare(b.option.label))
    .slice(0, limit)
    .map((s) => s.option)
}

/**
 * Suggests process keys instead of forcing a choice among them.
 *
 * An Autocomplete rather than a Select: even with both catalogs (deployed BPMN
 * definitions + process-builder wizards) the suggestion list is not a superset of
 * the keys that appear on requests — measured against a live sample it covered 50
 * of 54, the rest presumably coming from older BPMN versions or other spawners.
 * A strict Select would make those unfilterable, which is worse than the legacy
 * free-text box. So: suggestions, arbitrary values still accepted, and a hint
 * when the typed key isn't one we know about.
 */
export default function ProcessKeySelect({ value, onChange, disabled }: Props): React.JSX.Element {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  // Autocomplete's value doubles as the search text, so the server-side
  // fallback query is driven straight off it.
  const [debouncedSearch] = useDebouncedValue(value ?? '', 300)
  const { options, observedOptions, isCatalogReady, isSweeping } = useSymphonyProcessKeys()

  // -------------------------------------
  // Queries
  // -------------------------------------

  const remote = useQuery({
    queryKey: ['symphony', 'processKeySearch', debouncedSearch],
    queryFn: () => searchProcessKeys(debouncedSearch),
    enabled: !isCatalogReady && debouncedSearch.trim().length >= MIN_SEARCH_LENGTH,
    staleTime: 5 * 60 * 1000,
    retry: false
  })

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const remoteOptions = (remote.data ?? []).map((k) => k.name)
  // Observed keys come from real request rows, so they are always valid filter
  // values — and they cover what the definition catalogs cannot (a request started
  // against a BPMN version the `latestVersion=true` sweep excludes).
  const data = Array.from(
    new Set([
      ...(isCatalogReady ? options : remoteOptions),
      ...observedOptions,
      ...(value ? [value] : [])
    ])
  )

  const placeholder = isCatalogReady
    ? 'Any process'
    : isSweeping
      ? 'Loading catalog…'
      : 'Any process'

  const known = value != null && value !== '' && data.includes(value)

  return (
    <Autocomplete
      label="Process Key"
      placeholder={placeholder}
      data={data}
      value={value ?? ''}
      // Empty string means "no filter" to the caller, which models it as null.
      onChange={(next) => onChange(next === '' ? null : next)}
      disabled={disabled}
      limit={50}
      filter={processKeyFilter}
      description={
        value && isCatalogReady && !known
          ? 'Not in the known-process list — will still be sent as typed'
          : undefined
      }
      rightSection={isSweeping || remote.isFetching ? <Loader size="xs" /> : undefined}
    />
  )
}
