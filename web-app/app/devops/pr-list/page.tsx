'use client';

import { useState } from 'react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { Anchor, Badge, Button, Container, Group, Space, Table, Text, Title } from '@mantine/core';
import { fetchPrs, InitStatus, PreCommitStatus, PrRecord, PrStatus, triggerDiscover } from '../actions';

const STATUS_COLOR: Record<PrStatus, string> = {
    passed: 'green',
    failed: 'red',
    unknown: 'orange',
    done: 'teal',
    running: 'yellow',
    queued: 'blue',
    pending: 'gray',
};

const STATUS_LABEL: Record<PrStatus, string> = {
    passed: 'All tests passed',
    failed: 'Test failures detected',
    unknown: 'Unknown failure',
    done: 'Done',
    running: 'Running',
    queued: 'Queued',
    pending: 'Pending',
};

const PRE_COMMIT_COLOR: Record<PreCommitStatus, string> = {
    ok: 'green',
    ko: 'red',
};

const PRE_COMMIT_LABEL: Record<PreCommitStatus, string> = {
    ok: 'pre-commit OK',
    ko: 'pre-commit KO',
};

const INIT_COLOR: Record<InitStatus, string> = {
    ok: 'green',
    ko: 'red',
};

const INIT_LABEL: Record<InitStatus, string> = {
    ok: 'init OK',
    ko: 'init KO',
};

export default function PrListPage() {
    const queryClient = useQueryClient();
    const [discovering, setDiscovering] = useState(false);

    const { data: prs = [], isLoading } = useQuery<PrRecord[]>({
        queryKey: ['devops', 'prs'],
        queryFn: fetchPrs,
        refetchInterval: false,
    });

    async function handleDiscover() {
        setDiscovering(true);
        try {
            await triggerDiscover();
            await queryClient.invalidateQueries({ queryKey: ['devops', 'prs'] });
        } finally {
            setDiscovering(false);
        }
    }

    return (
        <Container size="xl" py="md">
            <Group justify="space-between">
                <Title fz={28}>Pull Requests</Title>
                <Button loading={discovering} onClick={handleDiscover}>
                    Force Discover
                </Button>
            </Group>

            <Space h={32} />

            {isLoading && (
                <Text c="dimmed" size="sm">
                    Loading…
                </Text>
            )}

            {!isLoading && prs.length === 0 && (
                <Text c="dimmed" size="sm">
                    No open pull requests.
                </Text>
            )}

            {prs.length > 0 && (
                <Table striped highlightOnHover>
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th>Title</Table.Th>
                            <Table.Th>Branch</Table.Th>
                            <Table.Th>Author</Table.Th>
                            <Table.Th>Commit</Table.Th>
                            <Table.Th>Status</Table.Th>
                        </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                        {prs.map((pr) => (
                            <Table.Tr key={pr.id}>
                                <Table.Td>
                                    <Group gap="xs" wrap="nowrap">
                                        {pr.isDraft && (
                                            <Badge color="gray" variant="outline" size="xs">Draft</Badge>
                                        )}
                                        {pr.commitId ? (
                                            <Anchor href={`/devops/${pr.commitId}`}>
                                                <Text size="sm" c="cyan">
                                                    {pr.title}
                                                </Text>
                                            </Anchor>
                                        ) : (
                                            <Text size="sm">{pr.title}</Text>
                                        )}
                                    </Group>
                                </Table.Td>
                                <Table.Td>
                                    <Text size="sm" c="dimmed">
                                        {pr.sourceBranch}
                                    </Text>
                                </Table.Td>
                                <Table.Td>
                                    <Text size="sm">{pr.author}</Text>
                                </Table.Td>
                                <Table.Td>
                                    <Text size="sm" ff="monospace" c="dimmed">
                                        {pr.commitId?.slice(0, 8) ?? '—'}
                                    </Text>
                                </Table.Td>
                                <Table.Td>
                                    <Group gap="xs" wrap="nowrap">
                                        <Badge
                                            color={STATUS_COLOR[pr.status]}
                                            variant="light"
                                            size="sm"
                                        >
                                            {STATUS_LABEL[pr.status]}
                                        </Badge>
                                        {pr.preCommitStatus && (
                                            <Badge
                                                color={PRE_COMMIT_COLOR[pr.preCommitStatus]}
                                                variant="outline"
                                                size="sm"
                                            >
                                                {PRE_COMMIT_LABEL[pr.preCommitStatus]}
                                            </Badge>
                                        )}
                                        {pr.initStatus && (
                                            <Badge
                                                color={INIT_COLOR[pr.initStatus]}
                                                variant="outline"
                                                size="sm"
                                            >
                                                {INIT_LABEL[pr.initStatus]}
                                            </Badge>
                                        )}
                                    </Group>
                                </Table.Td>
                            </Table.Tr>
                        ))}
                    </Table.Tbody>
                </Table>
            )}
        </Container>
    );
}
