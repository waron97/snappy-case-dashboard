'use client';

import dayjs from 'dayjs';
import { useState, type ReactNode } from 'react';
import { useParams } from 'next/navigation';
import {
  IconChevronDown,
  IconChevronUp,
  IconHelpCircle,
  IconLock,
  IconLockX,
  IconSearch,
  IconSelector,
} from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import {
  Alert,
  Box,
  Button,
  Center,
  Checkbox,
  Container,
  Grid,
  Group,
  LoadingOverlay,
  NumberInput,
  Pagination,
  Select,
  Stack,
  Switch,
  Table,
  Text,
  TextInput,
  Title,
  Tooltip,
  UnstyledButton,
} from '@mantine/core';
import { useDebouncedValue } from '@mantine/hooks';
import RelationLink from '@/components/RelationLink';
import UiCard from '@/components/UiCard';
import { fieldsGet, OdooFieldDefinition } from '../../../../src/utils/odoo';
import { odooNameGet, odooRead } from '../../../api';

const PAGE_SIZE = 50;

type SortKey = 'label' | 'fieldName' | 'type';
type SortDir = 'asc' | 'desc';

const EDITABLE_TYPES = new Set([
  'char',
  'text',
  'html',
  'integer',
  'float',
  'monetary',
  'boolean',
  'date',
  'datetime',
  'selection',
]);

function isEditable(def: OdooFieldDefinition) {
  return def.store && EDITABLE_TYPES.has(def.type);
}

function renderValue(
  _fieldName: string,
  fieldDef: OdooFieldDefinition,
  rawValue: unknown
): ReactNode {
  if (rawValue === false || rawValue === null || rawValue === undefined) {
    return '—';
  }

  switch (fieldDef.type) {
    case 'selection': {
      const entry = fieldDef.selection?.find(([k]) => k === rawValue);
      return entry ? entry[1] : String(rawValue);
    }
    case 'many2one':
      if (!Array.isArray(rawValue)) {
        return String(rawValue);
      }
      return (
        <RelationLink
          name={String(rawValue[1])}
          pgId={rawValue[0] as number}
          model={fieldDef.relation!}
        />
      );
    case 'one2many':
    case 'many2many':
      if (!Array.isArray(rawValue) || rawValue.length === 0) {
        return '—';
      }
      return (
        <Stack gap={2}>
          {(rawValue as number[]).map((id) => (
            <RelationLink key={id} pgId={id} model={fieldDef.relation!} autoName />
          ))}
        </Stack>
      );
    case 'boolean':
      return rawValue ? 'true' : 'false';
    case 'binary':
      return '[binary]';
    default:
      return String(rawValue);
  }
}

function MetaRow({ label, value }: { label: string; value: string }) {
  return (
    <Box>
      <Text size="xs" c="dimmed">
        {label}
      </Text>
      <Text size="sm">{value}</Text>
    </Box>
  );
}

function SortTh({
  label,
  sortKey,
  current,
  dir,
  onSort,
}: {
  label: string;
  sortKey: SortKey;
  current: SortKey;
  dir: SortDir;
  onSort: (k: SortKey) => void;
}) {
  const active = current === sortKey;
  const Icon = active ? (dir === 'asc' ? IconChevronUp : IconChevronDown) : IconSelector;
  return (
    <Table.Th>
      <UnstyledButton onClick={() => onSort(sortKey)} style={{ width: '100%' }}>
        <Group gap={4} wrap="nowrap">
          <Text fw={active ? 700 : 400} size="sm">
            {label}
          </Text>
          <Center>
            <Icon size={14} />
          </Center>
        </Group>
      </UnstyledButton>
    </Table.Th>
  );
}

