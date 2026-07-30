import { useCallback, useMemo, useState } from 'react'
import { IconAlertTriangle } from '@tabler/icons-react'
import { Alert, Center, Loader, ScrollArea, Stack, Table, Text } from '@mantine/core'
import UiCard from '@/components/UiCard'
import SymphonyVariableValueModal from '@/components/SymphonyVariableValueModal'
import VariableFilterBar from '@/components/SymphonyVariables/FilterBar'
import {
  EMPTY_VARIABLE_FILTER,
  type VariableFilter
} from '@/components/SymphonyVariables/filterTypes'
import VariableRow from '@/components/SymphonyVariables/VariableRow'
import { useSymphonyVariables } from '@/lib/symphonyDetail'
import { symphonyTimestampValue } from '@/lib/symphonyDates'
import type { SymphonyVariable } from '@/lib/symphony-api'

type Props = {
  processInstanceId: string | null
  isActive: boolean
  /** The caller is still resolving which process instance to ask about, so an
   *  empty result here means "not known yet", not "none exist". */
  pending?: boolean
}

export default function SymphonyVariables({
  processInstanceId,
  isActive,
  pending = false
}: Props): React.JSX.Element {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  // Only the settled filter lives here — the input text stays inside
  // VariableFilterBar so a keystroke doesn't re-render this table.
  const [filter, setFilter] = useState<VariableFilter>(EMPTY_VARIABLE_FILTER)
  const [selected, setSelected] = useState<SymphonyVariable | null>(null)

  // Stable identity so the memoized rows actually stay memoized.
  const handleSelect = useCallback((variable: SymphonyVariable) => setSelected(variable), [])
  const handleClose = useCallback(() => setSelected(null), [])

  // -------------------------------------
  // Queries
  // -------------------------------------

  const {
    data: variables,
    isLoading,
    isError,
    error
  } = useSymphonyVariables(processInstanceId, isActive)

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // Memoized so the empty-array fallback doesn't churn the filter memo below.
  const all = useMemo(() => variables ?? [], [variables])

  const availableTypes = useMemo(() => Array.from(new Set(all.map((v) => v.varType))).sort(), [all])

  // One pass over the COMPLETE set — never over a page. An indexOf across a few
  // megabytes is sub-millisecond, so no indexing is warranted.
  const filtered = useMemo(() => {
    const { caseSensitive, types, sortKey } = filter
    const name = caseSensitive ? filter.name : filter.name.toLowerCase()
    const value = caseSensitive ? filter.value : filter.value.toLowerCase()

    const matches = all.filter((v) => {
      if (types.length > 0 && !types.includes(v.varType)) return false
      if (name) {
        const haystack = caseSensitive ? v.varName : v.varName.toLowerCase()
        if (!haystack.includes(name)) return false
      }
      if (value) {
        const haystack = caseSensitive ? v.varValue : v.varValue.toLowerCase()
        if (!haystack.includes(value)) return false
      }
      return true
    })

    const sorted = [...matches]
    if (sortKey === 'name') {
      sorted.sort((a, b) => a.varName.localeCompare(b.varName))
    } else if (sortKey === 'date') {
      sorted.sort((a, b) => symphonyTimestampValue(b.varDate) - symphonyTimestampValue(a.varDate))
    } else {
      sorted.sort((a, b) => Number(b.size) - Number(a.size))
    }
    return sorted
  }, [all, filter])

  // Built once per filter change rather than on every parent render (opening the
  // value modal would otherwise rebuild all ~170 rows).
  const rows = useMemo(
    () =>
      filtered.map((variable) => (
        <VariableRow
          key={`${variable.varName}:${variable.varDate}`}
          variable={variable}
          onSelect={handleSelect}
        />
      )),
    [filtered, handleSelect]
  )

  return (
    <UiCard
      title="Variables"
      rightElement={
        <Text size="xs" c="dimmed">
          {filtered.length === all.length
            ? `${all.length} variables`
            : `${filtered.length} of ${all.length} variables`}
        </Text>
      }
    >
      <Stack gap="sm">
        <VariableFilterBar availableTypes={availableTypes} onChange={setFilter} />

        {isError && (
          <Alert color="red" icon={<IconAlertTriangle size={16} />}>
            {(error as Error)?.message ?? 'Failed to load variables'}
          </Alert>
        )}

        {(isLoading || pending) && (
          <Center py="lg">
            <Loader size="sm" />
          </Center>
        )}

        {!isLoading && !pending && !isError && (
          <ScrollArea.Autosize mah={700}>
            <Table striped highlightOnHover stickyHeader>
              <Table.Thead>
                <Table.Tr>
                  <Table.Th>Name</Table.Th>
                  <Table.Th w={110}>Type</Table.Th>
                  <Table.Th w={130}>Date</Table.Th>
                  <Table.Th w={80}>Size</Table.Th>
                  <Table.Th>Preview</Table.Th>
                  <Table.Th w={40} />
                </Table.Tr>
              </Table.Thead>
              <Table.Tbody>{rows}</Table.Tbody>
            </Table>

            {filtered.length === 0 && (
              <Center py="lg">
                <Text size="sm" c="dimmed">
                  {all.length === 0 ? 'No variables recorded' : 'No variables match these filters'}
                </Text>
              </Center>
            )}
          </ScrollArea.Autosize>
        )}
      </Stack>

      <SymphonyVariableValueModal variable={selected} onClose={handleClose} />
    </UiCard>
  )
}
