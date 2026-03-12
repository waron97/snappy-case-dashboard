'use client';

import { useParams } from 'next/navigation';
import { useQuery } from '@tanstack/react-query';
import {
  Center,
  Container,
  Grid,
  Group,
  Input,
  Loader,
  Space,
  Stack,
  Text,
  TextInput,
  Title,
} from '@mantine/core';
import CaseTimeline from '@/components/CaseTimeline';
import { odooRead, OneToMany } from '../../api';

type BaseFields = {
  id: number;
  name: string;
  stage_id: OneToMany;
  ticket_type_id: OneToMany;
  triplet_subtype_id: OneToMany;
  triplet_type_id: OneToMany;
  workflow_id: OneToMany;
};

export default function Ticket() {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const { id } = useParams();

  // -------------------------------------
  // Queries
  // -------------------------------------

  const {
    data: baseFields,
    isLoading: isBaseLoading,
    error,
  } = useQuery<BaseFields[]>({
    queryKey: ['case', 'base', id],
    queryFn: () =>
      odooRead(
        'helpdesk.ticket',
        [parseInt(String(id), 10)],
        [
          'name',
          'stage_id',
          'ticket_type_id',
          'workflow_id',
          'triplet_subtype_id',
          'triplet_type_id',
        ]
      ),
  });

  // -------------------------------------
  // Effects
  // -------------------------------------

  // -------------------------------------
  // Functions
  // -------------------------------------

  function renderTimeline(values: BaseFields) {}

  function renderBasicInfo(values: BaseFields) {
    const item = (label, value) => (
      <Group justify="space-between" gap={24}>
        <Text>{label}</Text>
        <Text fw="bold">{value}</Text>
      </Group>
    );

    return (
      <Stack>
        {item('Stage', values.stage_id[1])}
        {item('Type', values.triplet_type_id[1])}
        {item('Subtype', values.triplet_subtype_id[1])}
        {item('Detail', values.ticket_type_id[1])}
        {item('Workflow', values.workflow_id?.[1])}
      </Stack>
    );
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  if (isBaseLoading) {
    return (
      <Center py="xl">
        <Loader />
      </Center>
    );
  }

  const caseBaseFields = baseFields![0];

  if (!caseBaseFields || !caseBaseFields?.id || error) {
    return (
      <Container size="lg" py="xl">
        <Center py="xl">
          <Text c="red">
            Failed to load case: {error instanceof Error ? error.message : 'Unknown error'}
          </Text>
        </Center>
      </Container>
    );
  }

  // -------------------------------------

  return (
    <Container size="xl" py="md">
      <Title fz={28}>
        {caseBaseFields.name} (#{id})
      </Title>

      <Space h={32} />

      <Grid gutter="md">
        <Grid.Col span={3}>
          <Stack gap="lg">{renderBasicInfo(caseBaseFields)}</Stack>
        </Grid.Col>
        <Grid.Col span={4}></Grid.Col>
        <Grid.Col span={3}></Grid.Col>
        <Grid.Col span={2}>
          <CaseTimeline caseId={caseBaseFields.id} />
        </Grid.Col>
      </Grid>
    </Container>
  );
}
