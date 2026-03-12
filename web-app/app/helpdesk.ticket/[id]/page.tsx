'use client';

import { useParams } from 'next/navigation';
import { IconCode } from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import {
  Anchor,
  Button,
  Center,
  Container,
  Grid,
  Group,
  Loader,
  Space,
  Stack,
  Text,
  Title,
} from '@mantine/core';
import UiCard from '@/components/UiCard';
import { odooRead, OneToMany } from '../../api';

type BaseFields = {
  id: number;
  name: string;
  stage_id: OneToMany;
  ticket_type_id: OneToMany;
  triplet_subtype_id: OneToMany;
  triplet_type_id: OneToMany;
  workflow_id: OneToMany;
  parent_case_id: OneToMany;
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
          'parent_case_id',
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
    const item = (label: string, value: string, href?: string) => (
      <Stack gap={0}>
        <Text c="dimmed">{label}</Text>
        {href ? (
          <Anchor href={href} fw="bold">
            {value}
          </Anchor>
        ) : (
          <Text fw="bold">{value}</Text>
        )}
      </Stack>
    );

    const parent = values.parent_case_id;

    return (
      <UiCard title="Case Type">
        <Stack>
          {item('Stage', values.stage_id[1])}
          {item('Type', values.triplet_type_id[1])}
          {item('Subtype', values.triplet_subtype_id[1])}
          {item('Detail', values.ticket_type_id[1])}
          {item('Workflow', values.workflow_id?.[1])}
          {!!parent?.[0] && item('Parent', parent[1], `/helpdesk.ticket/${parent[0]}`)}
        </Stack>
      </UiCard>
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
      <Group gap="md" justify="space-between">
        <Title fz={28}>
          {caseBaseFields.name} (#{id})
        </Title>
        <Group gap="sm">
          <Anchor
            href={`https://odoo.sorgenia-test-02.symple.cloud/web#id=${id}&model=helpdesk.ticket&view_type=form`}
            target="_blank"
          >
            <Button bg="#714B67">ODOO</Button>
          </Anchor>
          <Button>
            <IconCode />
          </Button>
        </Group>
      </Group>

      <Space h={32} />

      <Grid gutter="md">
        <Grid.Col span={8}>
          <UiCard title="Active Phase" />
        </Grid.Col>
        <Grid.Col span={4}>
          <Stack gap="lg">
            {renderBasicInfo(caseBaseFields)}
            <UiCard title="Children" />
            <UiCard title="Logs" />
            <UiCard title="Staging Area" />
          </Stack>
        </Grid.Col>
      </Grid>
    </Container>
  );
}
