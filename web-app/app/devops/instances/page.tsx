'use client';

import { useEffect, useRef, useState } from 'react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import {
    Anchor,
    Badge,
    Button,
    Card,
    Collapse,
    Container,
    Group,
    Loader,
    Select,
    Space,
    Table,
    Text,
    TextInput,
    Title,
    Tooltip,
} from '@mantine/core';
import { InstanceStatusBadge } from '@/components/InstanceStatusBadge';
import {
    attachInstance,
    Copy,
    createCopy,
    deleteCopy,
    detachInstance,
    fetchCopies,
    fetchInstance,
    fetchInstanceLog,
    fetchLocalAddonsFolders,
    fetchPrs,
    fetchSources,
    fetchSuggestedUpgrades,
    InstanceStatus,
    PrRecord,
    resetSource,
    restartInstance,
    Source,
    syncInstance,
    syncLocalInstance,
} from '../actions';

function formatCreatedAt(unixSeconds: number): string {
    return new Date(unixSeconds * 1000).toLocaleString();
}

function copyStatusBadge(copy: Copy) {
    if (copy.status === 'creating') {
        return (
            <Badge color="yellow" variant="light" size="sm" tt="none">
                <Group gap={6} wrap="nowrap">
                    <Loader size={10} color="yellow" />
                    creating
                </Group>
            </Badge>
        );
    }
    if (copy.status === 'failed') {
        return (
            <Tooltip label={copy.error ?? 'unknown error'} multiline w={320}>
                <Badge color="red" variant="light" size="sm" tt="none">
                    failed
                </Badge>
            </Tooltip>
        );
    }
    return (
        <Badge color="green" variant="light" size="sm" tt="none">
            ready
        </Badge>
    );
}

