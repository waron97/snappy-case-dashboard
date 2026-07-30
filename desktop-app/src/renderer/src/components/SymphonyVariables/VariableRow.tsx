import { memo, useCallback } from 'react'
import { IconEye } from '@tabler/icons-react'
import { ActionIcon, Table, Text, Tooltip } from '@mantine/core'
import { formatSymphonyTimestamp } from '@/lib/symphonyDates'
import type { SymphonyVariable } from '@/lib/symphony-api'

const truncate = (value: string, max: number): string =>
  value.length > max ? `${value.slice(0, max)}…` : value

type Props = {
  variable: SymphonyVariable
  onSelect: (variable: SymphonyVariable) => void
}

/**
 * Memoized because the parent renders 170+ of these. Without it, any parent
 * re-render (opening the value modal, a filter settling) rebuilt every row's
 * subtree, which is what made typing in the filter feel laggy.
 *
 * `onSelect` must be referentially stable for the memo to hold — the parent
 * passes a useCallback'd setter.
 */
const VariableRow = memo(function VariableRow({ variable, onSelect }: Props): React.JSX.Element {
  const handleClick = useCallback(() => onSelect(variable), [onSelect, variable])

  return (
    <Table.Tr style={{ cursor: 'pointer' }} onClick={handleClick}>
      <Table.Td>
        <Text size="sm" ff="monospace">
          {variable.varName}
        </Text>
      </Table.Td>
      <Table.Td>
        <Text size="xs" c="dimmed">
          {variable.varType}
        </Text>
      </Table.Td>
      <Table.Td>
        <Text size="xs" c="dimmed">
          {formatSymphonyTimestamp(variable.varDate, 'D/M HH:mm:ss')}
        </Text>
      </Table.Td>
      <Table.Td>
        <Text size="xs" c="dimmed">
          {Number(variable.size).toLocaleString()}
        </Text>
      </Table.Td>
      <Table.Td>
        {/* varMin is the server's own ~103-char preview — cheaper than slicing a
            possibly 1MB varValue on every render. */}
        <Tooltip label="Click to open" openDelay={400}>
          <Text size="xs" c="dimmed" ff="monospace" style={{ whiteSpace: 'nowrap' }}>
            {truncate((variable.varMin || variable.varValue).replace(/\s+/g, ' '), 60)}
          </Text>
        </Tooltip>
      </Table.Td>
      <Table.Td>
        <ActionIcon variant="subtle" size="sm">
          <IconEye size={14} />
        </ActionIcon>
      </Table.Td>
    </Table.Tr>
  )
})

export default VariableRow
