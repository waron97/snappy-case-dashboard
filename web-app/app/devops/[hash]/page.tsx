'use client';

import { useEffect, useRef, useState } from 'react';
import { useParams } from 'next/navigation';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { Badge, Button, Container, Group, Space, Tabs, Text, Title } from '@mantine/core';
import LogViewer from '@/components/LogViewer';
import { fetchPrs, getRunningHashes, InitStatus, PreCommitStatus, PrRecord, PrStatus, readLog, readPreCommitLog, triggerNotify, triggerRecheck, triggerRecheckByPrId } from '../actions';

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

export default function PrDetailPage() {
    const params = useParams();
    const hash = params.hash as string;
    const queryClient = useQueryClient();
    const [rechecking, setRechecking] = useState(false);
    const [notifying, setNotifying] = useState(false);

    const { data: prs = [] } = useQuery<PrRecord[]>({
        queryKey: ['devops', 'prs'],
        queryFn: fetchPrs,
        refetchInterval: 10_000,
    });

    const { data: runningHashes = [] } = useQuery<string[]>({
        queryKey: ['devops', 'running'],
        queryFn: getRunningHashes,
        refetchInterval: 1_000,
    });

    const pr = prs.find((p) => p.commitId === hash) ?? null;
    const isRunning = runningHashes.includes(hash);
    const status: PrStatus = isRunning ? 'running' : (pr?.status ?? 'pending');
    const isActive = isRunning || status === 'queued';

    // When active→inactive, fire one final log fetch to capture last bytes
    const wasActive = useRef(false);
    useEffect(() => {
        if (wasActive.current && !isActive) {
            void queryClient.invalidateQueries({ queryKey: ['devops', 'log', hash] });
        }
        wasActive.current = isActive;
    }, [isActive, hash, queryClient]);

    const { data: installLog } = useQuery<string | null>({
        queryKey: ['devops', 'log', hash, 'install'],
        queryFn: () => readLog(hash, 'install'),
        refetchInterval: isActive ? 1_000 : false,
        gcTime: 0,
    });

    const { data: testLog } = useQuery<string | null>({
        queryKey: ['devops', 'log', hash, 'test'],
        queryFn: () => readLog(hash, 'test'),
        refetchInterval: isActive ? 1_000 : false,
        gcTime: 0,
    });

    const { data: preCommitLog } = useQuery<string | null>({
        queryKey: ['devops', 'log', hash, 'precommit'],
        queryFn: () => readPreCommitLog(hash),
        refetchInterval: isActive ? 1_000 : false,
        gcTime: 0,
    });

    const { data: initLog } = useQuery<string | null>({
        queryKey: ['devops', 'log', hash, 'init'],
        queryFn: () => readLog(hash, 'init'),
        refetchInterval: isActive ? 1_000 : false,
        gcTime: 0,
    });

    async function handleNotify() {
        setNotifying(true);
        try {
            await triggerNotify(hash);
        } finally {
            setNotifying(false);
        }
    }

    async function handleRecheck() {
        setRechecking(true);
        try {
            if (pr) {
                await triggerRecheckByPrId(pr.id);
            } else {
                await triggerRecheck(hash);
            }
            await queryClient.invalidateQueries({ queryKey: ['devops', 'prs'] });
        } finally {
            setRechecking(false);
        }
    }

    return (
        <Container size="xl" py="md">
            <Group justify="space-between">
                <Group gap="sm" align="center">
                    <Title fz={28}>{pr?.title ?? hash.slice(0, 12)}</Title>
                    <Badge color={STATUS_COLOR[status]} variant="light">
                        {STATUS_LABEL[status]}
                    </Badge>
                    {pr?.preCommitStatus && (
                        <Badge
                            color={PRE_COMMIT_COLOR[pr.preCommitStatus]}
                            variant="outline"
                        >
                            {PRE_COMMIT_LABEL[pr.preCommitStatus]}
                        </Badge>
                    )}
                    {pr?.initStatus && (
                        <Badge color={INIT_COLOR[pr.initStatus]} variant="outline">
                            {INIT_LABEL[pr.initStatus]}
                        </Badge>
                    )}
                </Group>
                <Group gap="sm">
                    {pr?.sourceBranch && (
                        <Text size="sm" c="dimmed" ff="monospace">
                            {pr.sourceBranch}
                        </Text>
                    )}
                    {!['pending', 'queued', 'running'].includes(status) && (
                        <Button loading={notifying} onClick={handleNotify} variant="default">
                            Force Notify
                        </Button>
                    )}
                    <Button loading={rechecking} onClick={handleRecheck}>
                        Force Recheck
                    </Button>
                </Group>
            </Group>

            <Space h={8} />
            <Text size="sm" c="dimmed" ff="monospace">
                {hash}
            </Text>

            <Space h={24} />

            <Tabs defaultValue="install">
                <Tabs.List>
                    <Tabs.Tab value="install">Install Log</Tabs.Tab>
                    <Tabs.Tab value="test">Test Log</Tabs.Tab>
                    <Tabs.Tab value="precommit">Pre-commit Log</Tabs.Tab>
                    <Tabs.Tab value="init">Init Log</Tabs.Tab>
                </Tabs.List>

                <Tabs.Panel value="install" pt="md">
                    <LogViewer content={installLog ?? null} />
                </Tabs.Panel>

                <Tabs.Panel value="test" pt="md">
                    <LogViewer content={testLog ?? null} />
                </Tabs.Panel>

                <Tabs.Panel value="precommit" pt="md">
                    <LogViewer content={preCommitLog ?? null} />
                </Tabs.Panel>

                <Tabs.Panel value="init" pt="md">
                    <LogViewer content={initLog ?? null} />
                </Tabs.Panel>
            </Tabs>
        </Container>
    );
}
