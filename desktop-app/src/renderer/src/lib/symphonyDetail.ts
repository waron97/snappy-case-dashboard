import { useQuery, type UseQueryResult } from '@tanstack/react-query'
import { useResolvedTabName, useVisitedGate } from '@/lib/tabActive'
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

// Moved to lib/tabActive once non-Symphony pages became tabs too; re-exported
// here so the existing Symphony imports keep working.
export { useVisitedGate }

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

export { useResolvedTabName }
