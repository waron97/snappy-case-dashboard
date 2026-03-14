'use client';

import dayjs from 'dayjs';
import { useRef, useState } from 'react';
import type { Metadata } from 'next';
import Link from 'next/link';
import { IconEye } from '@tabler/icons-react';
import { useInfiniteQuery } from '@tanstack/react-query';
import {
  Badge,
  Button,
  Center,
  Checkbox,
  Container,
  Group,
  Loader,
  Stack,
  Table,
  TagsInput,
  Text,
} from '@mantine/core';
import CaseFilters from '@/components/CaseFilters';
import { useInfiniteScroll } from '@/hooks/useInfiniteScroll';
import { constructOdooDomain } from '@/utils/odoo';
import { odooSearchRead } from './api';

interface Case {
  id: number;
  name: string;
  stage_id: [number, string];
  workflow_id: [number, string];
  ticket_type_id: [number, string];
  customer_id: [number, string];
  triplet_active_phase_id: [number, string];
  error_message?: string;
  create_date: string;
}

export default function HomePage() {
  // -------------------------------------
  // Hooks
  // -------------------------------------
  const [filters, setFilters] = useState<{
    name: string[];
    is_close: boolean | null;
    workflow: string[];
    ticketType: string[];
    customer_id: string[];
    startDate: string | null;
    endDate: string | null;
  }>({
    name: [],
    is_close: false,
    workflow: [],
    ticketType: [],
    customer_id: [],
    startDate: null,
    endDate: null,
  });

  const sentinelRef = useRef<HTMLDivElement>(null);

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data, isLoading, isError, error, fetchNextPage, hasNextPage, isFetchingNextPage } =
    useInfiniteQuery({
      queryKey: ['cases', filters],
      queryFn: ({ pageParam = 0 }) =>
        odooSearchRead(
          'helpdesk.ticket',
          [
            ...constructOdooDomain({
              'workflow_id.name': { operator: 'ilike', value: filters.workflow },
              'ticket_type_id.name': { operator: 'ilike', value: filters.ticketType },
              name: { operator: 'ilike', value: filters.name },
              is_close: { operator: '=', value: filters.is_close },
            }),
            ...(filters.startDate ? [['create_date', '>=', filters.startDate]] : []),
            ...(filters.endDate ? [['create_date', '<=', filters.endDate]] : []),
          ],
          [
            'name',
            'id',
            'ticket_type_id',
            'workflow_id',
            'customer_id',
            'stage_id',
            'triplet_active_phase_id',
            'error_message',
            'create_date',
          ],
          pageParam,
          20,
          'create_date DESC'
        ),
      getNextPageParam: (lastPage, allPages) =>
        lastPage.length === 20 ? allPages.length * 20 : undefined,
      initialPageParam: 0,
    });

  useInfiniteScroll({
    sentinelRef,
    hasNextPage,
    isFetchingNextPage,
    fetchNextPage,
  });

  // -------------------------------------
  // Functions
  // -------------------------------------

  const itemName = (row: Case) => {
    const stageName = row.stage_id[1];
    if (row.error_message || ['Done KO'].includes(stageName)) {
      return (
        <Badge size="md" color="red" style={{ whiteSpace: 'normal', overflow: 'visible' }}>
          {row.name}
        </Badge>
      );
    }

    if (['Cancelled'].includes(stageName)) {
      return (
        <Badge size="md" color="gray" style={{ whiteSpace: 'normal', overflow: 'visible' }}>
          {row.name}
        </Badge>
      );
    }

    if (['Solved', 'Done'].includes(stageName)) {
      return (
        <Badge size="md" color="green" style={{ whiteSpace: 'normal', overflow: 'visible' }}>
          {row.name}
        </Badge>
      );
    }

    return row.name;
  };

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const cases = data?.pages.flatMap((page) => page) ?? [];

  const rows = cases.map((item: Case) => (
    <Table.Tr key={item.id}>
      <Table.Td miw={130}>{itemName(item)}</Table.Td>
      <Table.Td>{item.customer_id[1]}</Table.Td>
      <Table.Td>{item.ticket_type_id[1]}</Table.Td>
      <Table.Td>{item.workflow_id[1]}</Table.Td>
      <Table.Td>{item.triplet_active_phase_id?.[1]}</Table.Td>
      <Table.Td>{dayjs(item.create_date).format('D/M/YY HH:mm')}</Table.Td>
      <Table.Td>
        <Link href={`/helpdesk.ticket/${item.id}`} target="_blank">
          <Button>
            <IconEye size={18} />
          </Button>
        </Link>
      </Table.Td>
    </Table.Tr>
  ));

  if (isError) {
    return (
      <Container size="lg" py="xl">
        <Center py="xl">
          <Text c="red">
            Failed to load cases: {error instanceof Error ? error.message : 'Unknown error'}
          </Text>
        </Center>
      </Container>
    );
  }

  return (
    <Container size="xl" py="sm">
      <Stack gap="md">
        <CaseFilters value={filters} onChange={(v: any) => setFilters(v)} />
        <Table striped highlightOnHover>
          <Table.Thead>
            <Table.Tr>
              <Table.Th>Name</Table.Th>
              <Table.Th>Customer</Table.Th>
              <Table.Th>Detail</Table.Th>
              <Table.Th>Workflow</Table.Th>
              <Table.Th>Active phase</Table.Th>
              <Table.Th>Create date</Table.Th>
              <Table.Th />
            </Table.Tr>
          </Table.Thead>
          <Table.Tbody>{rows}</Table.Tbody>
        </Table>

        <div ref={sentinelRef} style={{ height: '1px' }} />

        {(isLoading || isFetchingNextPage) && (
          <Center py="xl">
            <Loader size="sm" />
          </Center>
        )}
      </Stack>
    </Container>
  );
}
