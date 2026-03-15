import { useQuery } from '@tanstack/react-query';
import { Grid, Stack, Text } from '@mantine/core';
import { odooRead, OneToMany } from '../../../../../app/api';

type Props = {
  id: number;
};

type TicketFields = {
  triplet_type_id: OneToMany;
  triplet_subtype_id: OneToMany;
  ticket_type_id: OneToMany;
  stage_id: OneToMany;
  workflow_id: OneToMany;
  parent_case_id: OneToMany;
  triplet_active_phase_id: OneToMany;
};

export default function HelpdeskTicket(props: Props) {
  const { id } = props;

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data } = useQuery<TicketFields>({
    queryKey: ['helpdesk.ticket', id, 'popover'],
    queryFn: () =>
      odooRead(
        'helpdesk.ticket',
        [id],
        [
          'triplet_type_id',
          'triplet_subtype_id',
          'ticket_type_id',
          'stage_id',
          'workflow_id',
          'parent_case_id',
          'triplet_active_phase_id',
        ]
      ).then((res) => res[0]),
  });

  // -------------------------------------
  // Functions
  // -------------------------------------

  const item = (label: string, value: string, span?: number) => (
    <Grid.Col span={span || 'auto'}>
      <Stack gap={0}>
        <Text c="dimmed">{label}</Text>
        <Text fw="bold">{value}</Text>
      </Stack>
    </Grid.Col>
  );

  // -------------------------------------

  if (!data) {
    return null;
  }

  return (
    <Stack gap="sm" pt="sm">
      <Grid>
        {item('Type', data.triplet_type_id[1], 2)}
        {item('Subtype', data.triplet_subtype_id[1])}
        {item('Detail', data.ticket_type_id[1])}
      </Grid>
      <Grid>
        {item('Stage', data.stage_id[1], 2)}
        {!!data.workflow_id?.[0] && item('Workflow', data.workflow_id[1])}
        {!!data.triplet_active_phase_id?.[0] &&
          item('Active phase', data.triplet_active_phase_id[1])}
      </Grid>
      {!!data.parent_case_id?.[0] && <Grid>{item('Parent', data.parent_case_id[1])}</Grid>}
    </Stack>
  );
}
