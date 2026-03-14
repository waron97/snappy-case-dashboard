import dayjs from 'dayjs';
import { useState } from 'react';
import Link from 'next/link';
import { useQuery } from '@tanstack/react-query';
import { Box, Button, LoadingOverlay, Stack, Table } from '@mantine/core';
import { odooSearchRead, OneToMany } from '../../../app/api';

type Props = { caseId: number; childIds: number[] };

type Child = {
  id: number;
  name: string;
  ticket_type_id: OneToMany;
  create_date: string;
  workflow_id: OneToMany;
  stage_id: OneToMany;
  triplet_active_phase_id: OneToMany;
};

export default function CaseChildren({ caseId, childIds }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [isShowAll, setIsShowAll] = useState(false);

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: children, isLoading } = useQuery<Child[]>({
    queryKey: ['case-children', caseId, { isShowAll }],
    enabled: !!caseId && childIds?.length > 0,
    queryFn: () =>
      odooSearchRead(
        'helpdesk.ticket',
        [['id', 'in', childIds || []]],
        [
          'id',
          'name',
          'ticket_type_id',
          'create_date',
          'ticket_type_id',
          'workflow_id',
          'triplet_active_phase_id',
        ],
        0,
        isShowAll ? undefined : 20,
        'create_date desc'
      ),
  });

  // -------------------------------------
  // Effects
  // -------------------------------------

  // -------------------------------------
  // Functions
  // -------------------------------------

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  return (
    <Stack gap="sm" justify="space-between">
      <Box pos="relative" mih={isLoading ? 200 : 0}>
        <LoadingOverlay visible={isLoading} />

        <Table>
          <Table.Thead>
            <Table.Tr>
              <Table.Td>Name</Table.Td>
              <Table.Td>Ticket type</Table.Td>
              <Table.Td>Workflow</Table.Td>
              <Table.Td>Phase</Table.Td>
              <Table.Td>Date</Table.Td>
            </Table.Tr>
          </Table.Thead>
          <Table.Tbody>
            {children?.map((child) => {
              return (
                <Table.Tr key={child.id}>
                  <Table.Td>
                    <Link href={`/helpdesk.ticket/${child.id}`}>{child.name}</Link>
                  </Table.Td>
                  <Table.Td>{child.ticket_type_id[1]}</Table.Td>
                  <Table.Td>{child.workflow_id?.[1]}</Table.Td>
                  <Table.Td>{child.triplet_active_phase_id?.[1]}</Table.Td>
                  <Table.Td>{dayjs(child.create_date).format('DD/MM HH:mm')}</Table.Td>
                </Table.Tr>
              );
            })}
          </Table.Tbody>
        </Table>
      </Box>
      {!isShowAll && children?.length === 20 && (
        <Button size="sm" onClick={() => setIsShowAll(true)}>
          Show all
        </Button>
      )}
    </Stack>
  );
}
