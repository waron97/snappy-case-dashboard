import { Bubble, ChartPath } from './bubbles'
import { ChartResult } from './layout'

// viaResultId is the edge that connects this node to the previous backbone
// node, when that hop wasn't folded into a bubble (undefined for the very
// first node in a path, and unused when the previous token is a bubble —
// the bubble's own routes already draw the edge converging into this node).
export type NodeToken = { type: 'node'; phaseId: number; viaResultId?: number }
export type BubbleToken = {
  type: 'bubble'
  entry: number
  exit: number
  // All distinct short entry->exit routes found during bubble detection.
  routes: ChartPath[]
}
export type BackboneToken = NodeToken | BubbleToken

export type PathGroup = {
  backbone: BackboneToken[]
}

export type HighlightedGroup = {
  groupIndex: number
  backbone: BackboneToken[]
  phaseIds: number[]
  resultIds: number[]
}

// Cap on the number of GROUPS (not raw paths) enumerated. Bubbles are
// collapsed to a single hop *during* the search, so their interior routes
// never get multiplied out — this only guards against graphs with genuinely
// large branching outside of any bubble.
export const MAX_GROUPS = 500

type Adjacency = Map<number, Array<{ target: number; resultId: number }>>

function buildAdjacency(results: ChartResult[]): Adjacency {
  const adjacency: Adjacency = new Map()
  for (const result of results) {
    const target = result.next_phase_id?.[0]
    if (!target) {
      continue
    }
    for (const source of result.starting_phase_ids) {
      const edges = adjacency.get(source) ?? []
      edges.push({ target, resultId: result.id })
      adjacency.set(source, edges)
    }
  }
  return adjacency
}

export function findGroupedPaths(
  startPhaseId: number,
  targetPhaseId: number,
  bubbles: Map<number, Bubble>,
  results: ChartResult[]
): { groups: PathGroup[]; truncated: boolean } {
  if (startPhaseId === targetPhaseId) {
    return { groups: [{ backbone: [{ type: 'node', phaseId: startPhaseId }] }], truncated: false }
  }

  const adjacency = buildAdjacency(results)
  const groups: PathGroup[] = []
  const visited = new Set<number>([startPhaseId])
  const backbone: BackboneToken[] = [{ type: 'node', phaseId: startPhaseId }]

  function dfs(current: number): void {
    if (groups.length >= MAX_GROUPS) {
      return
    }
    if (current === targetPhaseId) {
      groups.push({ backbone: [...backbone] })
      return
    }

    const bubble = bubbles.get(current)
    // The target itself can legitimately sit as an interior node of one of
    // this bubble's routes (we're enumerating paths TO an arbitrary node,
    // not just to the overall bubble exit). Contracting past it would make
    // it permanently unreachable as a stopping point, so such a bubble must
    // be explored edge-by-edge instead of taken as a single hop.
    const bubbleContainsTarget =
      bubble?.routes.some((r) => r.phaseIds.slice(1, -1).includes(targetPhaseId)) ?? false
    const bubbleTaken = bubble !== undefined && !visited.has(bubble.exit) && !bubbleContainsTarget
    // Only exclude the bubble's first-hop edges from normal exploration when
    // the contracted hop was actually taken. If the exit is already visited
    // (common in a cyclic graph — some other branch already passed through
    // it), we fall back to exploring those edges individually instead of
    // silently pruning them.
    const bubbleFirstHops = bubbleTaken
      ? new Set(bubble!.routes.map((r) => r.phaseIds[1]))
      : undefined

    // Take the bubble as a single contracted hop — its interior routes are
    // known already (from detection), not rediscovered by branching here.
    if (bubbleTaken) {
      backbone.push({ type: 'bubble', entry: current, exit: bubble!.exit, routes: bubble!.routes })
      visited.add(bubble!.exit)
      dfs(bubble!.exit)
      visited.delete(bubble!.exit)
      backbone.pop()
    }

    // Any other edge not already covered by the bubble contraction above.
    for (const { target, resultId } of adjacency.get(current) ?? []) {
      if (groups.length >= MAX_GROUPS) {
        return
      }
      if (bubbleFirstHops?.has(target) || visited.has(target)) {
        continue
      }
      backbone.push({ type: 'node', phaseId: target, viaResultId: resultId })
      visited.add(target)
      dfs(target)
      visited.delete(target)
      backbone.pop()
    }
  }

  dfs(startPhaseId)

  return { groups, truncated: groups.length >= MAX_GROUPS }
}

export function highlightForGroup(groupIndex: number, group: PathGroup): HighlightedGroup {
  const phaseIds = new Set<number>()
  const resultIds = new Set<number>()

  for (const token of group.backbone) {
    if (token.type === 'node') {
      phaseIds.add(token.phaseId)
      if (token.viaResultId !== undefined) {
        resultIds.add(token.viaResultId)
      }
    } else {
      phaseIds.add(token.entry)
      phaseIds.add(token.exit)
      for (const route of token.routes) {
        route.phaseIds.forEach((id) => phaseIds.add(id))
        route.resultIds.forEach((id) => resultIds.add(id))
      }
    }
  }

  return {
    groupIndex,
    backbone: group.backbone,
    phaseIds: Array.from(phaseIds),
    resultIds: Array.from(resultIds)
  }
}
