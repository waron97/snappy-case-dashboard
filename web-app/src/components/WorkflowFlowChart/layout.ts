import { OneToMany } from '@app/api';
import ELK from 'elkjs';

const elk = new ELK();

export type ChartPhase = {
    id: number;
    name: string;
    allowed_phase_result_ids: number[];
};

export type ChartResult = {
    id: number;
    name: string;
    starting_phase_ids: number[];
    next_phase_id: OneToMany;
};

export const NODE_WIDTH = 230;
export const NODE_HEIGHT = 80;

export function buildWorkflowChartLayout(phases: ChartPhase[], results: ChartResult[]) {
    return elk.layout({
        id: 'root',
        layoutOptions: {
            'elk.algorithm': 'mrtree',
            'elk.direction': 'DOWN',
            // Useful options for BPMN-like orthogonal routing
            'elk.layered.spacing.nodeNodeBetweenLayers': '50',
            'elk.spacing.nodeNode': '100',
            'elk.edgeRouting': 'ORTHOGONAL',
        },
        children: phases.map((phase) => ({
            id: String(phase.id),
            width: NODE_WIDTH,
            height: NODE_HEIGHT,
        })),
        edges: results.map((result) => ({
            id: String(result.id),
            sources: result.starting_phase_ids.map(String),
            targets: [String(result.next_phase_id[0])],
        })),
    });
}
