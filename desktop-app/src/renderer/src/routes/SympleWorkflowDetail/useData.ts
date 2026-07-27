import { useQuery } from '@tanstack/react-query';
import { odooRead, odooSearchRead } from '@/lib/odoo-api';
import { PhaseRecord, WorkflowRecord } from './context';

export default function useData(workflowId: number) {
    const { data: workflow } = useQuery<WorkflowRecord>({
        queryKey: ['symple.workflow', workflowId],
        queryFn: () =>
            odooRead('symple.workflow', [workflowId], ['name', 'triplet_phase_id']).then(
                (r) => r[0]
            ),
    });

    const { data: phases = [] } = useQuery<PhaseRecord[]>({
        queryKey: ['symple.triplet.phase', { workflowId }],
        queryFn: () =>
            odooSearchRead(
                'symple.triplet.phase',
                [['workflow_id', '=', workflowId]],
                ['name', 'set_result_automatically']
            ),
    });

    return { workflow, phases };
}
