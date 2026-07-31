import { useQuery, type UseQueryResult } from '@tanstack/react-query'
import { useEffect, useState } from 'react'
import {
  getHistoricActivities,
  getHistoricVariables,
  getRequestDetailHtml,
  type SymphonyActivity,
  type SymphonyExecutionNode,
  type SymphonyVariable
} from '@/lib/symphony-api'
import { parseExecutionTree } from '@/lib/symphonyDetailHtml'

/** One request per page; the observed sample fits in a single size=1000 page,
 *  and the guard stops a runaway loop if last_page is ever wrong. */
const PAGE_SIZE = 1000
const MAX_PAGES = 10

const FIVE_MINUTES = 5 * 60 * 1000

/**
 * Every open Symphony tab's panel stays mounted (CasesWorkspace uses
 * keepMounted), and one process instance's variables can be several megabytes.
 * Restoring a saved tab set with eight request tabs would otherwise fetch all of
 * them at once. So a tab fetches only once it has actually been visited — and
 * keeps its data afterwards so switching back is instant.
 */
export function useVisitedGate(isActive: boolean): boolean {
  // Render-phase adjustment rather than an effect: the gate has to be true on
  // the very first render in which the tab becomes active, or the query would
  // stay disabled for one extra frame. This is React's documented pattern for
  // deriving state from props (it re-renders immediately, before committing).
  const [visited, setVisited] = useState(isActive)
  if (isActive && !visited) {
    setVisited(true)
  }
  return visited
}

/**
 * Fetches ALL variables, not a page.
 *
 * This is the whole point of the feature: the legacy UI paginates at 100/page
 * and its column filters only match the rows currently rendered, so a process
 * with 172 variables cannot be searched. One flat array makes filtering a
 * client-side pass over the complete set.
 */
export function useSymphonyVariables(
  processInstanceId: string | null,
  isActive: boolean
): UseQueryResult<SymphonyVariable[], Error> {
  const enabled = useVisitedGate(isActive) && Boolean(processInstanceId)

  return useQuery({
    queryKey: ['symphony', 'variables', processInstanceId],
    queryFn: async () => {
      const all: SymphonyVariable[] = []
      let page = 1
      for (;;) {
        const response = await getHistoricVariables(processInstanceId as string, page, PAGE_SIZE)
        all.push(...(response.data ?? []))
        const lastPage = response.last_page ?? 1
        if (page >= lastPage || page >= MAX_PAGES) {
          break
        }
        page++
      }
      return all
    },
    enabled,
    staleTime: FIVE_MINUTES,
    gcTime: FIVE_MINUTES,
    retry: false
  })
}

export function useSymphonyActivities(
  processInstanceId: string | null,
  isActive: boolean
): UseQueryResult<SymphonyActivity[], Error> {
  const enabled = useVisitedGate(isActive) && Boolean(processInstanceId)

  return useQuery({
    queryKey: ['symphony', 'activities', processInstanceId],
    queryFn: async () => {
      const all: SymphonyActivity[] = []
      let page = 1
      for (;;) {
        const response = await getHistoricActivities(processInstanceId as string, page, PAGE_SIZE)
        all.push(...(response.data ?? []))
        const lastPage = response.last_page ?? 1
        if (page >= lastPage || page >= MAX_PAGES) {
          break
        }
        page++
      }
      return all
    },
    enabled,
    staleTime: FIVE_MINUTES,
    gcTime: FIVE_MINUTES,
    retry: false
  })
}

/**
 * Fetches the execution tree's root node (with one level of children already
 * embedded) for the Child Processes tab. Deeper levels are fetched on demand
 * as the user expands `has-children` nodes — see components/SymphonyChildProcesses.
 */
export function useSymphonyExecutionTree(
  requestId: string | null,
  isActive: boolean
): UseQueryResult<SymphonyExecutionNode | null, Error> {
  const enabled = useVisitedGate(isActive) && Boolean(requestId)

  return useQuery({
    queryKey: ['symphony', 'executionTree', requestId],
    queryFn: async () => {
      const html = await getRequestDetailHtml(requestId as string, null, { onlyContent: false })
      return parseExecutionTree(html)
    },
    enabled,
    staleTime: FIVE_MINUTES,
    gcTime: FIVE_MINUTES,
    retry: false
  })
}

/** Pushes a resolved label up to the tab strip, mirroring CaseDetail. */
export function useResolvedTabName(
  name: string | undefined,
  onNameResolved: ((name: string) => void) | undefined
): void {
  useEffect(() => {
    if (name) {
      onNameResolved?.(name)
    }
  }, [name, onNameResolved])
}
