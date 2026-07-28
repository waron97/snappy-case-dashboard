import { useMemo } from 'react'
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
import { IconX } from '@tabler/icons-react'
import { ChartPhase, ChartResult } from './layout'
import { findAllSimplePaths } from './pathfinding'
import { detectBubbleExits } from './bubbles'
import {
  BubbleToken,
  groupPaths,
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

  const { paths, truncated } = useMemo(() => {
    if (phaseId === null || !startPhaseId) {
      return { paths: [], truncated: false }
    }
    return findAllSimplePaths(startPhaseId, phaseId, results)
  }, [startPhaseId, phaseId, results])

  const resultNameById = useMemo(() => new Map(results.map((r) => [r.id, r.name])), [results])

  // Detour branches that fork off and reconverge within a few hops get
  // collapsed into one group instead of listed as fully separate paths.
  const bubbleExitByEntry = useMemo(() => detectBubbleExits(results), [results])
  const groups = useMemo(() => groupPaths(paths, bubbleExitByEntry), [paths, bubbleExitByEntry])

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

  function handleSelectGroup(index: number): void {
    if (highlightedGroup?.groupIndex === index) {
      onHighlightGroup(null)
      return
    }
    onHighlightGroup(highlightForGroup(index, groups[index]))
  }

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
          <ActionIcon size="sm" variant="subtle" color="gray" onClick={onClose}>
            <IconX size={14} />
          </ActionIcon>
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
            {startPhaseId && paths.length === 0 && (
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
                            <Table.Td>{group.paths[0].resultIds.length}</Table.Td>
                            <Table.Td>{variantCount > 0 ? variantCount : '—'}</Table.Td>
                          </Table.Tr>
                        )
                      })}
                    </Table.Tbody>
                  </Table>
                </ScrollArea.Autosize>
                {truncated && (
                  <Text c="dimmed" size="xs">
                    Showing first {paths.length} paths — more may exist.
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
