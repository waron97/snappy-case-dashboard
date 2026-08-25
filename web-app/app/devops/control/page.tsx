'use client';

import { useEffect, useMemo, useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { Anchor, Badge, Card, Container, Group, Loader, Space, Table, Text, Title } from '@mantine/core';
import { TASK_COLOR, TASK_LABEL, TASK_NAMES, TaskBadge } from '@/components/TaskBadge';
import {
    fetchPoolStatus,
    fetchPrs,
    fetchStatus,
    PoolStatus,
    PrRecord,
    QueuedJob,
    SystemStatus,
    WorkerJob,
} from '../actions';

function StatCard({ label, value, color }: { label: string; value: number | string; color?: string }) {
    return (
        <Card withBorder radius="md" padding="md" style={{ minWidth: 130, flex: 1 }}>
            <Text size="xs" c="dimmed" tt="uppercase" fw={600}>
                {label}
            </Text>
            <Text fz={32} fw={700} c={color}>
                {value}
            </Text>
        </Card>
    );
}

function fmtElapsed(seconds: number): string {
    if (!Number.isFinite(seconds) || seconds < 0) {
        return '—';
    }
    const s = Math.floor(seconds);
    const h = Math.floor(s / 3600);
    const m = Math.floor((s % 3600) / 60);
    const rest = s % 60;
    const pad = (n: number) => String(n).padStart(2, '0');
    return h > 0 ? `${h}:${pad(m)}:${pad(rest)}` : `${m}:${pad(rest)}`;
}

function TaskChip({ task }: { task: WorkerJob['task'] }) {
    return (
        <Badge color={TASK_COLOR[task]} variant="filled" size="sm">
            {TASK_LABEL[task]}
        </Badge>
    );
}

function QueueTable({ jobs, titleFor }: { jobs: QueuedJob[]; titleFor: (c: string) => string }) {
    return (
        <Table striped highlightOnHover>
            <Table.Thead>
                <Table.Tr>
                    <Table.Th w={60}>#</Table.Th>
                    <Table.Th w={120}>Task</Table.Th>
                    <Table.Th>Commit</Table.Th>
                    <Table.Th>PR</Table.Th>
                </Table.Tr>
            </Table.Thead>
            <Table.Tbody>
                {jobs.map((job, i) => (
                    <Table.Tr key={`${job.commit}:${job.task}`}>
                        <Table.Td>
                            <Badge variant={i === 0 ? 'filled' : 'light'} color={i === 0 ? 'blue' : 'gray'}>
                                {i + 1}
                            </Badge>
                        </Table.Td>
                        <Table.Td>
                            <TaskChip task={job.task} />
                        </Table.Td>
                        <Table.Td>
                            <Anchor href={`/devops/${job.commit}`} size="sm" ff="monospace">
                                {job.commit.slice(0, 8)}
                            </Anchor>
                        </Table.Td>
                        <Table.Td>
                            <Text size="sm">{titleFor(job.commit)}</Text>
                        </Table.Td>
                    </Table.Tr>
                ))}
            </Table.Tbody>
        </Table>
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

    // Tick locally every second so the elapsed counters move between the 3s refetches.
    const [tick, setTick] = useState(0);
    useEffect(() => {
        const id = setInterval(() => setTick((t) => t + 1), 1_000);
        return () => clearInterval(id);
    }, []);

    const queue = status?.queue ?? [];
    const fastQueue = status?.fastQueue ?? [];
    const workers = status?.workers ?? [];

    // Render elapsed against the server clock: the API returns its own `now`, so a
    // browser whose clock is off by minutes doesn't show nonsense durations. Recomputed
    // on every tick, which is what keeps the counters advancing.
    const now = useMemo(() => {
        const skew = status ? Date.now() / 1000 - status.now : 0;
        return Date.now() / 1000 - skew;
    }, [status, tick]);

    const prFor = (commit: string) => prs.find((p) => p.commitId === commit) ?? null;
    const titleFor = (commit: string) => prFor(commit)?.title ?? '—';

    const inFlight = prs.filter((p) => Object.keys(p.tasks ?? {}).length > 0);

    return (
        <Container size="xl" py="md">
            <Title fz={28}>Control Panel</Title>
            <Space h={24} />

            <Group grow align="stretch">
                <StatCard label="Queue" value={queue.length} color={queue.length ? 'blue' : undefined} />
                <StatCard
                    label="Fast queue"
                    value={fastQueue.length}
                    color={fastQueue.length ? 'grape' : undefined}
                />
                <StatCard label="Running" value={workers.length} color={workers.length ? 'yellow' : undefined} />
                <StatCard label="Warm DBs ready" value={pool?.ready ?? '…'} color={pool?.ready ? 'green' : undefined} />
                <StatCard label="Warming" value={pool?.building ?? '…'} />
            </Group>

            <Space h={32} />

            <Title order={3} fz={20}>
                Running now
            </Title>
            <Space h={8} />
            {workers.length === 0 ? (
                <Text c="dimmed" size="sm">
                    No tasks running.
                </Text>
            ) : (
                <Table striped highlightOnHover>
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th w={160}>Worker</Table.Th>
                            <Table.Th w={120}>Task</Table.Th>
                            <Table.Th w={100}>Commit</Table.Th>
                            <Table.Th>PR</Table.Th>
                            <Table.Th>Stage</Table.Th>
                            <Table.Th w={90}>Elapsed</Table.Th>
                        </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                        {workers.map((job) => (
                            <Table.Tr key={job.worker}>
                                <Table.Td>
                                    <Text size="sm" ff="monospace" c="dimmed">
                                        {job.worker}
                                    </Text>
                                </Table.Td>
                                <Table.Td>
                                    <TaskChip task={job.task} />
                                </Table.Td>
                                <Table.Td>
                                    <Anchor href={`/devops/${job.commit}`} size="sm" ff="monospace">
                                        {job.commit.slice(0, 8)}
                                    </Anchor>
                                </Table.Td>
                                <Table.Td>
                                    <Text size="sm">{titleFor(job.commit)}</Text>
                                </Table.Td>
                                <Table.Td>
                                    <Group gap="xs" wrap="nowrap">
                                        <Loader size={12} />
                                        <Text size="sm">{job.stage}</Text>
                                    </Group>
                                </Table.Td>
                                <Table.Td>
                                    <Text size="sm" ff="monospace">
                                        {fmtElapsed(now - job.started)}
                                    </Text>
                                </Table.Td>
                            </Table.Tr>
                        ))}
                    </Table.Tbody>
                </Table>
            )}

            <Space h={32} />

            <Title order={3} fz={20}>
                Tasks by PR
            </Title>
            <Space h={8} />
            {inFlight.length === 0 ? (
                <Text c="dimmed" size="sm">
                    Nothing tracked.
                </Text>
            ) : (
                <Table striped highlightOnHover>
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th>PR</Table.Th>
                            <Table.Th w={100}>Commit</Table.Th>
                            {TASK_NAMES.map((task) => (
                                <Table.Th key={task} w={150}>
                                    {TASK_LABEL[task]}
                                </Table.Th>
                            ))}
                        </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                        {inFlight.map((pr) => (
                            <Table.Tr key={pr.id}>
                                <Table.Td>
                                    <Text size="sm">{pr.title}</Text>
                                </Table.Td>
                                <Table.Td>
                                    <Anchor href={`/devops/${pr.commitId}`} size="sm" ff="monospace">
                                        {pr.commitId.slice(0, 8)}
                                    </Anchor>
                                </Table.Td>
                                {TASK_NAMES.map((task) => (
                                    <Table.Td key={task}>
                                        <TaskBadge task={task} state={pr.tasks?.[task]} pr={pr} />
                                    </Table.Td>
                                ))}
                            </Table.Tr>
                        ))}
                    </Table.Tbody>
                </Table>
            )}

            <Space h={32} />

            <Title order={3} fz={20}>
                Fast queue (pre-commit, drained first)
            </Title>
            <Space h={8} />
            {fastQueue.length === 0 ? (
                <Text c="dimmed" size="sm">
                    Fast queue is empty.
                </Text>
            ) : (
                <QueueTable jobs={fastQueue} titleFor={titleFor} />
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
                <QueueTable jobs={queue} titleFor={titleFor} />
            )}
        </Container>
    );
}