export default function FullRecordView() {
  const { model, record } = useParams();
  const id = parseInt(String(record), 10);
  const [search, setSearch] = useState('');
  const [debouncedSearch] = useDebouncedValue(search, 300);
  const [typeFilter, setTypeFilter] = useState<string | null>(null);
  const [onlyComputed, setOnlyComputed] = useState(false);
  const [sortKey, setSortKey] = useState<SortKey>('label');
  const [sortDir, setSortDir] = useState<SortDir>('asc');
  const [page, setPage] = useState(1);
  const [locked, setLocked] = useState(true);
  const [edits, setEdits] = useState<Record<string, unknown>>({});

  const { data: name } = useQuery({
    queryKey: [model, record, 'name'],
    queryFn: () => odooNameGet(String(model), [id]).then((res) => res[0][1]),
  });

  const { data: fieldDefs, isLoading: fieldsLoading } = useQuery({
    queryKey: ['fields-get', model],
    queryFn: () => fieldsGet(String(model)),
  });

  const SKIP_TYPES = new Set(['binary', 'reference']);
  const BROKEN_FIELDS: Record<string, Set<string>> = {
    'helpdesk.ticket': new Set(['pdr_change_value_id']),
  };

  const fieldNames = fieldDefs
    ? Object.entries(fieldDefs)
        .filter(
          ([name, def]) =>
            def.store && !SKIP_TYPES.has(def.type) && !BROKEN_FIELDS[String(model)]?.has(name)
        )
        .map(([name]) => name)
    : [];

  const { data: records, isLoading: recordLoading } = useQuery({
    queryKey: ['record', model, record],
    queryFn: () => odooRead(String(model), [id], fieldNames),
    enabled: fieldNames.length > 0,
  });

  const recordData = records?.[0];

  const needle = debouncedSearch.toLowerCase();

  function handleSort(key: SortKey) {
    if (key === sortKey) {
      setSortDir((d) => (d === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortKey(key);
      setSortDir('asc');
    }
    setPage(1);
  }

  function handleSave() {
    console.log('[save]', { model, record, edits });
  }

  function handleReset() {
    setEdits({});
  }

  function renderEditInput(fieldName: string, fieldDef: OdooFieldDefinition, rawValue: unknown) {
    if (!isEditable(fieldDef)) {
      return null;
    }

    const currentValue = fieldName in edits ? edits[fieldName] : rawValue;

    function onChange(newVal: unknown) {
      if (
        newVal === rawValue ||
        (newVal === '' && (rawValue === false || rawValue === null || rawValue === undefined))
      ) {
        setEdits((prev) => {
          const next = { ...prev };
          delete next[fieldName];
          return next;
        });
      } else {
        setEdits((prev) => ({ ...prev, [fieldName]: newVal }));
      }
    }

    if (fieldDef.type === 'boolean') {
      return (
        <Switch
          checked={!!currentValue}
          onChange={(e) => onChange(e.currentTarget.checked)}
          size="sm"
        />
      );
    }

    if (fieldDef.type === 'selection') {
      const data = (fieldDef.selection ?? []).map(([v, l]) => ({ value: String(v), label: l }));
      return (
        <Select
          data={data}
          value={
            currentValue !== false && currentValue !== null && currentValue !== undefined
              ? String(currentValue)
              : null
          }
          onChange={(v) => onChange(v)}
          size="xs"
          clearable
        />
      );
    }

    if (fieldDef.type === 'integer') {
      return (
        <NumberInput
          value={
            typeof currentValue === 'number'
              ? currentValue
              : currentValue === false || currentValue === null || currentValue === undefined
                ? ''
                : Number(currentValue)
          }
          onChange={(v) => onChange(v)}
          allowDecimal={false}
          size="xs"
        />
      );
    }

    if (fieldDef.type === 'float' || fieldDef.type === 'monetary') {
      return (
        <NumberInput
          value={
            typeof currentValue === 'number'
              ? currentValue
              : currentValue === false || currentValue === null || currentValue === undefined
                ? ''
                : Number(currentValue)
          }
          onChange={(v) => onChange(v)}
          size="xs"
        />
      );
    }

    // char, text, html, date, datetime
    return (
      <TextInput
        value={
          currentValue === false || currentValue === null || currentValue === undefined
            ? ''
            : String(currentValue)
        }
        onChange={(e) => onChange(e.currentTarget.value)}
        size="xs"
      />
    );
  }

  const allRows =
    fieldDefs && recordData
      ? Object.entries(fieldDefs)
          .filter(
            ([name, def]) =>
              def.store && !SKIP_TYPES.has(def.type) && !BROKEN_FIELDS[String(model)]?.has(name)
          )
          .map(([fieldName, fieldDef]) => ({
            fieldName,
            label: fieldDef.string,
            fieldDef,
            value: renderValue(fieldName, fieldDef, recordData[fieldName]),
          }))
          .filter(({ fieldName, label, fieldDef }) => {
            if (
              needle &&
              !label.toLowerCase().includes(needle) &&
              !fieldName.toLowerCase().includes(needle)
            ) {
              return false;
            }
            if (typeFilter && fieldDef.type !== typeFilter) {
              return false;
            }
            if (onlyComputed && !fieldDef.compute) {
              return false;
            }
            return true;
          })
          .sort((a, b) => {
            let cmp = 0;
            if (sortKey === 'label') {
              cmp = a.label.localeCompare(b.label);
            } else if (sortKey === 'fieldName') {
              cmp = a.fieldName.localeCompare(b.fieldName);
            } else if (sortKey === 'type') {
              cmp = a.fieldDef.type.localeCompare(b.fieldDef.type);
            }

            return sortDir === 'asc' ? cmp : -cmp;
          })
      : [];

  const totalPages = Math.max(1, Math.ceil(allRows.length / PAGE_SIZE));
  const rows = allRows.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);

  const typeOptions = fieldDefs
    ? Array.from(new Set(Object.values(fieldDefs).map((d) => d.type)))
        .sort()
        .map((t) => ({ value: t, label: t }))
    : [];

  const fmt = (v: unknown) => (v && typeof v === 'string' ? dayjs(v).format('D/M/YY HH:mm') : '—');
  const userName = (v: unknown) => (Array.isArray(v) ? String(v[1]) : '—');

  const sortProps = { current: sortKey, dir: sortDir, onSort: handleSort };

  const lockButton = (
    <Button
      onClick={() => {
        if (!locked) {
          setEdits({});
        }
        setLocked((l) => !l);
      }}
      disabled={!recordData}
    >
      <Group gap="sm">
        <Text>{locked ? 'Unlock' : 'Lock'}</Text>
        {locked ? <IconLockX size={16} /> : <IconLock size={16} />}
      </Group>
    </Button>
  );

  const pendingKeys = Object.keys(edits);

  return (
    <Container size="xl" py="xl">
      <Title mb="md">{name || `${record} #${id}`}</Title>
      <Grid gutter="md" align="flex-start">
        <Grid.Col span={9}>
          <Stack gap="md">
            <UiCard title="Filters">
              <Group align="flex-end">
                <TextInput
                  placeholder="Search by name or label…"
                  leftSection={<IconSearch size={14} />}
                  value={search}
                  onChange={(e) => {
                    setSearch(e.currentTarget.value);
                    setPage(1);
                  }}
                  style={{ flex: 1 }}
                />
                <Select
                  placeholder="All types"
                  data={typeOptions}
                  value={typeFilter}
                  onChange={(v) => {
                    setTypeFilter(v);
                    setPage(1);
                  }}
                  clearable
                  w={160}
                />
                <Checkbox
                  label="Computed only"
                  checked={onlyComputed}
                  onChange={(e) => {
                    setOnlyComputed(e.currentTarget.checked);
                    setPage(1);
                  }}
                />
              </Group>
            </UiCard>

            <UiCard title={`Fields (${allRows.length})`} rightElement={lockButton}>
              {!locked && pendingKeys.length > 0 && (
                <Alert color="yellow" mb="md" title="Unsaved changes">
                  <Stack gap={4}>
                    {Object.entries(edits).map(([fieldName, newVal]) => {
                      const fieldDef = fieldDefs![fieldName];
                      return (
                        <Text key={fieldName} size="sm">
                          <b>{fieldDef.string}</b>:{' '}
                          {renderValue(fieldName, fieldDef, recordData![fieldName])} →{' '}
                          {renderValue(fieldName, fieldDef, newVal)}
                        </Text>
                      );
                    })}
                  </Stack>
                  <Group mt="sm" gap="xs">
                    <Button size="xs" color="green" onClick={handleSave}>
                      Save
                    </Button>
                    <Button size="xs" variant="subtle" onClick={handleReset}>
                      Reset
                    </Button>
                  </Group>
                </Alert>
              )}
              <Box pos="relative" style={{ overflowX: 'auto' }}>
                <LoadingOverlay visible={fieldsLoading || recordLoading} />
                <Table striped highlightOnHover>
                  <Table.Thead>
                    <Table.Tr>
                      <SortTh label="Field" sortKey="label" {...sortProps} />
                      <SortTh label="Type" sortKey="type" {...sortProps} />
                      <Table.Th>Value</Table.Th>
                      {!locked && <Table.Th>Updated value</Table.Th>}
                    </Table.Tr>
                  </Table.Thead>
                  <Table.Tbody>
                    {rows.map(({ fieldName, label, fieldDef, value }) => (
                      <Table.Tr key={fieldName}>
                        <Table.Td>
                          <Box style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                            {label}
                            {fieldDef.help && (
                              <Tooltip label={fieldDef.help} multiline maw={300} withArrow>
                                <IconHelpCircle
                                  size={14}
                                  style={{ cursor: 'help', flexShrink: 0 }}
                                />
                              </Tooltip>
                            )}
                          </Box>
                          <Text size="xs" c="dimmed">
                            {fieldName}
                          </Text>
                        </Table.Td>
                        <Table.Td>
                          <Text size="sm" c="dimmed">
                            {fieldDef.type}
                          </Text>
                        </Table.Td>
                        <Table.Td>{value}</Table.Td>
                        {!locked && (
                          <Table.Td>
                            {isEditable(fieldDef) ? (
                              renderEditInput(fieldName, fieldDef, recordData![fieldName])
                            ) : (
                              <Text size="xs" c="dimmed">
                                —
                              </Text>
                            )}
                          </Table.Td>
                        )}
                      </Table.Tr>
                    ))}
                  </Table.Tbody>
                </Table>
              </Box>
              {totalPages > 1 && (
                <Group justify="center" mt="md">
                  <Pagination value={page} onChange={setPage} total={totalPages} size="sm" />
                </Group>
              )}
            </UiCard>
          </Stack>
        </Grid.Col>

        <Grid.Col span={3}>
          <UiCard title="Record metadata">
            <Stack gap="sm">
              <MetaRow label="Created" value={fmt(recordData?.create_date)} />
              <MetaRow label="Created by" value={userName(recordData?.create_uid)} />
              <MetaRow label="Last modified" value={fmt(recordData?.write_date)} />
              <MetaRow label="Last modified by" value={userName(recordData?.write_uid)} />
            </Stack>
          </UiCard>
        </Grid.Col>
      </Grid>
    </Container>
  );
}
