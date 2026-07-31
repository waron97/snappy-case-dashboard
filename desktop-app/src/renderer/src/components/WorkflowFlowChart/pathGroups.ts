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
  const seenBackbones = new Set<string>()
  const visited = new Set<number>([startPhaseId])
  const backbone: BackboneToken[] = [{ type: 'node', phaseId: startPhaseId }]

  function pushGroup(): void {
    // Defensive dedupe: nothing in the search below is expected to produce
    // two identical backbones, but this keeps MAX_GROUPS bounding distinct
    // groups (its documented contract) even if some future graph shape
    // manages to reach the same backbone two different ways.
    const signature = JSON.stringify(backbone)
    if (seenBackbones.has(signature)) {
      return
    }
    seenBackbones.add(signature)
    groups.push({ backbone: [...backbone] })
  }

  // `chains`, when present, are remainders of an ancestor bubble's own
  // recorded routes: the exact tail still expected from `current` onward
  // before it rejoins that bubble's exit. Every node along the way is still
  // recorded normally (the chain doesn't hide anything from the backbone) —
  // it only tells the search where the *already-known* continuation ends,
  // so that final step isn't re-explored past a bubble's own exit and
  // duplicate the group its collapsed token (and sibling `dfs(exit)` call)
  // already produced.
  function dfs(current: number, chains?: ChartPath[]): void {
    if (groups.length >= MAX_GROUPS) {
      return
    }
    if (current === targetPhaseId) {
      pushGroup()
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
    // A node reached while tracing an ancestor's inherited chain is already
    // being walked edge-by-edge on that ancestor's behalf — taking a fresh
    // collapse here too would represent the exact same reconverging cluster
    // a second, redundant way (once flattened via the chain, once as its
    // own bubble token). Collapse only applies when a node is reached fresh.
    const bubbleTaken =
      chains === undefined &&
      bubble !== undefined &&
      !visited.has(bubble.exit) &&
      !bubbleContainsTarget
    // Non-escaping first hops are fully absorbed by the bubble contraction
    // below and excluded outright. Escaping first hops still need individual
    // exploration (handled per-edge below), since the deduped `routes` alone
    // don't capture what else hangs off them.
    const bubbleFirstHops = bubbleTaken
      ? new Set(
          bubble!.routes
            .map((r) => r.phaseIds[1])
            .filter((firstHop) => !bubble!.escapingFirstHops.has(firstHop))
        )
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

    for (const { target, resultId } of adjacency.get(current) ?? []) {
      if (groups.length >= MAX_GROUPS) {
        return
      }
      if (bubbleFirstHops?.has(target) || visited.has(target)) {
        continue
      }

      // Chains this exact edge continues — either inherited from an
      // ancestor bubble (`chains`) or freshly started because this edge is
      // one of the bubble just found at `current`'s escaping first hops.
      // Matching is by the precise (phaseId, resultId) pair, never just the
      // target node, so an unrelated edge that happens to land on the same
      // node (e.g. a different bubble's own route reaching it) is never
      // mistaken for a continuation of this one.
      const matchedChains: ChartPath[] = []
      if (chains) {
        for (const chain of chains) {
          if (chain.phaseIds[1] === target && chain.resultIds[0] === resultId) {
            matchedChains.push(chain)
          }
        }
      }
      if (bubbleTaken && bubble!.escapingFirstHops.has(target)) {
        for (const route of bubble!.routes) {
          if (route.phaseIds[1] === target && route.resultIds[0] === resultId) {
            matchedChains.push(route)
          }
        }
      }

      const survivors = matchedChains
        .map((chain) => ({
          phaseIds: chain.phaseIds.slice(1),
          resultIds: chain.resultIds.slice(1)
        }))
        .filter((chain) => chain.phaseIds.length > 1)

      // A matched chain with no surviving distance means this edge lands
      // exactly on a bubble's own exit via its already-known route — that
      // continuation is already owned by that bubble's `dfs(exit)` call, so
      // skip it entirely (no node, no recursion) rather than re-deriving it.
      if (matchedChains.length > 0 && survivors.length === 0) {
        continue
      }

      backbone.push({ type: 'node', phaseId: target, viaResultId: resultId })
      visited.add(target)
      dfs(target, survivors.length > 0 ? survivors : undefined)
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
