import { Link } from 'react-router-dom'
import { IconAlertTriangle, IconEye } from '@tabler/icons-react'
import { ActionIcon, Alert, Badge, Center, Loader, Table, Text, Tooltip } from '@mantine/core'
import { NO_PROCESS_ID, tabPath } from '@/lib/useCaseTabs'
import {
  useCaseSymphonyProcesses,
  type CaseProcessOrigin
} from '@/components/CaseSymphonyProcesses/useCaseProcesses'

const ORIGIN_LABELS: Record<CaseProcessOrigin, { label: string; color: string; hint: string }> = {
  current: {
    label: 'current',
    color: 'blue',
    hint: "The case's current Symphonie long-running process id"
  },
  history: {
    label: 'previous',
    color: 'gray',
    hint: 'A value this case held before — archived when the field was overwritten'
  },
  wizard: { label: 'wizard', color: 'grape', hint: 'Recorded when a wizard completed' }
}

/** Wizard outcomes, per the selection on symple.pb.instance.key. */
function statusColor(status: string): string {
  if (status === 'SUCCESS') return 'green'
  if (status.includes('PARTIAL')) return 'yellow'
  if (status === 'CANCEL') return 'gray'
  return 'red'
}

type Props = {
  caseId: number
}

export default function CaseSymphonyProcesses({ caseId }: Props): React.JSX.Element {
  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data, isLoading, isError, error } = useCaseSymphonyProcesses(caseId)

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const rows = data ?? []

  if (isLoading) {
    return (
      <Center py="lg">
        <Loader size="sm" />
      </Center>
    )
  }

  if (isError) {
    return (
      <Alert color="red" icon={<IconAlertTriangle size={16} />}>
        {(error as Error)?.message ?? 'Could not load Symphony processes for this case'}
      </Alert>
    )
  }

  if (rows.length === 0) {
    return (
      <Center py="lg">
        <Text size="sm" c="dimmed">
          No Symphony processes recorded for this case.
        </Text>
      </Center>
    )
  }

  return (
    <Table striped highlightOnHover>
      <Table.Thead>
        <Table.Tr>
          <Table.Th w={100}>Origin</Table.Th>
          <Table.Th>Process</Table.Th>
          <Table.Th>Id</Table.Th>
          <Table.Th w={150}>Wizard result</Table.Th>
          <Table.Th w={50} />
        </Table.Tr>
      </Table.Thead>
      <Table.Tbody>
        {rows.map((row) => {
          const origin = ORIGIN_LABELS[row.origin]
          return (
            <Table.Tr key={`${row.origin}:${row.id}`}>
              <Table.Td>
                <Tooltip label={origin.hint}>
                  <Badge size="sm" variant="light" color={origin.color}>
                    {origin.label}
                  </Badge>
                </Tooltip>
              </Table.Td>
              <Table.Td>
                <Text size="xs">{row.processName ?? '—'}</Text>
              </Table.Td>
              <Table.Td>
                <Text size="xs" ff="monospace">
                  {row.id}
                </Text>
              </Table.Td>
              <Table.Td>
                {row.wizardStatus ? (
                  <Tooltip
                    label={
                      row.cancelReason
                        ? `${row.wizardStateCode ?? ''} — ${row.cancelReason}`
                        : (row.wizardStateCode ?? row.wizardStatus)
                    }
                  >
                    <Badge size="sm" variant="light" color={statusColor(row.wizardStatus)}>
                      {row.wizardStatus}
                    </Badge>
                  </Tooltip>
                ) : (
                  <Text size="xs" c="dimmed">
                    —
                  </Text>
                )}
              </Table.Td>
              <Table.Td>
                <Tooltip label="Open this process in a tab">
                  <ActionIcon
                    component={Link}
                    variant="subtle"
                    size="sm"
                    // Odoo stores a single id without recording whether it is a
                    // request id or a process-instance id, so the process
                    // instance stays unknown until the detail page resolves it.
                    to={tabPath({
                      kind: 'symphony-request',
                      requestId: row.id,
                      processId: NO_PROCESS_ID,
                      label: row.processName ?? row.id
                    })}
                  >
                    <IconEye size={14} />
                  </ActionIcon>
                </Tooltip>
              </Table.Td>
            </Table.Tr>
          )
        })}
      </Table.Tbody>
    </Table>
  )
}
