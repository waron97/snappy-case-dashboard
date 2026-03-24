import { useEffect, useRef } from 'react';
import {
    Background,
    Controls,
    Edge,
    Node,
    ReactFlow,
    ReactFlowInstance,
    useEdgesState,
    useNodesState,
} from '@xyflow/react';
import { Box, Button, Group, Stack, Text, useMantineTheme } from '@mantine/core';
import { buildWorkflowChartLayout, ChartResult, NODE_WIDTH } from './layout';
import useWorkflowData from './useWorfklowData';

type Props = {
    workflowId: number;
    crossedPhases?: Set<number>;
    crossedResults?: Set<number>;
    activePhaseId?: number;
    startPhaseId?: number;
};

export default function WorkflowFlowChart(props: Props) {
    const { workflowId, crossedPhases, crossedResults, activePhaseId, startPhaseId } = props;

    // -------------------------------------
    // Hooks
    // -------------------------------------

    const theme = useMantineTheme();

    const [nodes, setNodes] = useNodesState([] as Node[]);
    const [edges, setEdges] = useEdgesState([] as Edge[]);

    const chartRef = useRef<ReactFlowInstance | null>(null);

    // -------------------------------------
    // Queries
    // -------------------------------------

    const { phases, results } = useWorkflowData(workflowId, startPhaseId);

    // -------------------------------------
    // Effects
    // -------------------------------------

    useEffect(() => {
        if (!results || !phases) {
            return;
        }

        const activeColor = theme.colors.teal[8];

        buildWorkflowChartLayout(phases, results).then((result) => {
            setNodes(
                result.children?.map((node) => {
                    const phase = phases.find((p) => String(p.id) === node.id)!;
                    const isCrossed = crossedPhases?.has(phase.id);
                    return {
                        id: String(phase.id),
                        position: { x: node.x!, y: node.y! },
                        data: { label: phase.name },
                        style: {
                            borderColor: isCrossed ? activeColor : undefined,
                            opacity: isCrossed ? 1 : 0.4,
                        },
                        width: NODE_WIDTH,
                    };
                }) || []
            );

            setEdges(
                results.reduce((acc: Edge[], current: ChartResult) => {
                    const isCrossed = crossedResults?.has(current.id);
                    const ret: Edge[] = [
                        ...acc,
                        ...current.starting_phase_ids.map((startId: number) => {
                            const edge: Edge = {
                                id: `${current.id}-${startId}`,
                                source: String(startId),
                                target: String(current.next_phase_id[0]),
                                type: 'smoothstep',
                                label: isCrossed ? current.name : undefined,
                                labelShowBg: true,
                                animated: true,
                                labelBgStyle: {
                                    fill: isCrossed ? activeColor : undefined,
                                },
                                style: {
                                    stroke: isCrossed ? activeColor : undefined,
                                    strokeWidth: isCrossed ? 3 : undefined,
                                },
                                data: {
                                    label: current.name,
                                },
                                zIndex: isCrossed ? 1 : 0,
                            };
                            return edge;
                        }),
                    ];
                    return ret;
                }, [])
            );
        });
    }, [results, phases, crossedPhases, crossedResults, theme]);

    // -------------------------------------
    // Functions
    // -------------------------------------

    function scrollToPhase(phase: number | 'active' | 'starting') {
        if (!chartRef.current) {
            return;
        }

        let targetPhaseId: string | undefined;

        if (phase === 'active') {
            // Scroll to the current active phase
            if (activePhaseId) {
                targetPhaseId = String(activePhaseId);
            }
        } else if (phase === 'starting') {
            // Scroll to the first phase in the workflow
            if (phases && phases.length > 0) {
                targetPhaseId = String(phases[0].id);
            }
        } else {
            targetPhaseId = String(phase);
        }

        if (!targetPhaseId) {
            return;
        }

        const targetNode = nodes.find((n) => n.id === targetPhaseId);
        if (!targetNode) {
            return;
        }

        // Center the view on the target node with smooth animation
        chartRef.current.setCenter(
            targetNode.position.x + NODE_WIDTH / 2,
            targetNode.position.y + 40,
            { zoom: 1.2, duration: 800 }
        );
    }

    // -------------------------------------
    // Local Variables
    // -------------------------------------

    // -------------------------------------

    return (
        <Stack pt="md">
            <Group justify="end">
                <Button size="sm" color="teal" onClick={() => scrollToPhase('active')}>
                    <Text>Show active phase</Text>
                </Button>
                <Button size="sm" color="teal" onClick={() => scrollToPhase('starting')}>
                    <Text>Show starting phase</Text>
                </Button>
            </Group>
            <Box h={600}>
                <ReactFlow
                    nodes={nodes}
                    edges={edges}
                    fitView
                    colorMode="dark"
                    onInit={(instance) => {
                        chartRef.current = instance;
                    }}
                >
                    <Background />
                    <Controls />
                </ReactFlow>
            </Box>
        </Stack>
    );
}
