import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { Box, Button, LoadingOverlay, Stack, Table } from '@mantine/core'
import { odooSearchRead, OneToMany } from '@/lib/odoo-api'
import RelationLink from '../RelationLink'

type Props = {
  caseId: number
  pointIds: number[]
}

type ServicePoint = {
  id: number
  code: string
  pod_id?: OneToMany
  pdr_id?: OneToMany
  idr_code?: string
  state: string
  supply_start_date: string
  supply_end_date?: string
  commodity: string
}

export default function CaseServicePoints({ caseId, pointIds }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [isShowAll, setIsShowAll] = useState(false)

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: points, isLoading } = useQuery<ServicePoint[]>({
    queryKey: ['case-service-points', caseId, { isShowAll }],
    refetchInterval: 30 * 1000,
    enabled: !!caseId && pointIds?.length > 0,
    queryFn: () =>
      odooSearchRead(
        'service.point',
        [['id', 'in', pointIds || []]],
        [
          'id',
          'code',
          'pod_id',
          'pdr_id',
          'idr_code',
          'supply_start_date',
          'supply_end_date',
          'state',
          'commodity'
        ],
        0,
        isShowAll ? undefined : 20,
        'supply_start_date desc'
      )
  })

  // -------------------------------------
  // Effects
  // -------------------------------------

  // -------------------------------------
  // Functions
  // -------------------------------------

  function renderSupply(h: any) {
    if (h.pod_id) {
      return <RelationLink pgId={h.pod_id[0]} model="res.partner.pod" name={h.pod_id[1]} />
    }
    if (h.pdr_id) {
      return <RelationLink pgId={h.pdr_id[0]} model="res.partner.pdr" name={h.pdr_id[1]} />
    }
    return h.idr_code
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  return (
    <Stack gap="sm" justify="space-between">
      <Box pos="relative" mih={isLoading ? 200 : undefined}>
        <LoadingOverlay visible={isLoading} />
        <Table>
          <Table.Thead>
            <Table.Tr>
              <Table.Th>PR code</Table.Th>
              <Table.Th>Commodity</Table.Th>
              <Table.Th>Supply</Table.Th>
              <Table.Th>State</Table.Th>
              <Table.Th>Supply start date</Table.Th>
              <Table.Th>Supply end date</Table.Th>
            </Table.Tr>
          </Table.Thead>
          <Table.Tbody>
            {points?.map((h) => {
              return (
                <Table.Tr key={h.id}>
                  <Table.Td>
                    <RelationLink name={h.code} pgId={h.id} model="service.point" />
                  </Table.Td>
                  <Table.Td>{h.commodity}</Table.Td>
                  <Table.Td>{renderSupply(h)}</Table.Td>
                  <Table.Td>{h.state}</Table.Td>
                  <Table.Td>{h.supply_start_date}</Table.Td>
                  <Table.Td>{h.supply_end_date}</Table.Td>
                </Table.Tr>
              )
            })}
          </Table.Tbody>
        </Table>
      </Box>
      {!isShowAll && points?.length === 20 && (
        <Button size="sm" onClick={() => setIsShowAll(true)}>
          Show all
        </Button>
      )}
    </Stack>
  )
}
