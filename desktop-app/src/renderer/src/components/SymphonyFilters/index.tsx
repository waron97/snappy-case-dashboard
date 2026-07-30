import { useState } from 'react'
import { IconRefresh, IconSearch } from '@tabler/icons-react'
import { ActionIcon, Button, Group, Stack, Text, Tooltip } from '@mantine/core'
import UiCard from '@/components/UiCard'
import FilterFields from '@/components/SymphonyFilters/FilterFields'
import {
  EMPTY_SYMPHONY_FILTERS,
  type SymphonyFilterState
} from '@/components/SymphonyFilters/types'
import { useSymphonyProcessKeys } from '@/lib/symphonyProcessKeys'
import { formatSymphonyTimestamp } from '@/lib/symphonyDates'

type Props = {
  value: SymphonyFilterState
  onApply: (next: SymphonyFilterState) => void
  onDeepSearch?: (draft: SymphonyFilterState) => void
}

export default function SymphonyFilters({
  value,
  onApply,
  onDeepSearch
}: Props): React.JSX.Element {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  // Local draft so typing doesn't refire the query on every keystroke — the
  // request list is a multi-hundred-row server query, not a client filter.
  const [draft, setDraft] = useState<SymphonyFilterState>(value)
  const { fetchedAt, isSweeping, refresh, error } = useSymphonyProcessKeys()

  // -------------------------------------
  // Functions
  // -------------------------------------

  function handleReset(): void {
    setDraft(EMPTY_SYMPHONY_FILTERS)
    onApply(EMPTY_SYMPHONY_FILTERS)
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const catalogHint = isSweeping
    ? 'Loading process catalog…'
    : error
      ? 'Process catalog unavailable'
      : fetchedAt
        ? `Catalog: ${formatSymphonyTimestamp(fetchedAt, 'D/M/YY HH:mm')}`
        : 'Process catalog not loaded'

  return (
    <UiCard
      title="Filters"
      rightElement={
        <Group gap="xs">
          <Text size="xs" c={error ? 'red' : 'dimmed'}>
            {catalogHint}
          </Text>
          <Tooltip label="Reload the process catalog">
            <ActionIcon
              variant="subtle"
              color="gray"
              size="sm"
              loading={isSweeping}
              onClick={refresh}
            >
              <IconRefresh size={14} />
            </ActionIcon>
          </Tooltip>
        </Group>
      }
    >
      <Stack gap="sm">
        <FilterFields value={draft} onChange={setDraft} />

        <Group justify="end" gap="sm">
          {onDeepSearch && (
            <Tooltip label="Sweep these requests and search inside their variables">
              <Button
                variant="light"
                leftSection={<IconSearch size={14} />}
                onClick={() => onDeepSearch(draft)}
              >
                Deep search
              </Button>
            </Tooltip>
          )}
          <Button variant="subtle" color="gray" onClick={handleReset}>
            Reset filters
          </Button>
          <Button onClick={() => onApply(draft)}>Apply</Button>
        </Group>
      </Stack>
    </UiCard>
  )
}
