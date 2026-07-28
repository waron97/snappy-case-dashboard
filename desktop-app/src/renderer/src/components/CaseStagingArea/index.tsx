import dayjs from 'dayjs'
import { useMemo, useState } from 'react'
import SearchableJsonView, { SearchableJsonModal } from '@/components/SearchableJsonView'
import { IconEye } from '@tabler/icons-react'
import { useQuery } from '@tanstack/react-query'
import { Box, Button, LoadingOverlay, Stack, Table } from '@mantine/core'
import { odooRead, odooSearchRead } from '@/lib/odoo-api'

type Props = { caseId: number }

export default function CaseStagingArea({ caseId }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [selected, setSelected] = useState<number | null>(null)

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: logs, isLoading: logsLoading } = useQuery<
    { id: number; process_name: string; create_date: string }[]
  >({
    queryKey: ['staging-area', { caseId }],
    queryFn: () =>
      odooSearchRead(
        'symple.pb.process.data',
        [['res_id', '=', String(caseId)]],
        ['create_date', 'process_name'],
        0,
        undefined,
        'process_name asc'
      )
  })

  const { data: logDetail, isLoading: detailLoading } = useQuery<{ id: number; payload: string }[]>(
    {
      queryKey: ['staging-area', selected],
      refetchInterval: 15 * 1000,
      enabled: !!selected,
      queryFn: () => odooRead('symple.pb.process.data', [selected!], ['payload'])
    }
  )

  const logJson = useMemo(() => {
    if (!logDetail?.length) {
      return {}
    }
    const { payload: message } = logDetail[0]
    try {
      return JSON.parse(message)
    } catch {
      return { content: message }
    }
  }, [logDetail?.[0]?.payload])

  // -------------------------------------
  // Effects
  // -------------------------------------

  // -------------------------------------
  // Functions
  // -------------------------------------

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // -------------------------------------

  return (
    <Stack gap="sm">
      <Box pos="relative" mih={200}>
        <LoadingOverlay visible={logsLoading} />
        <Table>
          <Table.Thead>
            <Table.Tr>
              <Table.Th>Timestamp</Table.Th>
              <Table.Th>Name</Table.Th>
              <Table.Th />
            </Table.Tr>
          </Table.Thead>
          <Table.Tbody>
            {logs?.map((log) => {
              return (
                <Table.Tr key={log.id}>
                  <Table.Td>{dayjs(log.create_date).format('DD/MM HH:mm')}</Table.Td>
                  <Table.Td>{log.process_name}</Table.Td>
                  <Table.Td>
                    <Button size="xs" onClick={() => setSelected(log.id)}>
                      <IconEye size={16} />
                    </Button>
                  </Table.Td>
                </Table.Tr>
              )
            })}
          </Table.Tbody>
        </Table>
      </Box>
      <SearchableJsonModal
        opened={!!selected}
        onClose={() => setSelected(null)}
        loading={detailLoading}
      >
        <SearchableJsonView src={logJson} theme="monokai" />
      </SearchableJsonModal>
    </Stack>
  )
}
