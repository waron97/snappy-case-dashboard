import { Checkbox, Group, Stack, TagsInput } from '@mantine/core';
import { DateInput, DatePicker } from '@mantine/dates';

type Props = {
  value: { [key: string]: any };
  onChange: (v: { [key: string]: any }) => void;
};

export default function CaseFilters(props: Props) {
  const { value: filters, onChange: setFilters } = props;
  console.log('filters', filters);

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

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // -------------------------------------

  return (
    <Stack gap="sm">
      <Group grow>
        <TagsInput
          label="Case Name"
          value={filters.name}
          onChange={(value: string[]) => setFilters({ ...filters, name: value || [] })}
        />
        <TagsInput
          label="Workflow"
          value={filters.workflow}
          onChange={(v) => setFilters({ ...filters, workflow: v })}
        />
        <TagsInput
          label="Ticket type"
          value={filters.ticketType}
          onChange={(v) => setFilters({ ...filters, ticketType: v })}
        />
      </Group>
      <Group grow>
        <DateInput
          label="Creati dopo il"
          value={filters.startDate}
          onChange={(v) => setFilters({ ...filters, startDate: v })}
          clearable
        />
        <DateInput
          label="Creati prima del"
          value={filters.endDate}
          onChange={(v) => setFilters({ ...filters, endDate: v })}
          clearable
        />
      </Group>
      <Checkbox
        label="Mostra case chiusi"
        checked={filters.is_close === null}
        onChange={(v) => setFilters({ ...filters, is_close: v.target.checked ? null : false })}
      />
    </Stack>
  );
}
