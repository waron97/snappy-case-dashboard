'use client';

import { useQuery } from '@tanstack/react-query';
import { Anchor, Badge, Card, Container, Group, Space, Table, Text, Title } from '@mantine/core';
import { fetchPoolStatus, fetchPrs, fetchStatus, PoolStatus, PrRecord, SystemStatus } from '../actions';

function StatCard({ label, value, color }: { label: string; value: number | string; color?: string }) {
    return (
        <Card withBorder radius="md" padding="md" style={{ minWidth: 150, flex: 1 }}>
            <Text size="xs" c="dimmed" tt="uppercase" fw={600}>
                {label}
            </Text>
            <Text fz={32} fw={700} c={color}>
                {value}
            </Text>
        </Card>
    );
}

export default function ControlPanelPage() {
    const { data: status } = useQuery<SystemStatus>({
        queryKey: ['devops', 'status'],
        queryFn: fetchStatus,
        refetchInterval: 3_000,
    });

    const { data: pool } = useQuery<PoolStatus>({
        queryKey: ['devops', 'pool'],
        queryFn: fetchPoolStatus,
        refetchInterval: 3_000,
    });

    const { data: prs = [] } = useQuery<PrRecord[]>({
        queryKey: ['devops', 'prs'],
        queryFn: fetchPrs,
        refetchInterval: 10_000,
    });

    const queue = status?.queue ?? [];
    const workers = status?.workers ?? {};
    const running = Object.values(workers);

    const titleFor = (commit: string) => prs.find((p) => p.commitId === commit)?.title ?? '—';

    return (
        <Container size="xl" py="md">
            <Title fz={28}>Control Panel</Title>
            <Space h={24} />

            <Group grow align="stretch">
                <StatCard label="Queue" value={queue.length} color={queue.length ? 'blue' : undefined} />
                <StatCard label="Running" value={running.length} color={running.length ? 'yellow' : undefined} />
                <StatCard label="Warm DBs ready" value={pool?.ready ?? '…'} color={pool?.ready ? 'green' : undefined} />
                <StatCard label="Warming" value={pool?.building ?? '…'} />
            </Group>

            <Space h={32} />

            <Title order={3} fz={20}>
                Running now
            </Title>
            <Space h={8} />
            {running.length === 0 ? (
                <Text c="dimmed" size="sm">
                    No tests running.
                </Text>
            ) : (
                <Table striped highlightOnHover>
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th>Worker</Table.Th>
                            <Table.Th>Commit</Table.Th>
                            <Table.Th>PR</Table.Th>
                        </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                        {Object.entries(workers).map(([wid, commit]) => (
                            <Table.Tr key={wid}>
                                <Table.Td>
                                    <Text size="sm" ff="monospace" c="dimmed">
                                        {wid}
                                    </Text>
                                </Table.Td>
                                <Table.Td>
                                    <Anchor href={`/devops/${commit}`} size="sm" ff="monospace">
                                        {commit.slice(0, 8)}
                                    </Anchor>
                                </Table.Td>
                                <Table.Td>
                                    <Text size="sm">{titleFor(commit)}</Text>
                                </Table.Td>
                            </Table.Tr>
                        ))}
                    </Table.Tbody>
                </Table>
            )}

            <Space h={32} />

            <Title order={3} fz={20}>
                Queue (processing order)
            </Title>
            <Space h={8} />
            {queue.length === 0 ? (
                <Text c="dimmed" size="sm">
                    Queue is empty.
                </Text>
            ) : (
                <Table striped highlightOnHover>
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th w={60}>#</Table.Th>
                            <Table.Th>Commit</Table.Th>
                            <Table.Th>PR</Table.Th>
                        </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                        {queue.map((commit, i) => (
                            <Table.Tr key={commit}>
                                <Table.Td>
                                    <Badge variant={i === 0 ? 'filled' : 'light'} color={i === 0 ? 'blue' : 'gray'}>
                                        {i + 1}
                                    </Badge>
                                </Table.Td>
                                <Table.Td>
                                    <Anchor href={`/devops/${commit}`} size="sm" ff="monospace">
                                        {commit.slice(0, 8)}
                                    </Anchor>
                                </Table.Td>
                                <Table.Td>
                                    <Text size="sm">{titleFor(commit)}</Text>
                                </Table.Td>
                            </Table.Tr>
                        ))}
                    </Table.Tbody>
                </Table>
            )}
        </Container>
    );
}