export default function InstancesPage() {
    const queryClient = useQueryClient();

    const { data: sources = [] } = useQuery<Source[]>({
        queryKey: ['devops', 'sources'],
        queryFn: fetchSources,
        refetchInterval: 5_000,
    });

    const { data: copies = [] } = useQuery<Copy[]>({
        queryKey: ['devops', 'copies'],
        queryFn: fetchCopies,
        refetchInterval: 5_000,
    });

    const { data: instance } = useQuery<InstanceStatus>({
        queryKey: ['devops', 'instance'],
        queryFn: fetchInstance,
        refetchInterval: 3_000,
    });

    const { data: prs = [] } = useQuery<PrRecord[]>({
        queryKey: ['devops', 'prs'],
        queryFn: fetchPrs,
        refetchInterval: 10_000,
    });

    const { data: localFolders = [] } = useQuery<string[]>({
        queryKey: ['devops', 'local-addons'],
        queryFn: fetchLocalAddonsFolders,
        refetchInterval: 30_000,
    });

    const [logOpen, setLogOpen] = useState(false);
    const { data: logData } = useQuery<{ log: string }>({
        queryKey: ['devops', 'instance-log'],
        queryFn: fetchInstanceLog,
        refetchInterval: logOpen ? 5_000 : false,
        enabled: logOpen,
    });

    // Follow the tail like `tail -f` on each poll, but only while the user hasn't
    // scrolled up to read earlier output — otherwise every 5s refresh yanks them back
    // to the bottom mid-read, which is the "jank" a plain polled <pre> block produces.
    const logBoxRef = useRef<HTMLPreElement>(null);
    const pinnedToBottomRef = useRef(true);

    function handleLogScroll() {
        const el = logBoxRef.current;
        if (!el) {
            return;
        }
        pinnedToBottomRef.current = el.scrollHeight - el.scrollTop - el.clientHeight < 40;
    }

    useEffect(() => {
        const el = logBoxRef.current;
        if (el && pinnedToBottomRef.current) {
            el.scrollTop = el.scrollHeight;
        }
    }, [logData?.log]);

    useEffect(() => {
        // Reopening always starts pinned to the tail, regardless of where it was left.
        if (logOpen) {
            pinnedToBottomRef.current = true;
        }
    }, [logOpen]);

    function invalidateSources() {
        return queryClient.invalidateQueries({ queryKey: ['devops', 'sources'] });
    }
    function invalidateCopies() {
        return queryClient.invalidateQueries({ queryKey: ['devops', 'copies'] });
    }
    function invalidateInstance() {
        return queryClient.invalidateQueries({ queryKey: ['devops', 'instance'] });
    }

    // --- sources: reset base -------------------------------------------------

    const [resettingSource, setResettingSource] = useState<string | null>(null);
    const [sourceError, setSourceError] = useState<string | null>(null);

    async function handleResetSource(id: string) {
        setResettingSource(id);
        setSourceError(null);
        const result = await resetSource(id);
        if (!result.ok) {
            setSourceError(result.error);
        } else {
            await invalidateSources();
        }
        setResettingSource(null);
    }

    // --- copies: create / delete / attach ------------------------------------

    const [newName, setNewName] = useState('');
    const [newSource, setNewSource] = useState<string | null>(null);
    const [creating, setCreating] = useState(false);
    const [createError, setCreateError] = useState<string | null>(null);

    async function handleCreateCopy() {
        setCreating(true);
        setCreateError(null);
        const result = await createCopy(newName, newSource ?? '');
        if (!result.ok) {
            setCreateError(result.error);
        } else {
            setNewName('');
            await invalidateCopies();
        }
        setCreating(false);
    }

    const [deletingCopy, setDeletingCopy] = useState<string | null>(null);
    const [copyError, setCopyError] = useState<string | null>(null);

    async function handleDeleteCopy(name: string) {
        setDeletingCopy(name);
        setCopyError(null);
        const result = await deleteCopy(name);
        if (!result.ok) {
            setCopyError(result.error);
        } else {
            await Promise.all([invalidateCopies(), invalidateInstance()]);
        }
        setDeletingCopy(null);
    }

    const [attachingCopy, setAttachingCopy] = useState<string | null>(null);

    async function handleAttachCopy(name: string) {
        setAttachingCopy(name);
        setInstanceError(null);
        const result = await attachInstance(name, installField || undefined, upgradeField || undefined);
        if (!result.ok) {
            setInstanceError(result.error);
        } else {
            await invalidateInstance();
        }
        setAttachingCopy(null);
    }

    // --- instance panel --------------------------------------------------------

    const [installField, setInstallField] = useState('');
    const [upgradeField, setUpgradeField] = useState('');
    const lastDbRef = useRef<string | null | undefined>(undefined);

    useEffect(() => {
        if (!instance) {
            return;
        }
        // Only reset the fields when the attached copy itself changes (attach/detach),
        // not on every poll — otherwise in-progress edits would be clobbered every 3s.
        if (instance.db !== lastDbRef.current) {
            lastDbRef.current = instance.db;
            setInstallField(instance.install ?? '');
            setUpgradeField(instance.upgrade ?? '');
        }
    }, [instance]);

    const [instanceError, setInstanceError] = useState<string | null>(null);
    const [restarting, setRestarting] = useState(false);
    const [detaching, setDetaching] = useState(false);
    const [suggesting, setSuggesting] = useState(false);
    const [syncing, setSyncing] = useState(false);
    const [selectedPrId, setSelectedPrId] = useState<string | null>(null);

    async function handleRestart() {
        setRestarting(true);
        setInstanceError(null);
        const result = await restartInstance(installField || undefined, upgradeField || undefined);
        if (!result.ok) {
            setInstanceError(result.error);
        } else {
            await invalidateInstance();
        }
        setRestarting(false);
    }

    async function handleDetach() {
        setDetaching(true);
        setInstanceError(null);
        const result = await detachInstance();
        if (!result.ok) {
            setInstanceError(result.error);
        } else {
            await invalidateInstance();
        }
        setDetaching(false);
    }

    async function handleSuggestUpgrades() {
        setSuggesting(true);
        setInstanceError(null);
        const result = await fetchSuggestedUpgrades();
        if (!result.ok) {
            setInstanceError(result.error);
        } else {
            setUpgradeField(result.data.modules.join(','));
        }
        setSuggesting(false);
    }

    async function handleSync() {
        if (!selectedPrId) {
            return;
        }
        setSyncing(true);
        setInstanceError(null);
        const result = await syncInstance(Number(selectedPrId));
        if (!result.ok) {
            setInstanceError(result.error);
        } else {
            await invalidateInstance();
        }
        setSyncing(false);
    }

    const [selectedLocalPath, setSelectedLocalPath] = useState<string | null>(null);
    const [syncingLocal, setSyncingLocal] = useState(false);

    async function handleSyncLocal() {
        if (!selectedLocalPath) {
            return;
        }
        setSyncingLocal(true);
        setInstanceError(null);
        const result = await syncLocalInstance(selectedLocalPath);
        if (!result.ok) {
            setInstanceError(result.error);
        } else {
            await invalidateInstance();
        }
        setSyncingLocal(false);
    }

    const sourceOptions = sources.map((s) => ({ value: s.id, label: s.id }));
    const prOptions = prs.map((pr) => ({ value: String(pr.id), label: `#${pr.id} ${pr.title}` }));
    const localFolderOptions = localFolders.map((f) => ({ value: f, label: f }));

    return (
        <Container size="xl" py="md">
            <Title fz={28}>Instances</Title>
            <Space h={24} />

            {/* --- Sources --- */}
            <Title order={3} fz={20}>
                Sources
            </Title>
            <Space h={8} />
            <Table striped highlightOnHover>
                <Table.Thead>
                    <Table.Tr>
                        <Table.Th>Source</Table.Th>
                        <Table.Th>Base DB</Table.Th>
                        <Table.Th w={140}>Status</Table.Th>
                        <Table.Th w={160} />
                    </Table.Tr>
                </Table.Thead>
                <Table.Tbody>
                    {sources.map((s) => (
                        <Table.Tr key={s.id}>
                            <Table.Td>
                                <Text size="sm" ff="monospace">
                                    {s.id}
                                </Text>
                            </Table.Td>
                            <Table.Td>
                                <Text size="sm" c="dimmed">
                                    {s.baseDb}
                                </Text>
                            </Table.Td>
                            <Table.Td>
                                {s.resetting ? (
                                    <Badge color="yellow" variant="light" size="sm" tt="none">
                                        <Group gap={6} wrap="nowrap">
                                            <Loader size={10} color="yellow" />
                                            resetting
                                        </Group>
                                    </Badge>
                                ) : (
                                    <Badge color={s.ready ? 'green' : 'gray'} variant="light" size="sm" tt="none">
                                        {s.ready ? 'ready' : 'not ready'}
                                    </Badge>
                                )}
                            </Table.Td>
                            <Table.Td>
                                <Button
                                    size="xs"
                                    variant="outline"
                                    color="orange"
                                    disabled={s.resetting}
                                    loading={resettingSource === s.id}
                                    onClick={() => handleResetSource(s.id)}
                                >
                                    Reset base
                                </Button>
                            </Table.Td>
                        </Table.Tr>
                    ))}
                </Table.Tbody>
            </Table>
            {sourceError && (
                <Text c="red" size="sm" mt="xs">
                    {sourceError}
                </Text>
            )}

            <Space h={32} />

            {/* --- Copies --- */}
            <Title order={3} fz={20}>
                Copies
            </Title>
            <Space h={8} />
            <Card withBorder radius="md" padding="sm">
                <Group align="flex-end">
                    <TextInput
                        label="Name"
                        placeholder="my-feature"
                        value={newName}
                        onChange={(e) => setNewName(e.currentTarget.value)}
                        size="sm"
                    />
                    <Select
                        label="Source"
                        placeholder="test-01 / test-02"
                        data={sourceOptions}
                        value={newSource}
                        onChange={setNewSource}
                        size="sm"
                        w={160}
                    />
                    <Button
                        size="sm"
                        loading={creating}
                        disabled={!newName || !newSource}
                        onClick={handleCreateCopy}
                    >
                        Create
                    </Button>
                </Group>
                {createError && (
                    <Text c="red" size="sm" mt="xs">
                        {createError}
                    </Text>
                )}
            </Card>
            <Space h={12} />
            {copyError && (
                <Text c="red" size="sm" mb="xs">
                    {copyError}
                </Text>
            )}
            {copies.length === 0 ? (
                <Text c="dimmed" size="sm">
                    No copies yet.
                </Text>
            ) : (
                <Table striped highlightOnHover>
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th>Name</Table.Th>
                            <Table.Th>Source</Table.Th>
                            <Table.Th>Created</Table.Th>
                            <Table.Th w={100}>Status</Table.Th>
                            <Table.Th w={120}>Attach</Table.Th>
                            <Table.Th w={90}>Delete</Table.Th>
                        </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                        {copies.map((c) => {
                            const isAttached = instance?.db === `dev_${c.name}`;
                            return (
                                <Table.Tr key={c.name}>
                                    <Table.Td>
                                        <Text size="sm" ff="monospace">
                                            {c.name}
                                        </Text>
                                    </Table.Td>
                                    <Table.Td>
                                        <Text size="sm" c="dimmed">
                                            {c.source}
                                        </Text>
                                    </Table.Td>
                                    <Table.Td>
                                        <Text size="sm">{formatCreatedAt(c.createdAt)}</Text>
                                    </Table.Td>
                                    <Table.Td>{copyStatusBadge(c)}</Table.Td>
                                    <Table.Td>
                                        <Button
                                            size="xs"
                                            variant={isAttached ? 'filled' : 'outline'}
                                            color={isAttached ? 'green' : 'blue'}
                                            disabled={c.status !== 'ready' || isAttached}
                                            loading={attachingCopy === c.name}
                                            onClick={() => handleAttachCopy(c.name)}
                                        >
                                            {isAttached ? 'Attached' : 'Attach'}
                                        </Button>
                                    </Table.Td>
                                    <Table.Td>
                                        <Button
                                            size="xs"
                                            variant="outline"
                                            color="red"
                                            loading={deletingCopy === c.name}
                                            onClick={() => handleDeleteCopy(c.name)}
                                        >
                                            Delete
                                        </Button>
                                    </Table.Td>
                                </Table.Tr>
                            );
                        })}
                    </Table.Tbody>
                </Table>
            )}

            <Space h={32} />

            {/* --- Instance --- */}
            <Title order={3} fz={20}>
                Odoo Instance
            </Title>
            <Space h={8} />
            <Card withBorder radius="md" padding="md">
                <Group justify="space-between" align="center">
                    <Group gap="md">
                        {instance && <InstanceStatusBadge status={instance.status} />}
                        <Text size="sm" ff="monospace" c="dimmed">
                            {instance?.db ?? '—'}
                        </Text>
                    </Group>
                    {instance?.url && (
                        <Anchor href={instance.url} target="_blank" size="sm">
                            Open Odoo (localhost:8069)
                        </Anchor>
                    )}
                </Group>

                <Space h={8} />
                <Group gap="lg">
                    <Text size="sm" c="dimmed">
                        Synced:{' '}
                        {instance?.syncedPr ? (
                            <Anchor href={`/devops/${instance.syncedCommit}`} size="sm" ff="monospace">
                                #{instance.syncedPr} ({instance.syncedCommit?.slice(0, 8)})
                            </Anchor>
                        ) : instance?.syncedLocal ? (
                            <Text component="span" size="sm" ff="monospace">
                                local: {instance.syncedLocal}
                            </Text>
                        ) : (
                            '—'
                        )}
                    </Text>
                    <Text size="sm" c="dimmed">
                        Started: {instance?.startedAt ? formatCreatedAt(instance.startedAt) : '—'}
                    </Text>
                </Group>

                {instance?.error && (
                    <Text c="red" size="sm" mt="xs">
                        {instance.error}
                    </Text>
                )}

                <Space h={16} />
                <Group align="flex-end">
                    <Select
                        label="Sync PR"
                        placeholder="pick a PR"
                        data={prOptions}
                        value={selectedPrId}
                        onChange={setSelectedPrId}
                        size="sm"
                        w={320}
                        searchable
                    />
                    <Button size="sm" loading={syncing} disabled={!selectedPrId} onClick={handleSync}>
                        Sync
                    </Button>
                </Group>

                <Space h={12} />
                <Group align="flex-end">
                    <Select
                        label="Sync local folder"
                        placeholder={localFolderOptions.length ? 'pick a folder' : 'none found (mount not configured?)'}
                        data={localFolderOptions}
                        value={selectedLocalPath}
                        onChange={setSelectedLocalPath}
                        size="sm"
                        w={320}
                        searchable
                        disabled={localFolderOptions.length === 0}
                    />
                    <Button
                        size="sm"
                        loading={syncingLocal}
                        disabled={!selectedLocalPath}
                        onClick={handleSyncLocal}
                    >
                        Sync
                    </Button>
                </Group>

                <Space h={16} />
                <Group align="flex-end">
                    <TextInput
                        label="-i (install)"
                        placeholder="module_a,module_b"
                        value={installField}
                        onChange={(e) => setInstallField(e.currentTarget.value)}
                        size="sm"
                        w={280}
                    />
                    <TextInput
                        label="-u (upgrade)"
                        placeholder="module_a,module_b"
                        value={upgradeField}
                        onChange={(e) => setUpgradeField(e.currentTarget.value)}
                        size="sm"
                        w={280}
                    />
                    <Button
                        size="sm"
                        variant="outline"
                        loading={suggesting}
                        disabled={instance?.status !== 'running'}
                        onClick={handleSuggestUpgrades}
                    >
                        Suggest -u
                    </Button>
                </Group>

                <Space h={16} />
                <Text size="xs" c="dimmed">
                    Restart re-pulls the currently synced PR or local folder before relaunching.
                </Text>
                <Space h={4} />
                <Group>
                    <Button
                        size="sm"
                        variant="outline"
                        loading={restarting}
                        disabled={!instance?.db}
                        onClick={handleRestart}
                    >
                        Restart
                    </Button>
                    <Button
                        size="sm"
                        variant="outline"
                        color="red"
                        loading={detaching}
                        disabled={!instance?.db}
                        onClick={handleDetach}
                    >
                        Detach
                    </Button>
                    <Button size="sm" variant="subtle" onClick={() => setLogOpen((o) => !o)}>
                        {logOpen ? 'Hide log' : 'Show log'}
                    </Button>
                </Group>

                {instanceError && (
                    <Text c="red" size="sm" mt="xs">
                        {instanceError}
                    </Text>
                )}

                <Collapse in={logOpen}>
                    <Space h={12} />
                    <Text
                        ref={logBoxRef}
                        component="pre"
                        onScroll={handleLogScroll}
                        ff="monospace"
                        fz="xs"
                        p="sm"
                        style={{
                            maxHeight: 400,
                            overflow: 'auto',
                            backgroundColor: 'var(--mantine-color-dark-8)',
                            borderRadius: 4,
                            whiteSpace: 'pre-wrap',
                        }}
                    >
                        {logData?.log ?? 'Loading…'}
                    </Text>
                </Collapse>
            </Card>
        </Container>
    );
}
