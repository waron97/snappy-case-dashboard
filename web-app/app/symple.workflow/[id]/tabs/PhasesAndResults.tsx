'use client';

import { useEffect, useState } from 'react';
import { IconSearch } from '@tabler/icons-react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { Badge, Grid, Group, Input, NavLink, ScrollArea, Stack, Switch, Text } from '@mantine/core';
import PythonEditor from '@/components/PythonEditor';
import UiCard from '@/components/UiCard';
import { odooRead, odooWrite } from '../../../api';
import { PhaseRecord, useWorkflowContext } from '../context';

function fuzzyMatch(name: string, query: string): boolean {
    if (!query) {
        return true;
    }
    const haystack = name.toLowerCase();
    const needle = query.toLowerCase();
    let hi = 0;
    for (let ni = 0; ni < needle.length; ni++) {
        hi = haystack.indexOf(needle[ni], hi);
        if (hi === -1) {
            return false;
        }
        hi++;
    }
    return true;
}

export default function PhasesAndResults() {
    const { workflow, phases } = useWorkflowContext();
    const queryClient = useQueryClient();

    const [selectedPhaseId, setSelectedPhaseId] = useState<number | null>(null);
    const [search, setSearch] = useState('');
    const [automaticOnly, setAutomaticOnly] = useState(true);
    const [code, setCode] = useState('');

    useEffect(() => {
        if (workflow?.triplet_phase_id) {
            setSelectedPhaseId(workflow.triplet_phase_id[0]);
        }
    }, [workflow?.triplet_phase_id[0]]);

    const selectedPhase = phases.find((p) => p.id === selectedPhaseId) ?? null;

    const codeQueryKey = ['symple.triplet.phase', selectedPhaseId, 'code'];

    const { data: savedCode } = useQuery<string>({
        enabled: selectedPhaseId !== null,
        queryKey: codeQueryKey,
        queryFn: () =>
            odooRead('symple.triplet.phase', [selectedPhaseId!], ['code']).then(
                (r) => r[0].code ?? ''
            ),
    });

    useEffect(() => {
        setCode(savedCode ?? '');
    }, [savedCode]);

    const isDirty = code !== (savedCode ?? '');

    async function saveCode() {
        await odooWrite('symple.triplet.phase', [selectedPhaseId!], { code });
        queryClient.invalidateQueries({ queryKey: codeQueryKey });
    }

    const visiblePhases = phases.filter((phase) => {
        if (phase.id === selectedPhaseId) {
            return true;
        }
        if (automaticOnly && !phase.set_result_automatically) {
            return false;
        }
        return fuzzyMatch(phase.name, search);
    });

    function handleSelect(phase: PhaseRecord) {
        setSelectedPhaseId((prev) => (prev === phase.id ? null : phase.id));
    }

    return (
        <Grid gutter="md">
            <Grid.Col span={8}>
                <UiCard title={selectedPhase?.name}>
                    {!selectedPhase ? (
                        <Text c="dimmed" size="sm">
                            Select a phase
                        </Text>
                    ) : savedCode !== undefined ? (
                        <PythonEditor
                            value={code}
                            onChange={setCode}
                            onSave={isDirty ? saveCode : undefined}
                            maxHeight="800px"
                            height="800px"
                        />
                    ) : null}
                </UiCard>
            </Grid.Col>

            <Grid.Col span={4}>
                <UiCard title="Phases">
                    <Stack gap="xs">
                        <Group justify="space-between" wrap="nowrap">
                            <Input
                                flex={1}
                                size="xs"
                                placeholder="Search…"
                                leftSection={<IconSearch size={14} />}
                                value={search}
                                onChange={(e) => setSearch(e.currentTarget.value)}
                            />
                            <Switch
                                size="xs"
                                label="Auto only"
                                checked={automaticOnly}
                                onChange={(e) => setAutomaticOnly(e.currentTarget.checked)}
                            />
                        </Group>

                        <ScrollArea.Autosize mah={740}>
                            <Stack gap={0}>
                                {visiblePhases.map((phase) => (
                                    <NavLink
                                        key={phase.id}
                                        label={phase.name}
                                        active={selectedPhaseId === phase.id}
                                        onClick={() => handleSelect(phase)}
                                        rightSection={
                                            phase.set_result_automatically ? (
                                                <Badge size="xs" variant="light" color="gray">
                                                    {phase.set_result_automatically}
                                                </Badge>
                                            ) : undefined
                                        }
                                    />
                                ))}

                                {visiblePhases.length === 0 && (
                                    <Text c="dimmed" size="sm">
                                        No phases
                                    </Text>
                                )}
                            </Stack>
                        </ScrollArea.Autosize>
                    </Stack>
                </UiCard>
            </Grid.Col>
        </Grid>
    );
}
