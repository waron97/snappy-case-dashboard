import { useEffect, useRef, useState } from 'react'
import '@xyflow/react/dist/style.css'
import {
  Background,
  Controls,
  Edge,
  Node,
  ReactFlow,
  ReactFlowInstance,
  useEdgesState,
  useNodesState
} from '@xyflow/react'
import { Box, Button, Group, Stack, Text, useMantineTheme } from '@mantine/core'
import { buildWorkflowChartLayout, ChartResult, NODE_WIDTH } from './layout'
import useWorkflowData from './useWorfklowData'
import PhaseDetailPopover from './PhaseDetailPopover'
import MiniPathChart from './MiniPathChart'
import { HighlightedGroup } from './pathGroups'

type Props = {
  workflowId: number
  crossedPhases?: Set<number>
  crossedResults?: Set<number>
  activePhaseId?: number
  startPhaseId?: number
}

export default function WorkflowFlowChart(props: Props) {
  const { workflowId, crossedPhases, crossedResults, activePhaseId, startPhaseId } = props

  // -------------------------------------
  // Hooks
  // -------------------------------------

  const theme = useMantineTheme()

  const [nodes, setNodes] = useNodesState([] as Node[])
  const [edges, setEdges] = useEdgesState([] as Edge[])

  const [selectedPhaseId, setSelectedPhaseId] = useState<number | null>(null)
  const [highlightedGroup, setHighlightedGroup] = useState<HighlightedGroup | null>(null)

  const chartRef = useRef<ReactFlowInstance | null>(null)

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { phases, results } = useWorkflowData(workflowId, startPhaseId)

  // -------------------------------------
  // Effects
  // -------------------------------------

  useEffect(() => {
    if (!results || !phases) {
      return
    }

    const activeColor = theme.colors.teal[8]
    const pinkColor = theme.colors.pink[8]
    const pathPhaseIds = highlightedGroup ? new Set(highlightedGroup.phaseIds) : undefined
    const pathResultIds = highlightedGroup ? new Set(highlightedGroup.resultIds) : undefined

    buildWorkflowChartLayout(phases, results, startPhaseId).then((result) => {
      setNodes(
        result.children?.map((node) => {
          const phase = phases.find((p) => String(p.id) === node.id)!
          const isPathNode = pathPhaseIds?.has(phase.id)
          const isCrossed = crossedPhases?.has(phase.id)
          return {
            id: String(phase.id),
            position: { x: node.x!, y: node.y! },
            data: { label: phase.name },
            style: {
              borderColor: isPathNode ? pinkColor : isCrossed ? activeColor : undefined,
              opacity: 1
            },
            width: NODE_WIDTH
          }
        }) || []
      )

      setEdges(
        results.reduce((acc: Edge[], current: ChartResult) => {
          const isPathEdge = pathResultIds?.has(current.id)
          const isCrossed = crossedResults?.has(current.id)
          const edgeColor = isPathEdge ? pinkColor : isCrossed ? activeColor : undefined
          const ret: Edge[] = [
            ...acc,
            ...current.starting_phase_ids.map((startId: number) => {
              const edge: Edge = {
                id: `${current.id}-${startId}`,
                source: String(startId),
                target: String(current.next_phase_id[0]),
                type: 'smoothstep',
                label: edgeColor ? current.name : undefined,
                labelShowBg: true,
                animated: true,
                labelBgStyle: {
                  fill: edgeColor
                },
                style: {
                  stroke: edgeColor,
                  strokeWidth: edgeColor ? 3 : undefined
                },
                data: {
                  label: current.name
                },
                zIndex: edgeColor ? 1 : 0
              }
              return edge
            })
          ]
          return ret
        }, [])
      )
    })
  }, [results, phases, crossedPhases, crossedResults, theme, startPhaseId, highlightedGroup])

  // -------------------------------------
  // Functions
  // -------------------------------------

  function centerOnPhase(phaseId: number): void {
    if (!chartRef.current) {
      return
    }

    const targetNode = nodes.find((n) => n.id === String(phaseId))
    if (!targetNode) {
      return
    }

    // Center the view on the target node with smooth animation
    chartRef.current.setCenter(targetNode.position.x + NODE_WIDTH / 2, targetNode.position.y + 40, {
      zoom: 1.2,
      duration: 800
    })
  }

  function scrollToPhase(phase: number | 'active' | 'starting') {
    let targetPhaseId: number | undefined

    if (phase === 'active') {
      // Scroll to the current active phase
      targetPhaseId = activePhaseId
    } else if (phase === 'starting') {
      // Scroll to the first phase in the workflow
      targetPhaseId = phases && phases.length > 0 ? phases[0].id : undefined
    } else {
      targetPhaseId = phase
    }

    if (targetPhaseId === undefined) {
      return
    }

    centerOnPhase(targetPhaseId)
  }

  function onFocusPhase(phaseId: number): void {
    centerOnPhase(phaseId)
    setSelectedPhaseId(phaseId)
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // -------------------------------------

  return (
    <Stack pt="md">
      <Group justify="end">
        {highlightedGroup && (
          <Button size="sm" color="pink" variant="light" onClick={() => setHighlightedGroup(null)}>
            <Text>Clear highlighted path</Text>
          </Button>
        )}
        <Button size="sm" color="teal" onClick={() => scrollToPhase('active')}>
          <Text>Show active phase</Text>
        </Button>
        <Button size="sm" color="teal" onClick={() => scrollToPhase('starting')}>
          <Text>Show starting phase</Text>
        </Button>
      </Group>
      <Group align="stretch" wrap="nowrap" gap="md">
        <Box h={900} mah="90vh" style={{ flex: 1, minWidth: 0 }}>
          <ReactFlow
            nodes={nodes}
            edges={edges}
            fitView
            colorMode="dark"
            onInit={(instance) => {
              chartRef.current = instance
            }}
            onNodeClick={(_, node) => setSelectedPhaseId(Number(node.id))}
          >
            <Background />
            <Controls />
            <PhaseDetailPopover
              phaseId={selectedPhaseId}
              phases={phases}
              results={results}
              startPhaseId={startPhaseId}
              highlightedGroup={highlightedGroup}
              onClose={() => setSelectedPhaseId(null)}
              onFocusPhase={onFocusPhase}
              onHighlightGroup={setHighlightedGroup}
            />
          </ReactFlow>
        </Box>
        {highlightedGroup && (
          <MiniPathChart phases={phases} results={results} group={highlightedGroup} />
        )}
      </Group>
    </Stack>
  )
}
