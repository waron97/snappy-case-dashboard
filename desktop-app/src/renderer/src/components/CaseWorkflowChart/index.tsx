import { useEffect, useMemo, useState } from 'react';
import { odooRead, odooSearchRead, OneToMany } from '@/lib/odoo-api';
import { useQuery } from '@tanstack/react-query';
import WorkflowFlowChart from '../WorkflowFlowChart';

type CaseHistory = {
    id: number;
    active_phase_id: OneToMany;
    phase_result_id: OneToMany;
    phase_id: OneToMany;
    error_message?: string;
    date: string;
};

export default function CaseWorkflowChart({
    workflowId,
    caseId,
    activePhaseId,
}: {
    workflowId: number;
    caseId: number;
    activePhaseId?: number;
}) {
    // -------------------------------------
    // Hooks
    // -------------------------------------

    const [isCaseDone, setIsCaseDone] = useState(false);

    // -------------------------------------
    // Queries
    // -------------------------------------

    const { data: workflowFields } = useQuery<{ id: number; triplet_phase_id: OneToMany }>({
        queryKey: ['symple.workflow', workflowId, 'for-workflow-chart'],
        queryFn: () =>
            odooRead('symple.workflow', [workflowId], ['triplet_phase_id']).then((res) => res[0]),
    });

    const { data: [caseFields] = [] } = useQuery<
        { triplet_active_phase_id: OneToMany; stage_id: OneToMany }[]
    >({
        queryKey: ['helpdesk.ticket', caseId, 'for-workflow-chart'],
        refetchInterval: isCaseDone ? undefined : 3 * 1000,
        queryFn: () =>
            odooRead('helpdesk.ticket', [caseId], ['triplet_active_phase_id', 'stage_id']),
    });

    const { data: caseHistory } = useQuery<CaseHistory[]>({
        queryKey: ['symple.triplet.phase.history', caseId],
        refetchInterval: isCaseDone ? undefined : 3 * 1000,
        enabled: !!caseId,
        queryFn: () =>
            odooSearchRead(
                'symple.triplet.phase.history',
                [['ticket_id', '=', caseId]],
                ['active_phase_id', 'phase_result_id', 'error_message', 'date', 'phase_id'],
                0,
                undefined,
                'id desc'
            ),
    });

    const [crossedPhases, crossedResults] = useMemo(() => {
        const crossedPhases = new Set<number>();
        const crossedResults = new Set<number>();

        if (!caseHistory) {
            return [crossedResults, crossedResults];
        }

        caseHistory.forEach((entry) => {
            if (entry?.phase_id?.[0]) {
                crossedPhases.add(entry.phase_id[0]);
            }

            if (entry.phase_result_id?.[0]) {
                crossedResults.add(entry.phase_result_id[0]);
            }
        });

        return [crossedPhases, crossedResults];
    }, [caseHistory]);

    // -------------------------------------
    // Effects
    // -------------------------------------

    useEffect(() => {
        const stage = caseFields?.stage_id?.[1];
        if (
            stage === 'Solved' ||
            stage === 'Cancelled' ||
            stage === 'Done KO' ||
            stage === 'Done'
        ) {
            setIsCaseDone(true);
        } else {
            setIsCaseDone(false);
        }
    }, [caseFields]);

    // -------------------------------------
    // Functions
    // -------------------------------------

    // -------------------------------------
    // Local Variables
    // -------------------------------------

    // -------------------------------------

    return (
        <WorkflowFlowChart
            workflowId={workflowId}
            crossedPhases={crossedPhases}
            crossedResults={crossedResults}
            activePhaseId={caseFields?.triplet_active_phase_id?.[0] || activePhaseId}
            startPhaseId={workflowFields?.triplet_phase_id?.[0]}
        />
    );
}
