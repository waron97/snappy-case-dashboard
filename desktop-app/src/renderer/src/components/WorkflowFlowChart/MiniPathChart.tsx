import { useMemo } from 'react'
import { Background, Edge, Node, ReactFlow } from '@xyflow/react'
import { Box, useMantineTheme } from '@mantine/core'
import { ChartPhase, ChartResult, NODE_HEIGHT, NODE_WIDTH } from './layout'
import { HighlightedGroup } from './pathGroups'

type Props = {
  phases: ChartPhase[]
  results: ChartResult[]
  group: HighlightedGroup
}

const SPINE_GAP = NODE_HEIGHT + 120
const BUBBLE_ROW_GAP = NODE_HEIGHT + 100
const COLUMN_SPACING = NODE_WIDTH + 40

export default function MiniPathChart({ phases, results, group }: Props): React.JSX.Element {
  const theme = useMantineTheme()
  const pinkColor = theme.colors.pink[8]

  const { nodes, edges } = useMemo(() => {
    const phaseNameById = new Map(phases.map((p) => [p.id, p.name]))
    const resultNameById = new Map(results.map((r) => [r.id, r.name]))

    const nodes: Node[] = []
    const edges: Edge[] = []
    const placedIds = new Set<string>()

    function placeNode(
      id: string,
      x: number,
      y: number,
      label: string | number,
      viaSubtitle?: string
    ): void {
      if (placedIds.has(id)) {
        return
      }
      placedIds.add(id)
      nodes.push({
        id,
        position: { x, y },
        data: {
          label: viaSubtitle ? (
            <div>
              <div style={{ fontSize: 10, opacity: 0.75, marginBottom: 2 }}>{viaSubtitle}</div>
              <div>{label}</div>
            </div>
          ) : (
            label
          )
        },
        width: NODE_WIDTH,
        style: { borderColor: pinkColor, opacity: 1 }
      })
    }

    // Edges converging within a bubble stay unlabeled — a smoothstep edge's
    // label sits near the step corner, not the true midpoint, so several
    // diagonal branches from/to the same node clump their labels together.
    // The transition name goes on the destination node instead (see above).
    function placeEdge(id: string, source: string, target: string, label?: string): void {
      edges.push({
        id,
        source,
        target,
        type: 'smoothstep',
        label,
        labelShowBg: true,
        labelBgStyle: { fill: pinkColor },
        style: { stroke: pinkColor, strokeWidth: 3 }
      })
    }

    let y = 0
    let prevSpineId: string | undefined

    group.backbone.forEach((token, k) => {
      if (token.type === 'node') {
        const id = String(token.phaseId)
        if (k > 0) {
          y += SPINE_GAP
        }
        placeNode(id, 0, y, phaseNameById.get(token.phaseId) ?? token.phaseId)
        if (token.viaResultId !== undefined && prevSpineId) {
          placeEdge(
            `e-${prevSpineId}-${id}`,
            prevSpineId,
            id,
            resultNameById.get(token.viaResultId) ?? ''
          )
        }
        prevSpineId = id
      } else {
        const entryId = String(token.entry)
        const exitId = String(token.exit)
        const entryY = y
        const maxInteriorLen = Math.max(...token.routes.map((r) => r.phaseIds.length - 2))
        const exitY = entryY + (maxInteriorLen + 1) * BUBBLE_ROW_GAP

        placeNode(entryId, 0, entryY, phaseNameById.get(token.entry) ?? token.entry)

        token.routes.forEach((route, r) => {
          const xOffset = (r - (token.routes.length - 1) / 2) * COLUMN_SPACING
          const interior = route.phaseIds.slice(1, -1)
          let prevId = entryId

          interior.forEach((phaseId, idx) => {
            const nodeId = `${phaseId}-b${token.entry}-${token.exit}-r${r}`
            placeNode(
              nodeId,
              xOffset,
              entryY + (idx + 1) * BUBBLE_ROW_GAP,
              phaseNameById.get(phaseId) ?? phaseId,
              resultNameById.get(route.resultIds[idx])
            )
            placeEdge(`${prevId}-${nodeId}`, prevId, nodeId)
            prevId = nodeId
          })

          placeEdge(`${prevId}-${exitId}-r${r}`, prevId, exitId)
        })

        placeNode(exitId, 0, exitY, phaseNameById.get(token.exit) ?? token.exit)
        y = exitY
        prevSpineId = exitId
      }
    })

    return { nodes, edges }
  }, [phases, results, group, pinkColor])

  return (
    <Box w={320} h={900} mah="90vh">
      <ReactFlow nodes={nodes} edges={edges} fitView colorMode="dark">
        <Background />
      </ReactFlow>
    </Box>
  )
}
