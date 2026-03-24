import { useEffect, useState } from 'react';
import { odooSearchRead } from '@app/api';
import { useQuery } from '@tanstack/react-query';
import { ChartPhase, ChartResult } from './layout';

export default function useWorkflowData(workflowId: number, startPhaseId?: number) {
    // -------------------------------------
    // State
    // -------------------------------------

    const [phases, setPhases] = useState<ChartPhase[]>([]);
    const [results, setResults] = useState<ChartResult[]>([]);

    const [phaseIdsToFill, setPhaseIdsToFill] = useState<number[]>([]);
    const [resultIdsToFill, setResultIdsToFill] = useState<number[]>([]);

    const [isDone, setIsDone] = useState(false);

    // -------------------------------------
    // Queries
    // -------------------------------------

    const { data: initialPhases } = useQuery<ChartPhase[]>({
        enabled: !!workflowId && !isDone,
        queryKey: ['symple.triplet.phase', { workflowId }, 'for-workflow-chart'],
        queryFn: () =>
            odooSearchRead(
                'symple.triplet.phase',
                [['workflow_id', '=', workflowId]],
                ['name', 'allowed_phase_result_ids']
            ),
    });

    const { data: initialResults } = useQuery<ChartResult[]>({
        enabled: !!workflowId && !isDone,
        queryKey: ['symple.triplet.phase.result', { workflowId }, 'for-workflow-chart'],
        queryFn: () =>
            odooSearchRead(
                'symple.triplet.phase.result',
                [['workflow_id', '=', workflowId]],
                ['name', 'starting_phase_ids', 'next_phase_id']
            ),
    });

    const { data: complementPhases } = useQuery<ChartPhase[]>({
        enabled: !!workflowId && phaseIdsToFill.length > 0 && !isDone,
        queryKey: ['symple.triplet.phase', { ids: phaseIdsToFill }, 'for-workflow-chart'],
        queryFn: () =>
            odooSearchRead(
                'symple.triplet.phase',
                [['id', 'in', phaseIdsToFill]],
                ['name', 'allowed_phase_result_ids']
            ),
    });

    const { data: complementResults } = useQuery<ChartResult[]>({
        enabled: !!workflowId && resultIdsToFill.length > 0 && !isDone,
        queryKey: ['symple.triplet.phase.result', { ids: resultIdsToFill }, 'for-workflow-chart'],
        queryFn: () =>
            odooSearchRead(
                'symple.triplet.phase.result',
                [['id', 'in', resultIdsToFill]],
                ['name', 'starting_phase_ids', 'next_phase_id']
            ),
    });

    // -------------------------------------
    // Methods
    // -------------------------------------

    function findPhase(id: number): ChartPhase | null {
        return (
            initialPhases?.find((p) => p.id === id) ||
            complementPhases?.find((p) => p.id === id) ||
            null
        );
    }

    function findResult(id: number): ChartResult | null {
        return (
            initialResults?.find((p) => p.id === id) ||
            complementResults?.find((p) => p.id === id) ||
            null
        );
    }

    function traverse(
        startId: number,
        phases: ChartPhase[] = [],
        results: ChartResult[] = []
    ): [ChartPhase[], ChartResult[]] {
        const phase = findPhase(startId);
        if (!phase) {
            throw new MissingPhaseError(startId);
        }

        let newPhases = [...phases];
        let newResults = [...results];

        newPhases.push(phase);

        const resultIds = phase.allowed_phase_result_ids;

        for (const resultId of resultIds) {
            if (newResults.some((r) => r.id === resultId)) {
                continue;
            }

            const result = findResult(resultId);

            if (!result) {
                throw new MissingResultError(resultId);
            }

            newResults.push(result);
            const nextPhaseId = result.next_phase_id?.[0];
            if (nextPhaseId && !newPhases.some((p) => p.id === nextPhaseId)) {
                [newPhases, newResults] = traverse(nextPhaseId, newPhases, newResults);
            }
        }

        return [newPhases, newResults];
    }

    // -------------------------------------
    // Effects
    // -------------------------------------

    useEffect(() => {
        if (isDone) {
            return;
        }

        if (!initialPhases || !initialResults || !startPhaseId) {
            return;
        }

        try {
            const [partialPhases, partialResults] = traverse(startPhaseId);
            setPhases(partialPhases);
            setResults(partialResults);
            setIsDone(true);
        } catch (err) {
            if (err instanceof MissingPhaseError) {
                setPhaseIdsToFill([...phaseIdsToFill, err.id]);
            } else if (err instanceof MissingResultError) {
                setResultIdsToFill([...resultIdsToFill, err.id]);
            } else {
                throw err;
            }
        }
    }, [initialPhases, initialResults, complementPhases, complementResults, isDone, startPhaseId]);

    return { phases, results };
}

class MissingPhaseError extends Error {
    id: number;

    constructor(id: number) {
        super(`Phase not found: ${id}`);
        this.id = id;
    }
}

class MissingResultError extends Error {
    id: number;

    constructor(id: number) {
        super(`Phase not found: ${id}`);
        this.id = id;
    }
}
