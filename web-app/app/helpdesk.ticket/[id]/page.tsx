'use client';

import Link from 'next/link';
import { useParams } from 'next/navigation';
import { IconCode, ReactNode } from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import {
  Alert,
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
import CaseActivePhase from '@/components/CaseActivePhase';
import CaseIntegrationHistory from '@/components/CaseIntegrationHistory';
import CaseLogs from '@/components/CaseLogs';
import CaseMarketComm from '@/components/CaseMarketComm';
import CaseStagingArea from '@/components/CaseStagingArea';
import CaseTabs from '@/components/CaseTabs';
import RelationLink from '@/components/RelationLink';
import UiCard from '@/components/UiCard';
import { odooRead, OneToMany } from '../../api';

type BaseFields = {
  id: number;
  name: string;
  stage_id: OneToMany;
  ticket_type_id: OneToMany;
  triplet_subtype_id: OneToMany;
  triplet_type_id: OneToMany;
  error_message?: string;
  workflow_id: OneToMany;
  parent_case_id: OneToMany;
  child_case_ids: number[];
  market_comm_event_log_ids: number[];
  integration_history_ids: number[];
  customer_id: OneToMany;
  partner_id?: OneToMany;
  customer_code: string;
  service_point_ids: number[];
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
    queryKey: ['case', id, 'for-base-view'],
    queryFn: () =>
      odooRead(
        'helpdesk.ticket',
        [parseInt(String(id), 10)],
        [
          'name',
          'stage_id',
          'ticket_type_id',
          'error_message',
          'workflow_id',
          'triplet_subtype_id',
          'triplet_type_id',
          'parent_case_id',
          'child_case_ids',
          'market_comm_event_log_ids',
          'integration_history_ids',
          'customer_id',
          'partner_id',
          'customer_code',
          'service_point_ids',
        ]
      ),
  });

  // -------------------------------------
  // Effects
  // -------------------------------------

  // -------------------------------------
  // Functions
  // -------------------------------------

  function renderBasicInfo(values: BaseFields) {
    const item = (label: string, value: ReactNode, href?: string, wrapValue: boolean = true) => (
      <Grid.Col span={4}>
        <Stack gap={0}>
          <Text c="dimmed">{label}</Text>
          {href ? (
            <Anchor href={href} fw="bold">
              {value}
            </Anchor>
          ) : wrapValue ? (
            <Text fw="bold">{value}</Text>
          ) : (
            value
          )}
        </Stack>
      </Grid.Col>
    );

    const parent = values.parent_case_id;

    return (
      <UiCard title="Case Type">
        <Stack>
          <Grid>
            {item(
              'Type',
              <RelationLink
                name={values.triplet_type_id[1]}
                pgId={values.triplet_type_id[0]}
                model="symple.triplet.type"
              />,
              undefined,
              false
            )}
            {item(
              'Subtype',
              <RelationLink
                name={values.triplet_subtype_id[1]}
                pgId={values.triplet_subtype_id[0]}
                model="symple.triplet.subtype"
              />,
              undefined,
              false
            )}
            {item(
              'Detail',
              <RelationLink
                name={values.ticket_type_id[1]}
                pgId={values.ticket_type_id[0]}
                model="helpdesk.ticket.type"
              />,
              undefined,
              false
            )}
          </Grid>
          <Grid>
            {item(
              'Stage',
              <RelationLink
                name={values.stage_id[1]}
                pgId={values.stage_id[0]}
                model="helpdesk.stage"
              />,
              undefined,
              false
            )}
            {!!values.workflow_id?.[0] &&
              item(
                'Workflow',
                <RelationLink
                  name={values.workflow_id[1]}
                  pgId={values.workflow_id[0]}
                  model="symple.workflow"
                />,
                undefined,
                false
              )}
            {!!parent?.[0] &&
              item(
                'Parent',
                <RelationLink
                  name={parent[1]}
                  pgId={parent[0]}
                  model="helpdesk.ticket"
                  href={`/helpdesk.ticket/${parent[0]}`}
                />,
                undefined,
                false
              )}
          </Grid>
          <Grid>
            {item(
              'Customer',
              <RelationLink
                name={values.customer_id[1]}
                pgId={values.customer_id[0]}
                model="res.partner"
              />,
              undefined,
              false
            )}
            {item('Customer code', values.customer_code)}
            {!!values.partner_id?.[0] &&
              item(
                'Contact',
                <RelationLink
                  name={values.partner_id[1]}
                  pgId={values.partner_id[0]}
                  model="res.partner"
                />,
                undefined,
                false
              )}
          </Grid>
        </Stack>
      </UiCard>
    );
  }

  function renderLeft() {
    return (
      <Stack gap="md">
        {caseBaseFields.error_message && <Alert color="red">{caseBaseFields.error_message}</Alert>}
        {renderBasicInfo(caseBaseFields)}
        <CaseActivePhase caseId={caseBaseFields.id} workflowId={caseBaseFields.workflow_id[0]} />
        <CaseTabs
          caseId={caseBaseFields.id}
          servicePointIds={caseBaseFields.service_point_ids}
          childIds={caseBaseFields.child_case_ids}
        />
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

          <Link href={`/full-field-config/helpdesk.ticket/${id}`}>
            <Button>
              <IconCode />
            </Button>
          </Link>
        </Group>
      </Group>

      <Space h={32} />

      <Grid gutter="md">
        <Grid.Col span={8}>{renderLeft()}</Grid.Col>
        <Grid.Col span={4}>
          <Stack gap="lg">
            {caseBaseFields.market_comm_event_log_ids.length > 0 && (
              <UiCard title="Market comm">
                <CaseMarketComm caseId={caseBaseFields.id} />
              </UiCard>
            )}
            <UiCard title="Logs">
              <CaseLogs caseId={caseBaseFields.id} />
            </UiCard>
            {caseBaseFields.integration_history_ids.length > 0 && (
              <UiCard title="Integration History">
                <CaseIntegrationHistory caseId={caseBaseFields.id} />
              </UiCard>
            )}
            <UiCard title="Staging Area">
              <CaseStagingArea caseId={caseBaseFields.id} />
            </UiCard>
          </Stack>
        </Grid.Col>
      </Grid>
    </Container>
  );
}
