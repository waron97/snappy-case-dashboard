import dayjs from 'dayjs';
import Link from 'next/link';
import { IconCode, ReactNode } from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import { Anchor, Box, Button, Grid, Group, Stack, Tabs, Text, Title } from '@mantine/core';
import { odooRead, OneToMany } from '../../../../app/api';
import HelpdeskTicket from './HelpdeskTicket';

type Props = {
  name: string;
  model: string;
  pgId: number;
  href?: string;
};

export default function RelationDropdownBase(props: Props) {
  const { name, model, pgId, href } = props;
  // -------------------------------------
  // Hooks
  // -------------------------------------

  // -------------------------------------
  // Queries
  // -------------------------------------

  // -------------------------------------
  // Effects
  // -------------------------------------

  // -------------------------------------
  // Functions
  // -------------------------------------

  function renderContent() {
    if (model === 'helpdesk.ticket') {
      return <HelpdeskTicket id={pgId} />;
    }

    return <BaseOverlayContent pgId={pgId} model={model} />;
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // -------------------------------------

  return (
    <Stack gap="sm">
      <Group justify="space-between">
        <Title component="h3" size="md">
          {name}
        </Title>
        <Group gap="sm">
          {href && (
            <Link href={href}>
              <Button>View</Button>
            </Link>
          )}
          <Anchor
            href={`https://odoo.sorgenia-test-02.symple.cloud/web#id=${pgId}&model=${model}&view_type=form`}
            target="_blank"
          >
            <Button bg="#714B67">ODOO</Button>
          </Anchor>
          <Link href={`/full-field-config/${model}/${pgId}`}>
            <Button>
              <IconCode />
            </Button>
          </Link>
        </Group>
      </Group>
      {renderContent()}
    </Stack>
  );
}

function BaseOverlayContent({ pgId, model }: { pgId: number; model: string }) {
  const { data } = useQuery<{
    create_uid: OneToMany;
    write_uid: OneToMany;
    create_date: string;
    write_date: string;
  }>({
    queryKey: [model, pgId, 'popover'],
    queryFn: () =>
      odooRead(model, [pgId], ['create_uid', 'create_date', 'write_date', 'write_uid']).then(
        (res) => res[0]
      ),
  });

  const fmt = (d: string) => dayjs(d).format('D/M/YYYY HH:mm');

  const item = (label: string, value: ReactNode, href?: string, wrapValue: boolean = true) => (
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
  );

  if (!data) {
    return null;
  }

  return (
    <Tabs defaultValue="metadata">
      <Tabs.List>
        <Tabs.Tab value="metadata">Metadata</Tabs.Tab>
        <Tabs.Tab value="database">Database</Tabs.Tab>
      </Tabs.List>
      <Tabs.Panel value="database">
        <Grid pt="md">
          <Grid.Col span={6}>
            <Stack gap="sm">
              {item('Model', model)}
              {item('ID', pgId)}
            </Stack>
          </Grid.Col>
        </Grid>
      </Tabs.Panel>
      <Tabs.Panel value="metadata">
        <Grid pt="md">
          <Grid.Col span={6}>
            <Stack gap="sm">
              {item('Create date', fmt(data.create_date))}
              {item('Creation user', data.create_uid[1])}
            </Stack>
          </Grid.Col>
          <Grid.Col span={6}>
            <Stack gap="sm">
              {item('Write date', fmt(data.write_date))}
              {item('Creation user', data.write_uid[1])}
            </Stack>
          </Grid.Col>
        </Grid>
      </Tabs.Panel>
    </Tabs>
  );
}
