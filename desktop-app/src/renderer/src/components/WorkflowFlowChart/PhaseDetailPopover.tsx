import { useEffect, useMemo } from 'react'
import { NodeToolbar, Position } from '@xyflow/react'
import {
  ActionIcon,
  Button,
  Group,
  Paper,
  ScrollArea,
  Stack,
  Table,
  Tabs,
  Text
} from '@mantine/core'
import { IconBug, IconX } from '@tabler/icons-react'
import { ChartPhase, ChartResult } from './layout'
import { detectBubbles } from './bubbles'
import {
  BubbleToken,
  findGroupedPaths,
  highlightForGroup,
  HighlightedGroup,
  PathGroup
} from './pathGroups'

type Props = {
  phaseId: number | null
  phases: ChartPhase[]
  results: ChartResult[]
  startPhaseId?: number
  highlightedGroup: HighlightedGroup | null
  onClose: () => void
  onFocusPhase: (phaseId: number) => void
  onHighlightGroup: (group: HighlightedGroup | null) => void
}

export default function PhaseDetailPopover(props: Props): React.JSX.Element {
  const {
    phaseId,
    phases,
    results,
    startPhaseId,
    highlightedGroup,
    onClose,
    onFocusPhase,
    onHighlightGroup
  } = props

  const phase = phaseId !== null ? phases.find((p) => p.id === phaseId) : undefined

  const incoming = useMemo(() => {
    if (phaseId === null) {
      return []
    }
    return results
      .filter((r) => r.next_phase_id?.[0] === phaseId)
      .flatMap((r) => r.starting_phase_ids.map((sourceId) => ({ result: r, otherId: sourceId })))
  }, [results, phaseId])

  const outgoing = useMemo(() => {
    if (phaseId === null) {
      return []
    }
    return results
      .filter((r) => r.starting_phase_ids.includes(phaseId))
      .map((r) => ({ result: r, otherId: r.next_phase_id?.[0] }))
      .filter((r): r is { result: ChartResult; otherId: number } => !!r.otherId)
  }, [results, phaseId])

  const resultNameById = useMemo(() => new Map(results.map((r) => [r.id, r.name])), [results])

  // Detour branches that fork off and reconverge within a few hops are
  // detected once per graph, then collapsed into a single hop during
  // enumeration below — their interior routes never get multiplied out.
  const bubbles = useMemo(() => detectBubbles(results), [results])

  const { groups, truncated } = useMemo(() => {
    if (phaseId === null || !startPhaseId) {
      return { groups: [], truncated: false }
    }
    return findGroupedPaths(startPhaseId, phaseId, bubbles, results)
  }, [startPhaseId, phaseId, bubbles, results])

  // The distinct alternate routes folded into a group by bubble collapsing —
  // each one is a short "variant" branch the group's paths take.
  function variantLabels(group: PathGroup): string[] {
    const bubbleTokens = group.backbone.filter((t): t is BubbleToken => t.type === 'bubble')
    return bubbleTokens.flatMap((token) =>
      token.routes.map((route) =>
        route.resultIds.map((id) => resultNameById.get(id) ?? String(id)).join(' → ')
      )
    )
  }

  // Representative hop count for a group — bubbles report their shortest
  // known route's length, since the exact count varies by variant.
  function stepCount(group: PathGroup): number {
    let steps = 0
    for (const token of group.backbone) {
      if (token.type === 'node') {
        if (token.viaResultId !== undefined) {
          steps += 1
        }
      } else {
        steps += Math.min(...token.routes.map((r) => r.resultIds.length))
      }
    }
    return steps
  }

  function handleSelectGroup(index: number): void {
    if (highlightedGroup?.groupIndex === index) {
      onHighlightGroup(null)
      return
    }
    onHighlightGroup(highlightForGroup(index, groups[index]))
  }

  // Debug snapshot of everything the bubble/grouping algorithm saw for the
  // currently selected phase — for reporting graph-shape bugs without
  // needing live Odoo access to reproduce them.
  const debugPayload = useMemo(() => {
    if (phaseId === null) {
      return null
    }
    return {
      phaseId,
      startPhaseId,
      phases: phases.map((p) => ({
        id: p.id,
        name: p.name,
        allowed_phase_result_ids: p.allowed_phase_result_ids
      })),
      results: results.map((r) => ({
        id: r.id,
        name: r.name,
        starting_phase_ids: r.starting_phase_ids,
        next_phase_id: r.next_phase_id
      })),
      bubbles: Array.from(bubbles.entries()).map(([entry, bubble]) => ({ entry, ...bubble })),
      groups
    }
  }, [phaseId, startPhaseId, phases, results, bubbles, groups])

  useEffect(() => {
    if (debugPayload) {
      console.log('[WorkflowChart debug]', debugPayload)
    }
  }, [debugPayload])

  return (
    <NodeToolbar
      nodeId={phaseId !== null ? String(phaseId) : undefined}
      isVisible={phaseId !== null}
      position={Position.Top}
      offset={14}
      align="center"
    >
      <Paper shadow="md" radius="md" p="xs" w={360} withBorder>
        <Group justify="space-between" mb={4} wrap="nowrap" gap="xs">
          <Text fw={600} size="sm" truncate>
            {phase?.name}
          </Text>
          <Group gap={4} wrap="nowrap">
            <ActionIcon
              size="sm"
              variant="subtle"
              color="gray"
              title="Copy debug data (phases/results/bubbles/groups) to clipboard"
              onClick={() => navigator.clipboard.writeText(JSON.stringify(debugPayload, null, 2))}
            >
              <IconBug size={14} />
            </ActionIcon>
            <ActionIcon size="sm" variant="subtle" color="gray" onClick={onClose}>
              <IconX size={14} />
            </ActionIcon>
          </Group>
        </Group>

        <Tabs defaultValue="edges">
          <Tabs.List>
            <Tabs.Tab value="edges" fz="xs">
              Edges
            </Tabs.Tab>
            <Tabs.Tab value="paths" fz="xs">
              Paths
            </Tabs.Tab>
          </Tabs.List>

          <Tabs.Panel value="edges" pt="xs">
            <ScrollArea.Autosize mah={260} className="nowheel">
              <Stack gap="sm">
                <Stack gap={4}>
                  <Text fw={600} size="xs" c="dimmed">
                    Incoming
                  </Text>
                  {incoming.length === 0 && (
                    <Text c="dimmed" size="xs">
                      None
                    </Text>
                  )}
                  {incoming.map(({ result, otherId }) => (
                    <Button
                      key={`${result.id}-${otherId}`}
                      size="xs"
                      variant="light"
                      justify="start"
                      fullWidth
                      onClick={() => onFocusPhase(otherId)}
                      styles={{ label: { whiteSpace: 'normal', textAlign: 'left' } }}
                    >
                      {result.name}
                    </Button>
                  ))}
                </Stack>

                <Stack gap={4}>
                  <Text fw={600} size="xs" c="dimmed">
                    Outgoing
                  </Text>
                  {outgoing.length === 0 && (
                    <Text c="dimmed" size="xs">
                      None
                    </Text>
                  )}
                  {outgoing.map(({ result, otherId }) => (
                    <Button
                      key={`${result.id}-${otherId}`}
                      size="xs"
                      variant="light"
                      justify="start"
                      fullWidth
                      onClick={() => onFocusPhase(otherId)}
                      styles={{ label: { whiteSpace: 'normal', textAlign: 'left' } }}
                    >
                      {result.name}
                    </Button>
                  ))}
                </Stack>
              </Stack>
            </ScrollArea.Autosize>
          </Tabs.Panel>

          <Tabs.Panel value="paths" pt="xs">
            {!startPhaseId && (
              <Text c="dimmed" size="xs">
                Workflow has no starting phase configured.
              </Text>
            )}
            {startPhaseId && groups.length === 0 && (
              <Text c="dimmed" size="xs">
                No path found from the starting phase.
              </Text>
            )}
            {groups.length > 0 && (
              <Stack gap={4}>
                <ScrollArea.Autosize mah={260} className="nowheel">
                  <Table striped highlightOnHover fz="xs" verticalSpacing={4}>
                    <Table.Thead>
                      <Table.Tr>
                        <Table.Th />
                        <Table.Th>Steps</Table.Th>
                        <Table.Th>Variants</Table.Th>
                      </Table.Tr>
                    </Table.Thead>
                    <Table.Tbody>
                      {groups.map((group, i) => {
                        const variantCount = variantLabels(group).length
                        return (
                          <Table.Tr
                            key={i}
                            onClick={() => handleSelectGroup(i)}
                            bg={highlightedGroup?.groupIndex === i ? 'pink.9' : undefined}
                            style={{ cursor: 'pointer' }}
                          >
                            <Table.Td>P{i + 1}</Table.Td>
                            <Table.Td>{stepCount(group)}</Table.Td>
                            <Table.Td>{variantCount > 0 ? variantCount : '—'}</Table.Td>
                          </Table.Tr>
                        )
                      })}
                    </Table.Tbody>
                  </Table>
                </ScrollArea.Autosize>
                {truncated && (
                  <Text c="dimmed" size="xs">
                    Showing first {groups.length} groups — more may exist.
                  </Text>
                )}
              </Stack>
            )}
          </Tabs.Panel>
        </Tabs>
      </Paper>
    </NodeToolbar>
  )
}
