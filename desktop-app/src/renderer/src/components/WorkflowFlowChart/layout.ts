import { OneToMany } from '@/lib/odoo-api';
import ELK from 'elkjs';

const elk = new ELK();

export type ChartPhase = {
    id: number;
    name: string;
    allowed_phase_result_ids: number[];
    stage_code?: string | false;
};

export type ChartResult = {
    id: number;
    name: string;
    starting_phase_ids: number[];
    next_phase_id: OneToMany;
};

export const NODE_WIDTH = 230;
export const NODE_HEIGHT = 80;

// Stage codes that mark a successful "Done"/"Solved" end phase. The happy flow
// is any route from the starting phase into a phase with one of these codes.
// ("ko" = Done KO and "annulled" = Cancelled are deliberately excluded.)
export const HAPPY_STAGE_CODES = ['solved', 'ok'];

/**
 * Returns the set of result (edge) ids that lie on some path from `startPhaseId`
 * to any happy-terminal phase (stage_code in HAPPY_STAGE_CODES).
 *
 * Cycle-safe: works on reachability sets, not path enumeration.
 *   - forward  = phases reachable from the start phase
 *   - backward = phases that can reach a happy terminal (BFS on reversed edges)
 * A result is happy when any of its sources is forward-reachable and its target
 * is backward-reachable, i.e. the edge sits on a start -> terminal walk.
 */
export function computeHappyResultIds(
    phases: ChartPhase[],
    results: ChartResult[],
    startPhaseId?: number
): Set<number> {
    const happy = new Set<number>();
    if (!startPhaseId) {
        return happy;
    }

    const terminals = phases
        .filter((p) => p.stage_code && HAPPY_STAGE_CODES.includes(p.stage_code))
        .map((p) => p.id);
    if (terminals.length === 0) {
        return happy;
    }

    // Adjacency: source phase -> [target phase], and the reverse.
    const forwardAdj = new Map<number, number[]>();
    const backwardAdj = new Map<number, number[]>();
    for (const result of results) {
        const target = result.next_phase_id?.[0];
        if (!target) {
            continue;
        }
        for (const source of result.starting_phase_ids) {
            (forwardAdj.get(source) ?? forwardAdj.set(source, []).get(source)!).push(target);
            (backwardAdj.get(target) ?? backwardAdj.set(target, []).get(target)!).push(source);
        }
    }

    const bfs = (starts: number[], adj: Map<number, number[]>): Set<number> => {
        const visited = new Set<number>(starts);
        const queue = [...starts];
        while (queue.length > 0) {
            const node = queue.shift()!;
            for (const next of adj.get(node) ?? []) {
                if (!visited.has(next)) {
                    visited.add(next);
                    queue.push(next);
                }
            }
        }
        return visited;
    };

    const forward = bfs([startPhaseId], forwardAdj);
    const backward = bfs(terminals, backwardAdj);

    for (const result of results) {
        const target = result.next_phase_id?.[0];
        if (target && backward.has(target) && result.starting_phase_ids.some((s) => forward.has(s))) {
            happy.add(result.id);
        }
    }

    return happy;
}

export function buildWorkflowChartLayout(
    phases: ChartPhase[],
    results: ChartResult[],
    startPhaseId?: number
) {
    const happyResultIds = computeHappyResultIds(phases, results, startPhaseId);

    return elk.layout({
        id: 'root',
        layoutOptions: {
            'elk.algorithm': 'layered',
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
        edges: results.map((result) => {
            const isHappy = happyResultIds.has(result.id);
            return {
                id: String(result.id),
                sources: result.starting_phase_ids.map(String),
                targets: [String(result.next_phase_id[0])],
                // Pull the happy flow into a straight, short spine (prbot-style).
                layoutOptions: {
                    'elk.layered.priority.straightness': isHappy ? '10' : '1',
                    'elk.layered.priority.shortness': isHappy ? '10' : '1',
                    'elk.layered.priority.direction': isHappy ? '10' : '1',
                },
            };
        }),
    });
}
