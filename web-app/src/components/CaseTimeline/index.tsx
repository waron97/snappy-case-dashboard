'use client';

import dayjs from 'dayjs';
import { IconArrowRight } from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import { Center, Loader, Text, Timeline } from '@mantine/core';
import { odooSearchRead, OneToMany } from '../../../app/api';

type Props = {
  caseId: number;
};

type CaseHistory = {
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

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: caseHistory, isLoading } = useQuery<CaseHistory[]>({
    queryKey: ['case-history', { caseId }],
    enabled: !!caseId,
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase.history',
        [['ticket_id', '=', caseId]],

        ['active_phase_id', 'phase_result_id', 'error_message', 'date', 'phase_id'],
        undefined,
        undefined,
        'date asc'
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

  if (isLoading) {
    return (
      <Center>
        <Loader />
      </Center>
    );
  }

  return (
    <Timeline>
      {caseHistory
        ?.filter((historyItem) => historyItem.phase_id && historyItem.phase_result_id)
        ?.map((historyItem) => {
          return (
            <Timeline.Item title="Case avanzato">
              <Text c="dimmed" size="sm">
                {historyItem.active_phase_id[1]}
              </Text>
              <Text c="dimmed" size="sm">
                {historyItem.phase_result_id[1]}
              </Text>
              <Text size="xs" mt={4}>
                {dayjs(historyItem.date).format('DD/MM/YY HH:mm')}
              </Text>
            </Timeline.Item>
          );
        })}
    </Timeline>
  );
}
