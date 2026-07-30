import { IconPlus, IconTrash } from '@tabler/icons-react'
import {
  ActionIcon,
  Button,
  Checkbox,
  Grid,
  Group,
  SegmentedControl,
  Select,
  Stack,
  Text,
  TextInput,
  Tooltip
} from '@mantine/core'
import { OPS } from '@/routes/SymphonyDeepSearch/ops'
import type {
  SweepClause,
  SweepClauseMode,
  SweepPredicate,
  SweepStringOp
} from '@/lib/symphonyDeepSearch'

type Props = {
  value: SweepPredicate
  onChange: (next: SweepPredicate) => void
  disabled?: boolean
}

/** Unique within one predicate. Derived from existing ids rather than random, so
 *  a re-render can never change a row's key and blur the focused input. */
function nextClauseId(clauses: SweepClause[]): string {
  const taken = new Set(clauses.map((c) => c.id))
  let n = clauses.length
  while (taken.has(`clause-${n}`)) {
    n++
  }
  return `clause-${n}`
}

function emptyClause(id: string): SweepClause {
  return { id, name: { op: 'contains', value: '' }, value: { op: 'contains', value: '' } }
}

/**
 * Repeatable variable conditions.
 *
 * Each row is one clause whose name and value must hit the SAME variable; the
 * mode control decides how rows combine across a process instance's whole
 * variable set. That distinction is the easy thing to get wrong, so it is stated
 * in words under the rows rather than left implied.
 */
export default function ClauseEditor({ value, onChange, disabled }: Props): React.JSX.Element {
  // -------------------------------------
  // Functions
  // -------------------------------------

  function patchSide(
    index: number,
    side: 'name' | 'value',
    patch: Partial<{ op: SweepStringOp; value: string }>
  ): void {
    const existing = value.clauses[index][side] ?? { op: 'contains' as SweepStringOp, value: '' }
    const next = { ...existing, ...patch }
    onChange({
      ...value,
      clauses: value.clauses.map((c, i) => (i === index ? { ...c, [side]: next } : c))
    })
  }

  function addClause(): void {
    onChange({ ...value, clauses: [...value.clauses, emptyClause(nextClauseId(value.clauses))] })
  }

  function removeClause(index: number): void {
    onChange({ ...value, clauses: value.clauses.filter((_, i) => i !== index) })
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const multiple = value.clauses.length > 1

  return (
    <Stack gap="sm">
      {value.clauses.length === 0 && (
        <Text size="sm" c="dimmed">
          No conditions yet — add one to say what to look for inside the variables.
        </Text>
      )}

      {value.clauses.map((clause, index) => (
        <Grid key={clause.id} gutter="xs" align="end">
          <Grid.Col span={{ base: 12, sm: 3 }}>
            <Select
              label={index === 0 ? 'Variable name' : undefined}
              data={OPS}
              disabled={disabled}
              allowDeselect={false}
              value={clause.name?.op ?? 'contains'}
              onChange={(op) =>
                patchSide(index, 'name', { op: (op as SweepStringOp) ?? 'contains' })
              }
            />
          </Grid.Col>
          <Grid.Col span={{ base: 12, sm: 3 }}>
            <TextInput
              label={index === 0 ? ' ' : undefined}
              placeholder="callTaskBody"
              disabled={disabled}
              value={clause.name?.value ?? ''}
              onChange={(e) => patchSide(index, 'name', { value: e.currentTarget.value })}
            />
          </Grid.Col>
          <Grid.Col span={{ base: 12, sm: 2 }}>
            <Select
              label={index === 0 ? 'Variable value' : undefined}
              data={OPS}
              disabled={disabled}
              allowDeselect={false}
              value={clause.value?.op ?? 'contains'}
              onChange={(op) =>
                patchSide(index, 'value', { op: (op as SweepStringOp) ?? 'contains' })
              }
            />
          </Grid.Col>
          <Grid.Col span={{ base: 10, sm: 3 }}>
            <TextInput
              label={index === 0 ? ' ' : undefined}
              placeholder="e1501e9c-cd1b-461"
              disabled={disabled}
              value={clause.value?.value ?? ''}
              onChange={(e) => patchSide(index, 'value', { value: e.currentTarget.value })}
            />
          </Grid.Col>
          <Grid.Col span={{ base: 2, sm: 1 }}>
            <Tooltip label="Remove this condition">
              <ActionIcon
                variant="subtle"
                color="red"
                disabled={disabled}
                onClick={() => removeClause(index)}
              >
                <IconTrash size={16} />
              </ActionIcon>
            </Tooltip>
          </Grid.Col>
        </Grid>
      ))}

      <Group justify="space-between" align="center">
        <Group gap="lg" align="center">
          <Button
            size="xs"
            variant="light"
            leftSection={<IconPlus size={14} />}
            disabled={disabled}
            onClick={addClause}
          >
            Add condition
          </Button>
          <Checkbox
            size="xs"
            label="Case sensitive"
            disabled={disabled}
            checked={value.caseSensitive}
            onChange={(e) => onChange({ ...value, caseSensitive: e.currentTarget.checked })}
          />
        </Group>
        {multiple && (
          <Group gap="xs" align="center">
            <Text size="xs" c="dimmed">
              Match
            </Text>
            <SegmentedControl
              size="xs"
              disabled={disabled}
              value={value.mode}
              onChange={(mode) => onChange({ ...value, mode: mode as SweepClauseMode })}
              data={[
                { value: 'all', label: 'all conditions' },
                { value: 'any', label: 'any condition' }
              ]}
            />
          </Group>
        )}
      </Group>

      <Text size="xs" c="dimmed">
        {multiple
          ? value.mode === 'all'
            ? 'A process matches when EVERY condition is met — each may be met by a different variable.'
            : 'A process matches when AT LEAST ONE condition is met.'
          : 'Within one condition, the name and value must match the same variable.'}
      </Text>
    </Stack>
  )
}
