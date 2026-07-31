import { ChartResult } from './layout'

// A "bubble" is a short branch-and-reconverge: from `entry`, at least two
// distinct short routes (<= MAX_BUBBLE_EDGES edges) lead to the same `exit`
// node. Path enumeration treats a bubble as a single entry->exit hop, so the
// combinatorial fan-out of its interior routes never gets multiplied out
// during the search — see pathGroups.ts's findGroupedPaths.
export const MAX_BUBBLE_EDGES = 3

export type ChartPath = { phaseIds: number[]; resultIds: number[] }
export type Bubble = {
  exit: number
  routes: ChartPath[]
  // First-hop nodes (immediate successors of `entry`) that have OTHER short
  // routes leading somewhere other than `exit` — a real branch point the
  // dedup below hid from `routes`. Contracting straight from entry to exit
  // would make whatever hangs off that branch permanently unreachable, so
  // pathGroups.ts must still explore these first hops edge-by-edge instead
  // of treating them as fully absorbed into the bubble.
  escapingFirstHops: Set<number>
}

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

function findBubble(entry: number, adjacency: Adjacency): Bubble | undefined {
  const routesByNode = new Map<number, ChartPath[]>()

  function walk(node: number, phaseIds: number[], resultIds: number[], visited: Set<number>): void {
    if (node !== entry) {
      const routes = routesByNode.get(node) ?? []
      routes.push({ phaseIds: [...phaseIds], resultIds: [...resultIds] })
      routesByNode.set(node, routes)
    }
    if (resultIds.length === MAX_BUBBLE_EDGES) {
      return
    }
    for (const { target, resultId } of adjacency.get(node) ?? []) {
      if (visited.has(target)) {
        continue
      }
      visited.add(target)
      phaseIds.push(target)
      resultIds.push(resultId)
      walk(target, phaseIds, resultIds, visited)
      resultIds.pop()
      phaseIds.pop()
      visited.delete(target)
    }
  }

  walk(entry, [entry], [], new Set([entry]))

  let bestNode: number | undefined
  let bestDepth = Infinity

  for (const [node, routes] of routesByNode) {
    // Keep at most one (the shortest) route per distinct first EDGE from
    // entry, for RANKING candidate exits only (see below) — two routes that
    // only diverge deep inside an already-shared tail aren't a real fork for
    // ranking purposes, they're the same branch found twice. Keying by the
    // edge (resultId), not the node it lands on, matters when two distinct
    // results from `entry` both target the same immediate next phase — that
    // is two genuinely different decisions that happen to coincide on where
    // they land, not one branch found twice, and must still count toward
    // the >=2 check below.
    const shortestByFirstEdge = new Map<number, ChartPath>()
    for (const route of routes) {
      const firstEdge = route.resultIds[0]
      const existing = shortestByFirstEdge.get(firstEdge)
      if (!existing || route.resultIds.length < existing.resultIds.length) {
        shortestByFirstEdge.set(firstEdge, route)
      }
    }
    const dedupedRoutes = Array.from(shortestByFirstEdge.values())

    if (dedupedRoutes.length >= 2) {
      // Depth at which a *second* distinct branch is confirmed to have
      // reconverged here — not just the fastest branch's own arrival time.
      // A node reached by routes of length [1, 3] isn't a real bubble exit
      // until hop 3; ranking it by its length-1 route would wrongly make it
      // look nearer than a node whose two routes are both length 2.
      const lengths = dedupedRoutes.map((r) => r.resultIds.length).sort((a, b) => a - b)
      const depth = lengths[1]
      if (depth < bestDepth) {
        bestDepth = depth
        bestNode = node
      }
    }
  }

  if (bestNode === undefined) {
    return undefined
  }

  // Final routes kept for the bubble: every distinct route (by exact
  // resultIds sequence) the walk found into bestNode — not just one per
  // first hop, so a first hop with multiple genuinely different-length
  // reconverging routes keeps all of them instead of only the shortest.
  const seenResultSequences = new Set<string>()
  const bestRoutes: ChartPath[] = []
  for (const route of routesByNode.get(bestNode) ?? []) {
    const key = route.resultIds.join(',')
    if (seenResultSequences.has(key)) {
      continue
    }
    seenResultSequences.add(key)
    bestRoutes.push(route)
  }

  // Which node(s) does each first hop actually lead to, across every route
  // the walk found (not just the ones kept in `routes`)? A first hop that
  // only ever leads back to the exit is safe to fully absorb; one that also
  // reaches some other node has a branch `routes` doesn't capture.
  const nodesByFirstHop = new Map<number, Set<number>>()
  for (const [node, routes] of routesByNode) {
    for (const route of routes) {
      // Continuing the bounded walk past bestNode isn't a new destination —
      // it's downstream of the exit, not a genuine branch for this first hop.
      if (route.phaseIds.slice(0, -1).includes(bestNode)) {
        continue
      }
      const firstHop = route.phaseIds[1]
      const nodes = nodesByFirstHop.get(firstHop) ?? new Set<number>()
      nodes.add(node)
      nodesByFirstHop.set(firstHop, nodes)
    }
  }

  const escapingFirstHops = new Set<number>()
  for (const route of bestRoutes) {
    const firstHop = route.phaseIds[1]
    const reachableNodes = nodesByFirstHop.get(firstHop) ?? new Set<number>()
    if (reachableNodes.size > 1 || !reachableNodes.has(bestNode)) {
      escapingFirstHops.add(firstHop)
    }
  }

  return { exit: bestNode, routes: bestRoutes, escapingFirstHops }
}

// entry phase id -> its bubble (nearest reconvergence + the short routes
// that reach it), for every node with >=2 distinct short routes to a shared
// downstream node.
export function detectBubbles(results: ChartResult[]): Map<number, Bubble> {
  const adjacency = buildAdjacency(results)
  const bubbleByEntry = new Map<number, Bubble>()

  for (const [node, edges] of adjacency) {
    if (edges.length < 2) {
      continue
    }
    const bubble = findBubble(node, adjacency)
    if (bubble) {
      bubbleByEntry.set(node, bubble)
    }
  }

  return bubbleByEntry
}
