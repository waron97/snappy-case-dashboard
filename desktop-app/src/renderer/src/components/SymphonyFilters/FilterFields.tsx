import { Checkbox, Grid, Group, Stack, TextInput } from '@mantine/core'
import { DateTimePicker } from '@mantine/dates'
import ProcessKeySelect from '@/components/SymphonyFilters/ProcessKeySelect'
import { ALL_STATUSES, type SymphonyFilterState } from '@/components/SymphonyFilters/types'
import type { SymphonyRequestStatus } from '@/lib/symphony-api'

const STATUS_LABELS: Record<SymphonyRequestStatus, string> = {
  CANCELLED: 'Cancelled',
  NEW: 'New',
  COMPLETED: 'Completed',
  WORKING: 'Working',
  FAILED: 'Failed'
}

type Props = {
  value: SymphonyFilterState
  onChange: (next: SymphonyFilterState) => void
  disabled?: boolean
  /**
   * Show the single-record identity fields (request id, process instance id,
   * reference id, external key). Off for a deep-search sweep: those pin the
   * query to one request, which is the opposite of sweeping many, and if you
   * already have the id you'd open the request directly instead.
   */
  showIdentityFields?: boolean
}

/**
 * The request-list filter fields, with no card, buttons or apply semantics —
 * shared by the Symphony list's filter bar and a deep-search job's editable
 * request filter, so the two can't drift apart.
 */
export default function FilterFields({
  value,
  onChange,
  disabled,
  showIdentityFields = true
}: Props): React.JSX.Element {
  // -------------------------------------
  // Functions
  // -------------------------------------

  function patch(next: Partial<SymphonyFilterState>): void {
    onChange({ ...value, ...next })
  }

  return (
    <Stack gap="sm">
      <Grid gutter="sm">
        {showIdentityFields && (
          <>
            <Grid.Col span={{ base: 12, sm: 4 }}>
              <TextInput
                label="Request Id"
                disabled={disabled}
                value={value.requestId}
                onChange={(e) => patch({ requestId: e.currentTarget.value })}
              />
            </Grid.Col>
            <Grid.Col span={{ base: 12, sm: 4 }}>
              <TextInput
                label="Process Instance Id"
                disabled={disabled}
                value={value.processId}
                onChange={(e) => patch({ processId: e.currentTarget.value })}
              />
            </Grid.Col>
          </>
        )}
        <Grid.Col span={{ base: 12, sm: 4 }}>
          <ProcessKeySelect
            value={value.processKey}
            disabled={disabled}
            onChange={(processKey) => patch({ processKey })}
          />
        </Grid.Col>

        {showIdentityFields && (
          <>
            <Grid.Col span={{ base: 12, sm: 4 }}>
              <TextInput
                label="Reference Id"
                disabled={disabled}
                value={value.referenceId}
                onChange={(e) => patch({ referenceId: e.currentTarget.value })}
              />
            </Grid.Col>
            <Grid.Col span={{ base: 12, sm: 4 }}>
              <TextInput
                label="External Key"
                disabled={disabled}
                value={value.externalKey}
                onChange={(e) => patch({ externalKey: e.currentTarget.value })}
              />
            </Grid.Col>
            {/* Spacer so the two date pickers share a row of their own. */}
            <Grid.Col span={{ base: 0, sm: 4 }} />
          </>
        )}

        <Grid.Col span={{ base: 12, sm: 4 }}>
          <DateTimePicker
            label="Received Time Init"
            clearable
            disabled={disabled}
            value={value.startDate}
            onChange={(startDate) => patch({ startDate })}
          />
        </Grid.Col>
        <Grid.Col span={{ base: 12, sm: 4 }}>
          <DateTimePicker
            label="Received Time End"
            clearable
            disabled={disabled}
            value={value.endDate}
            onChange={(endDate) => patch({ endDate })}
          />
        </Grid.Col>
      </Grid>

      <Group gap="md" align="end">
        {/* Dead job is a state like the other five — the engine failed to execute
            a state due to malformation, rather than hitting a normal business
            error. It is a separate wire param though, and it stays OUTSIDE
            Checkbox.Group because that group drives every descendant Checkbox
            from its own `value` array and ignores `checked`, which left it stuck
            unchecked when it was nested. */}
        <Checkbox.Group
          label="Status"
          description={
            value.statuses.length === 0 && !value.deadJob ? 'none ticked = any state' : undefined
          }
          value={value.statuses}
          onChange={(statuses) => patch({ statuses: statuses as SymphonyRequestStatus[] })}
        >
          <Group gap="md" mt={4}>
            {ALL_STATUSES.map((status) => (
              <Checkbox
                key={status}
                value={status}
                disabled={disabled}
                label={STATUS_LABELS[status]}
              />
            ))}
          </Group>
        </Checkbox.Group>
        <Checkbox
          label="Dead Job"
          disabled={disabled}
          checked={value.deadJob}
          onChange={(e) => patch({ deadJob: e.currentTarget.checked })}
        />
      </Group>
    </Stack>
  )
}
