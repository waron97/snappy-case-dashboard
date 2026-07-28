import dayjs from 'dayjs'
import { useState } from 'react'
import { odooRead, odooSearchRead } from '@/lib/odoo-api'
import { IconEye } from '@tabler/icons-react'
import { useQuery } from '@tanstack/react-query'
import { Badge, Button, LoadingOverlay, Table, Text } from '@mantine/core'
import RipLogModal from '@/components/RipLogModal'
import UiCard from '@/components/UiCard'

type Props = {
  id: number
}

type RipLog = {
  id: number
  method: string
  status: number
  create_date: string
}

export default function MfaRecentCalls({ id }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [selectedId, setSelectedId] = useState<number | null>(null)

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: mfa } = useQuery({
    queryKey: ['mfa', id, 'endpoint-base'],
    queryFn: () => odooRead('rip.model.function.access', [id], ['name', 'model_name'])
  })

  const mfaRecord = mfa?.[0]
  const endpoint = mfaRecord ? `${mfaRecord.model_name}/${mfaRecord.name}` : undefined

  const { data: logs, isLoading } = useQuery({
    queryKey: ['mfa', id, 'recent-calls', endpoint],
    queryFn: () =>
      odooSearchRead(
        'rip.request.log',
        [['endpoint', 'ilike', endpoint!]],
        ['id', 'method', 'status', 'create_date'],
        0,
        10,
        'create_date DESC'
      ),
    enabled: !!endpoint
  })

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const rows = (logs ?? []).map((log: RipLog) => (
    <Table.Tr key={log.id}>
      <Table.Td>{log.method}</Table.Td>
      <Table.Td>
        <Badge color={log.status >= 200 && log.status < 300 ? 'green' : 'red'}>{log.status}</Badge>
      </Table.Td>
      <Table.Td>
        <Text size="xs">{dayjs(log.create_date).format('D/M/YY HH:mm')}</Text>
      </Table.Td>
      <Table.Td>
        <Button size="xs" onClick={() => setSelectedId(log.id)}>
          <IconEye size={16} />
        </Button>
      </Table.Td>
    </Table.Tr>
  ))

  // -------------------------------------

  return (
    <>
      <UiCard title="Recent Calls">
        <div style={{ position: 'relative', minHeight: 60 }}>
          <LoadingOverlay visible={isLoading} />
          <Table striped highlightOnHover>
            <Table.Thead>
              <Table.Tr>
                <Table.Th>Method</Table.Th>
                <Table.Th>Status</Table.Th>
                <Table.Th>Date</Table.Th>
                <Table.Th />
              </Table.Tr>
            </Table.Thead>
            <Table.Tbody>{rows}</Table.Tbody>
          </Table>
        </div>
      </UiCard>

      <RipLogModal id={selectedId} onClose={() => setSelectedId(null)} />
    </>
  )
}
