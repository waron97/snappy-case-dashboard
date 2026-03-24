'use client';

import { useRef, useState } from 'react';
import Link from 'next/link';
import { odooSearchRead } from '@app/api';
import { IconEye } from '@tabler/icons-react';
import { useInfiniteQuery } from '@tanstack/react-query';
import {
    Badge,
    Button,
    Center,
    Container,
    Group,
    Loader,
    Stack,
    Table,
    TagsInput,
    Text,
} from '@mantine/core';
import UiCard from '@/components/UiCard';
import { useInfiniteScroll } from '@/hooks/useInfiniteScroll';
import { constructOdooDomain } from '@/utils/odoo';

interface MFA {
    id: number;
    name: string;
    model_name: string;
    model_schema_in_id: [number, string] | false;
    model_schema_out_id: [number, string] | false;
    enabled: boolean;
}

export default function MFA() {
    // -------------------------------------
    // Hooks
    // -------------------------------------

    const [filters, setFilters] = useState<{
        name: string[];
        model: string[];
    }>({
        name: [],
        model: [],
    });

    const sentinelRef = useRef<HTMLDivElement>(null);

    // -------------------------------------
    // Queries
    // -------------------------------------

    const { data, isLoading, isError, error, fetchNextPage, hasNextPage, isFetchingNextPage } =
        useInfiniteQuery({
            queryKey: ['mfa', filters],
            queryFn: ({ pageParam = 0 }) =>
                odooSearchRead(
                    'rip.model.function.access',
                    constructOdooDomain({
                        name: { operator: 'ilike', value: filters.name },
                        model_name: { operator: 'ilike', value: filters.model },
                    }),
                    [
                        'id',
                        'name',
                        'model_name',
                        'model_schema_in_id',
                        'model_schema_out_id',
                        'enabled',
                    ],
                    pageParam,
                    20,
                    'name ASC'
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
    // Local Variables
    // -------------------------------------

    const items = data?.pages.flatMap((page) => page) ?? [];

    const rows = items.map((item: MFA) => (
        <Table.Tr key={item.id}>
            <Table.Td miw={130}>
                {item.enabled ? (
                    item.name
                ) : (
                    <Badge color="gray" size="md">
                        {item.name}
                    </Badge>
                )}
            </Table.Td>
            <Table.Td>{item.model_name}</Table.Td>
            {/* <Table.Td>{item.model_schema_in_id ? item.model_schema_in_id[1] : '—'}</Table.Td> */}
            {/* <Table.Td>{item.model_schema_out_id ? item.model_schema_out_id[1] : '—'}</Table.Td> */}
            <Table.Td>
                <Link href={`/rip/mfa/${item.id}`}>
                    <Button size="xs">
                        <IconEye size={18} />
                    </Button>
                </Link>
            </Table.Td>
        </Table.Tr>
    ));

    // -------------------------------------

    if (isError) {
        return (
            <Container size="lg" py="xl">
                <Center py="xl">
                    <Text c="red">
                        Failed to load functions:{' '}
                        {error instanceof Error ? error.message : 'Unknown error'}
                    </Text>
                </Center>
            </Container>
        );
    }

    return (
        <Container size="xl" py="sm">
            <Stack gap="md" pt="md">
                <UiCard title="Filters">
                    <Group grow>
                        <TagsInput
                            label="Name"
                            value={filters.name}
                            onChange={(name) => setFilters({ ...filters, name })}
                        />
                        <TagsInput
                            label="Model"
                            value={filters.model}
                            onChange={(model) => setFilters({ ...filters, model })}
                        />
                    </Group>
                </UiCard>

                <Table striped highlightOnHover>
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th>Name</Table.Th>
                            <Table.Th>Model</Table.Th>
                            {/* <Table.Th>Schema In</Table.Th> */}
                            {/* <Table.Th>Schema Out</Table.Th> */}
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
