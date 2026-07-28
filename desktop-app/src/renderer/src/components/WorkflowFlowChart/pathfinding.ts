import { ChartResult } from './layout'

export type ChartPath = { phaseIds: number[]; resultIds: number[] }

export const MAX_PATHS = 300

export function findAllSimplePaths(
  startPhaseId: number,
  targetPhaseId: number,
  results: ChartResult[]
): { paths: ChartPath[]; truncated: boolean } {
  if (startPhaseId === targetPhaseId) {
    return { paths: [{ phaseIds: [startPhaseId], resultIds: [] }], truncated: false }
  }

  const adjacency = new Map<number, Array<{ target: number; resultId: number }>>()
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

  const paths: ChartPath[] = []
  const visited = new Set<number>([startPhaseId])
  const phaseIds: number[] = [startPhaseId]
  const resultIds: number[] = []

  function dfs(current: number): void {
    if (paths.length >= MAX_PATHS) {
      return
    }

    for (const { target, resultId } of adjacency.get(current) ?? []) {
      if (paths.length >= MAX_PATHS) {
        return
      }
      if (visited.has(target)) {
        continue
      }

      phaseIds.push(target)
      resultIds.push(resultId)
      visited.add(target)

      if (target === targetPhaseId) {
        paths.push({ phaseIds: [...phaseIds], resultIds: [...resultIds] })
      } else {
        dfs(target)
      }

      visited.delete(target)
      resultIds.pop()
      phaseIds.pop()
    }
  }

  dfs(startPhaseId)

  return { paths, truncated: paths.length >= MAX_PATHS }
}
