'use client';

import dayjs from 'dayjs';
import { useMemo, useState } from 'react';
import dynamic from 'next/dynamic';
import { IconEye } from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import { Box, Button, LoadingOverlay, Modal, Stack, Table } from '@mantine/core';
import { odooRead, odooSearchRead } from '../../../app/api';

const ReactJson = dynamic(() => import('react-json-view'), { ssr: false });

type Props = { caseId: number };

export default function CaseIntegrationHistory({ caseId }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [isShowAll, setIsShowAll] = useState(false);
  const [selected, setSelected] = useState<number | null>(null);

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: logs, isLoading: logsLoading } = useQuery<
    { id: number; name: string; create_date: string }[]
  >({
    queryKey: ['integration-history', { caseId, isShowAll }],
    queryFn: () =>
      odooSearchRead(
        'case.integration.history',
        [['ticket_id', '=', caseId]],
        ['create_date', 'name'],
        0,
        isShowAll ? undefined : 5,
        'create_date desc'
      ),
  });

  const { data: logDetail, isLoading: detailLoading } = useQuery<{ id: number; payload: string }[]>(
    {
      queryKey: ['integration-history', selected],
      enabled: !!selected,
      queryFn: () => odooRead('case.integration.history', [selected!], ['payload']),
    }
  );

  const logJson = useMemo(() => {
    if (!logDetail?.length) {
      return {};
    }
    const { payload: message } = logDetail[0];
    try {
      return JSON.parse(message);
    } catch {
      return { content: message };
    }
  }, [logDetail?.[0]?.payload]);

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
                  <Table.Td>{log.name}</Table.Td>
                  <Table.Td>
                    <Button size="xs" onClick={() => setSelected(log.id)}>
                      <IconEye size={16} />
                    </Button>
                  </Table.Td>
                </Table.Tr>
              );
            })}
          </Table.Tbody>
        </Table>
      </Box>
      {!isShowAll && logs?.length === 5 && (
        <Button size="sm" onClick={() => setIsShowAll(true)}>
          Show all
        </Button>
      )}
      <Modal opened={!!selected} onClose={() => setSelected(null)} size="xl">
        <Box pos="relative" mih={100}>
          <LoadingOverlay visible={detailLoading} />
          <ReactJson src={logJson} theme="monokai" />
        </Box>
      </Modal>
    </Stack>
  );
}
