import { useEffect, useRef, useState } from 'react'
import { Badge, Grid, Group, MultiSelect, Switch, Text, TextInput } from '@mantine/core'
import { useDebouncedValue } from '@mantine/hooks'
import type { SortKey, VariableFilter } from '@/components/SymphonyVariables/filterTypes'

type Props = {
  availableTypes: string[]
  onChange: (filter: VariableFilter) => void
}

/**
 * Owns the text-input state locally and only pushes debounced values upward.
 *
 * This is a performance boundary, not just tidiness: the parent renders a table
 * of every variable (170+ rows, each with several Mantine components). Holding
 * the query text in the parent meant every keystroke re-rendered that whole
 * table, so typing lagged ~200ms per character even though the *filtering* was
 * already debounced. Keeping the text here means a keystroke re-renders only
 * these inputs, and the table re-renders once the debounce settles.
 */
export default function VariableFilterBar({ availableTypes, onChange }: Props): React.JSX.Element {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [name, setName] = useState('')
  const [value, setValue] = useState('')
  const [types, setTypes] = useState<string[]>([])
  const [caseSensitive, setCaseSensitive] = useState(false)
  const [sortKey, setSortKey] = useState<SortKey>('name')

  const [debouncedName] = useDebouncedValue(name, 250)
  // Longer: this one scans every value, which is megabytes in total.
  const [debouncedValue] = useDebouncedValue(value, 350)

  // Ref'd so the push effect below doesn't re-fire just because the parent
  // re-rendered and handed us a new function identity.
  const onChangeRef = useRef(onChange)

  // -------------------------------------
  // Effects
  // -------------------------------------

  useEffect(() => {
    onChangeRef.current = onChange
  }, [onChange])

  useEffect(() => {
    onChangeRef.current({
      name: debouncedName,
      value: debouncedValue,
      types,
      caseSensitive,
      sortKey
    })
  }, [debouncedName, debouncedValue, types, caseSensitive, sortKey])

  const pending = name !== debouncedName || value !== debouncedValue

  return (
    <>
      <Grid gutter="xs">
        <Grid.Col span={{ base: 12, sm: 4 }}>
          <TextInput
            label="Name contains"
            placeholder="callTaskBody"
            value={name}
            onChange={(e) => setName(e.currentTarget.value)}
          />
        </Grid.Col>
        <Grid.Col span={{ base: 12, sm: 4 }}>
          <TextInput
            label="Value contains"
            placeholder="e1501e9c-cd1b-461"
            value={value}
            onChange={(e) => setValue(e.currentTarget.value)}
          />
        </Grid.Col>
        <Grid.Col span={{ base: 12, sm: 4 }}>
          <MultiSelect
            label="Type"
            placeholder={types.length ? undefined : 'Any'}
            data={availableTypes}
            value={types}
            onChange={setTypes}
            clearable
            searchable
          />
        </Grid.Col>
      </Grid>

      <Group gap="lg">
        <Switch
          size="xs"
          label="Case sensitive"
          checked={caseSensitive}
          onChange={(e) => setCaseSensitive(e.currentTarget.checked)}
        />
        <Group gap="xs">
          <Text size="xs" c="dimmed">
            Sort
          </Text>
          {(['name', 'date', 'size'] as SortKey[]).map((key) => (
            <Badge
              key={key}
              variant={sortKey === key ? 'filled' : 'default'}
              style={{ cursor: 'pointer' }}
              onClick={() => setSortKey(key)}
            >
              {key}
            </Badge>
          ))}
        </Group>
        {pending && (
          <Text size="xs" c="dimmed">
            filtering…
          </Text>
        )}
      </Group>
    </>
  )
}
