import { MAX_BUBBLE_EDGES } from './bubbles'
import { ChartPath } from './pathfinding'

// viaResultId is the edge that connects this node to the previous backbone
// node, when that hop wasn't folded into a bubble (undefined for the very
// first node in a path, and unused when the previous token is a bubble —
// the bubble's own routes already draw the edge converging into this node).
export type NodeToken = { type: 'node'; phaseId: number; viaResultId?: number }
export type BubbleToken = {
  type: 'bubble'
  entry: number
  exit: number
  // Distinct short entry->exit routes actually observed among this group's
  // member paths (each inclusive of entry and exit).
  routes: ChartPath[]
}
export type BackboneToken = NodeToken | BubbleToken

export type PathGroup = {
  paths: ChartPath[]
  backbone: BackboneToken[]
}

export type HighlightedGroup = {
  groupIndex: number
  backbone: BackboneToken[]
  phaseIds: number[]
  resultIds: number[]
}

function replayPath(path: ChartPath, bubbleExitByEntry: Map<number, number>): BackboneToken[] {
  const backbone: BackboneToken[] = []
  let i = 0

  while (i < path.phaseIds.length) {
    const node = path.phaseIds[i]
    const exit = bubbleExitByEntry.get(node)
    let collapsed = false

    if (exit !== undefined) {
      const maxLookahead = Math.min(path.phaseIds.length - 1, i + MAX_BUBBLE_EDGES)
      for (let j = i + 1; j <= maxLookahead; j++) {
        if (path.phaseIds[j] === exit) {
          backbone.push({
            type: 'bubble',
            entry: node,
            exit,
            routes: [
              {
                phaseIds: path.phaseIds.slice(i, j + 1),
                resultIds: path.resultIds.slice(i, j)
              }
            ]
          })
          i = j
          collapsed = true
          break
        }
      }
    }

    if (!collapsed) {
      backbone.push({
        type: 'node',
        phaseId: node,
        viaResultId: i > 0 ? path.resultIds[i - 1] : undefined
      })
      i += 1
    }
  }

  return backbone
}

function signatureOf(backbone: BackboneToken[]): string {
  return backbone
    .map((token) => (token.type === 'node' ? `n${token.phaseId}` : `b${token.entry}-${token.exit}`))
    .join('|')
}

export function groupPaths(
  paths: ChartPath[],
  bubbleExitByEntry: Map<number, number>
): PathGroup[] {
  const groupsBySignature = new Map<string, PathGroup>()

  for (const path of paths) {
    const backbone = replayPath(path, bubbleExitByEntry)
    const signature = signatureOf(backbone)

    let group = groupsBySignature.get(signature)
    if (!group) {
      group = { paths: [], backbone }
      groupsBySignature.set(signature, group)
    }
    group.paths.push(path)

    for (let k = 0; k < group.backbone.length; k++) {
      const existingToken = group.backbone[k]
      const newToken = backbone[k]
      if (existingToken.type === 'bubble' && newToken.type === 'bubble') {
        const seen = new Set(existingToken.routes.map((route) => route.phaseIds.join(',')))
        for (const route of newToken.routes) {
          const key = route.phaseIds.join(',')
          if (!seen.has(key)) {
            existingToken.routes.push(route)
            seen.add(key)
          }
        }
      }
    }
  }

  return Array.from(groupsBySignature.values())
}

export function highlightForGroup(groupIndex: number, group: PathGroup): HighlightedGroup {
  const phaseIds = new Set<number>()
  const resultIds = new Set<number>()

  for (const path of group.paths) {
    path.phaseIds.forEach((id) => phaseIds.add(id))
    path.resultIds.forEach((id) => resultIds.add(id))
  }

  return {
    groupIndex,
    backbone: group.backbone,
    phaseIds: Array.from(phaseIds),
    resultIds: Array.from(resultIds)
  }
}
