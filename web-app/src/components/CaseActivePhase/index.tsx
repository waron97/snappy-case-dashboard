import { useEffect, useState } from 'react';
import { IconLock, IconLockX } from '@tabler/icons-react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { toast, ToastContainer } from 'react-toastify';
import { Alert, Button, Center, Group, Select, Stack, Text } from '@mantine/core';
import { odooCallMethod, odooRead, odooSearchRead, odooWrite, OneToMany } from '../../../app/api';
import PhaseResultSelector from '../PhaseResultSelector';
import PythonEditor from '../PythonEditor';
import UiCard from '../UiCard';

type Props = {
    caseId: number;
    workflowId?: number;
    activePhaseId?: number;
};

export default function CaseActivePhase(props: Props) {
    const { caseId, workflowId } = props;

    // -------------------------------------
    // Hooks
    // -------------------------------------

    const [isLocked, setIsLocked] = useState(true);

    const [form, setForm] = useState<{ phase: number | null; code: string }>({
        phase: null,
        code: '',
    });

    const queryClient = useQueryClient();

    // -------------------------------------
    // Queries
    // -------------------------------------

    const { data: [caseFields] = [] } = useQuery<{ triplet_active_phase_id: OneToMany }[]>({
        queryKey: ['case', caseId, 'for-active-phase'],
        refetchInterval: isLocked ? 3 * 1000 : undefined,
        queryFn: () => odooRead('helpdesk.ticket', [caseId], ['triplet_active_phase_id']),
    });

    const { data: workflowPhases } = useQuery<{ id: number; name: string }[]>({
        queryKey: ['workflow', 'phases', { workflowId }],
        enabled: !!workflowId,
        queryFn: () =>
            odooSearchRead(
                'symple.triplet.phase',
                [['workflow_id', '=', workflowId!]],
                ['id', 'name']
            ),
    });

    const activePhaseId = caseFields?.triplet_active_phase_id?.[0];

    const { data: [activePhaseData] = [] } = useQuery<
        {
            id: number;
            code: string;
            set_result_automatically: string;
        }[]
    >({
        queryKey: ['phase', activePhaseId, 'for-active-phase'],
        enabled: !!activePhaseId,
        queryFn: () =>
            odooRead('symple.triplet.phase', [activePhaseId], ['code', 'set_result_automatically']),
    });

    const phaseIdToFetch = form.phase;

    const { data: [selectedPhaseData] = [] } = useQuery<
        {
            id: number;
            code: string;
            set_result_automatically: string;
        }[]
    >({
        queryKey: ['phase', phaseIdToFetch, 'for-active-phase'],
        enabled: !!phaseIdToFetch,
        queryFn: () =>
            odooRead(
                'symple.triplet.phase',
                [phaseIdToFetch!],
                ['code', 'set_result_automatically']
            ),
    });

    const [submitting, setSubmitting] = useState(false);
    const [relaunching, setRelaunching] = useState(false);

    // -------------------------------------
    // Effects
    // -------------------------------------

    useEffect(() => {
        if (caseFields) {
            setForm({ ...form, phase: caseFields.triplet_active_phase_id[0] });
        }
    }, [caseFields]);

    useEffect(() => {
        if (selectedPhaseData) {
            setForm({ ...form, phase: selectedPhaseData.id, code: selectedPhaseData.code });
        }
    }, [selectedPhaseData]);

    // -------------------------------------
    // Functions
    // -------------------------------------

    async function handleSubmitError(err: unknown) {
        if (err instanceof Error) {
            toast(err.message);
            // eslint-disable-next-line
            console.error(err);
        } else {
            toast('Unknown error. Check browser console.');
            // eslint-disable-next-line
            console.error(err);
        }
    }

    async function saveCode() {
        await odooWrite('symple.triplet.phase', [form.phase!], { code: form.code });
        queryClient.invalidateQueries({ queryKey: ['phase', form.phase, 'for-active-phase'] });
    }

    async function submit() {
        setSubmitting(true);
        try {
            await odooWrite(
                'helpdesk.ticket',
                [caseId],
                { triplet_phase_id: form.phase },
                { bypass_ticket_check_write_allowed: true }
            );
            queryClient.invalidateQueries({ queryKey: ['case', caseId, 'for-active-phase'] });
            queryClient.invalidateQueries({ queryKey: ['case-history', caseId] });
            setIsLocked(true);
        } catch (err) {
            handleSubmitError(err);
        } finally {
            setSubmitting(false);
        }
    }

    async function relaunch() {
        setRelaunching(true);
        try {
            await odooCallMethod('helpdesk.ticket', [caseId], 'run_code_and_set_result');
            queryClient.invalidateQueries({ queryKey: ['case', caseId, 'for-active-phase'] });
            queryClient.invalidateQueries({ queryKey: ['logs', caseId] });
        } catch (err) {
            if (err instanceof Error) {
                toast(err.message);
                // eslint-disable-next-line
                console.error(err);
            } else {
                toast('Unknown error. Check browser console.');
                // eslint-disable-next-line
                console.error(err);
            }
        } finally {
            setRelaunching(false);
        }
    }

    function handleLock() {
        if (isLocked) {
            setIsLocked(false);
        } else {
            setIsLocked(true);
            setForm({
                phase: caseFields.triplet_active_phase_id[0],
                code: activePhaseData?.code || '',
            });
        }
    }

    function getChangedFields(): { anyChanged: boolean; phase: boolean; code: boolean } {
        if (isLocked) {
            return { anyChanged: false, phase: false, code: false };
        }
        const phase = form.phase !== caseFields?.triplet_active_phase_id?.[0];
        const code = !!(selectedPhaseData?.code && form.code !== selectedPhaseData?.code);
        return { anyChanged: phase || code, phase, code };
    }

    function renderCodeEditor(codeChanged: boolean) {
        if (isLocked || !form.code || selectedPhaseData?.set_result_automatically !== 'from_code') {
            return null;
        }
        return (
            <PythonEditor
                value={form.code || ''}
                readOnly={isLocked}
                onChange={(newCode) => setForm({ ...form, code: newCode })}
                onSave={codeChanged ? saveCode : undefined}
            />
        );
    }

    function renderContent() {
        if (!workflowId) {
            return (
                <Center>
                    <Text c="red">Case has no workflow</Text>
                </Center>
            );
        }

        const { phase: phaseChanged, code: codeChanged } = getChangedFields();

        return (
            <Stack gap="md">
                {phaseChanged && (
                    <Alert color="yellow" mb="md" title="Unsaved changes">
                        <Text size="sm">The ticket will be moved to the selected phase.</Text>
                        {codeChanged && (
                            <Text size="sm" c="red" mt="xs">
                                Unsaved code changes will be lost.
                            </Text>
                        )}
                        <Group mt="sm" gap="xs">
                            <Button size="xs" color="green" onClick={submit} loading={submitting}>
                                Submit
                            </Button>
                            <Button
                                size="xs"
                                variant="subtle"
                                onClick={() => {
                                    setForm({
                                        ...form,
                                        phase: caseFields.triplet_active_phase_id[0],
                                        code: '',
                                    });
                                }}
                            >
                                Reset
                            </Button>
                        </Group>
                    </Alert>
                )}
                <Select
                    label="Active phase"
                    disabled={isLocked}
                    searchable
                    data={
                        workflowPhases?.map((phase) => ({
                            label: phase.name,
                            value: String(phase.id),
                        })) || []
                    }
                    value={String(phaseIdToFetch)}
                    onChange={(v) => setForm({ ...form, phase: v ? parseInt(v, 10) : null })}
                />
                {renderCodeEditor(codeChanged)}
            </Stack>
        );
    }

    // -------------------------------------
    // Local Variables
    // -------------------------------------

    // -------------------------------------

    return (
        <UiCard
            title="Active phase"
            rightElement={
                <Group gap="sm">
                    <Button onClick={relaunch} loading={relaunching}>
                        Relaunch phase
                    </Button>
                    <PhaseResultSelector caseId={caseId} activePhaseId={activePhaseId} />
                    <Button onClick={handleLock}>
                        <Group gap="sm">
                            <Text>{isLocked ? 'Unlock' : 'Lock'}</Text>
                            {isLocked ? <IconLockX /> : <IconLock />}
                        </Group>
                    </Button>
                </Group>
            }
        >
            {renderContent()}
            <ToastContainer />
        </UiCard>
    );
}
