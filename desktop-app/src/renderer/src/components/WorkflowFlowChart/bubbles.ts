import { ChartResult } from './layout'

// A "bubble" is a short branch-and-reconverge: from `entry`, at least two
// distinct short routes (<= MAX_BUBBLE_EDGES edges) lead to the same `exit`
// node. Paths that only differ inside a bubble get grouped together instead
// of listed as fully separate paths.
export const MAX_BUBBLE_EDGES = 3

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

function findBubbleExit(entry: number, adjacency: Adjacency): number | undefined {
  const routeCountByNode = new Map<number, number>()
  const depthByNode = new Map<number, number>()

  function walk(node: number, depth: number, visited: Set<number>): void {
    if (node !== entry) {
      routeCountByNode.set(node, (routeCountByNode.get(node) ?? 0) + 1)
      const prevDepth = depthByNode.get(node)
      if (prevDepth === undefined || depth < prevDepth) {
        depthByNode.set(node, depth)
      }
    }
    if (depth === MAX_BUBBLE_EDGES) {
      return
    }
    for (const { target } of adjacency.get(node) ?? []) {
      if (visited.has(target)) {
        continue
      }
      visited.add(target)
      walk(target, depth + 1, visited)
      visited.delete(target)
    }
  }

  for (const { target } of adjacency.get(entry) ?? []) {
    walk(target, 1, new Set([entry, target]))
  }

  let bestNode: number | undefined
  let bestDepth = Infinity
  for (const [node, count] of routeCountByNode) {
    if (count >= 2) {
      const depth = depthByNode.get(node)!
      if (depth < bestDepth) {
        bestDepth = depth
        bestNode = node
      }
    }
  }
  return bestNode
}

// entry phase id -> exit phase id, for every node that has a nearby
// reconvergence reachable via >=2 distinct short routes.
export function detectBubbleExits(results: ChartResult[]): Map<number, number> {
  const adjacency = buildAdjacency(results)
  const exitByEntry = new Map<number, number>()

  for (const [node, edges] of adjacency) {
    if (edges.length < 2) {
      continue
    }
    const exit = findBubbleExit(node, adjacency)
    if (exit !== undefined) {
      exitByEntry.set(node, exit)
    }
  }

  return exitByEntry
}
