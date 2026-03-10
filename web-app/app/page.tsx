'use client';

import { useMemo, useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import {
  Center,
  Container,
  Group,
  Loader,
  Pagination,
  Select,
  Stack,
  Table,
  Text,
  TextInput,
} from '@mantine/core';
import { odooSearchRead } from './api';

interface Case {
  id: number;
  title: string;
  status: string;
  priority: string;
  date: string;
}

export default function HomePage() {
  const [filters, setFilters] = useState({
    search: '',
    status: '',
    priority: '',
  });

  const [page, setPage] = useState(1);
  const pageSize = 10;

  const {
    data: cases = [],
    isLoading,
    isError,
    error,
  } = useQuery<Case[]>({
    queryKey: ['cases'],
    queryFn: () =>
      odooSearchRead(
        'helpdesk.ticket',
        [],
        ['name', 'id', 'ticket_type_id'],
        0,
        20,
        'create_date DESC'
      ),
  });

  const filteredData = useMemo(
    () =>
      cases.filter((item: Case) => {
        const matchesSearch = item.title.toLowerCase().includes(filters.search.toLowerCase());
        const matchesStatus = !filters.status || item.status === filters.status;
        const matchesPriority = !filters.priority || item.priority === filters.priority;
        return matchesSearch && matchesStatus && matchesPriority;
      }),
    [cases, filters]
  );

  const totalPages = Math.ceil(filteredData.length / pageSize);
  const paginatedData = filteredData.slice((page - 1) * pageSize, page * pageSize);

  if (isLoading) {
    return (
      <Container size="lg" py="xl">
        <Center py="xl">
          <Loader />
        </Center>
      </Container>
    );
  }

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

  const rows = paginatedData.map((item: Case) => (
    <Table.Tr key={item.id}>
      <Table.Td>{item.id}</Table.Td>
      <Table.Td>{item.title}</Table.Td>
      <Table.Td>{item.status}</Table.Td>
      <Table.Td>{item.priority}</Table.Td>
      <Table.Td>{item.date}</Table.Td>
    </Table.Tr>
  ));

  return (
    <Container size="lg" py="xl">
      <Stack gap="md">
        <Stack gap="sm">
          <TextInput
            placeholder="Search cases..."
            value={filters.search}
            onChange={(e) => setFilters({ ...filters, search: e.currentTarget.value })}
          />
          <Group grow>
            <Select
              placeholder="Filter by status"
              data={['Open', 'In Progress', 'Closed']}
              value={filters.status}
              onChange={(value) => setFilters({ ...filters, status: value || '' })}
              clearable
            />
            <Select
              placeholder="Filter by priority"
              data={['Low', 'Medium', 'High']}
              value={filters.priority}
              onChange={(value) => setFilters({ ...filters, priority: value || '' })}
              clearable
            />
          </Group>
        </Stack>

        <Table striped highlightOnHover>
          <Table.Thead>
            <Table.Tr>
              <Table.Th>ID</Table.Th>
              <Table.Th>Title</Table.Th>
              <Table.Th>Status</Table.Th>
              <Table.Th>Priority</Table.Th>
              <Table.Th>Date</Table.Th>
            </Table.Tr>
          </Table.Thead>
          <Table.Tbody>{rows}</Table.Tbody>
        </Table>

        <Group justify="center">
          <Pagination value={page} onChange={setPage} total={totalPages} />
        </Group>
      </Stack>
    </Container>
  );
}
