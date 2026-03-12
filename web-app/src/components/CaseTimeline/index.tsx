'use client';

import dayjs from 'dayjs';
import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { Box, Button, LoadingOverlay, Stack, Table } from '@mantine/core';
import { odooSearchRead, OneToMany } from '../../../app/api';

type Props = {
  caseId: number;
};

type CaseHistory = {
  id: number;
  active_phase_id: OneToMany;
  phase_result_id: OneToMany;
  phase_id: OneToMany;
  error_message?: string;
  date: string;
};

export default function CaseTimeline({ caseId }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [isShowAll, setIsShowAll] = useState(false);

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: caseHistory, isLoading } = useQuery<CaseHistory[]>({
    queryKey: ['case-history', caseId, { isShowAll }],
    refetchInterval: 30 * 1000,
    enabled: !!caseId,
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase.history',
        [['ticket_id', '=', caseId]],
        ['active_phase_id', 'phase_result_id', 'error_message', 'date', 'phase_id'],
        0,
        isShowAll ? undefined : 20,
        'date desc'
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
      <Box pos="relative" mih={200}>
        <LoadingOverlay visible={isLoading} />
        <Table>
          <Table.Thead>
            <Table.Tr>
              <Table.Th>Timestamp</Table.Th>
              <Table.Th>Phase</Table.Th>
              <Table.Th>Result</Table.Th>
              <Table.Th>Error message</Table.Th>
            </Table.Tr>
          </Table.Thead>
          <Table.Tbody>
            {caseHistory?.map((h) => {
              return (
                <Table.Tr key={h.id}>
                  <Table.Td>{dayjs(h.date).format('DD/MM HH:mm')}</Table.Td>
                  <Table.Td>{h.phase_id[1]}</Table.Td>
                  <Table.Td>{h.phase_result_id?.[1]}</Table.Td>
                  <Table.Td>{h.error_message}</Table.Td>
                </Table.Tr>
              );
            })}
          </Table.Tbody>
        </Table>
      </Box>
      {!isShowAll && caseHistory?.length === 20 && (
        <Button size="sm" onClick={() => setIsShowAll(true)}>
          Show all
        </Button>
      )}
    </Stack>
  );
}
