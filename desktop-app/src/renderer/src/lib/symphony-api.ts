// Renderer shim over window.api.symphony — same role as odoo-api.ts. No hooks
// here; react-query lives in the sibling lib/symphony*.ts modules.

export type {
  SymphonyActivitiesPage,
  SymphonyActivity,
  SymphonyExecutionNode,
  SymphonyExecutionNodeQuery,
  SymphonyIconConfig,
  SymphonyProcessKey,
  SymphonyProcessKeyCatalog,
  SymphonyRequestDetailOptions,
  SymphonyRequestRow,
  SymphonyRequestStatus,
  SymphonyRequestTreePage,
  SymphonyRequestTreeQuery,
  SymphonySorter,
  SymphonyVariable,
  SymphonyVariablesPage
} from '../../../main/backend/symphony/types'

import type {
  SymphonyActivitiesPage,
  SymphonyExecutionNodeQuery,
  SymphonyRequestDetailOptions,
  SymphonyRequestTreePage,
  SymphonyRequestTreeQuery,
  SymphonyVariablesPage
} from '../../../main/backend/symphony/types'

/** Kept in sync with SYMPHONY_STATUSES in backend/symphony/types.ts. Duplicated
 *  rather than imported so nothing in the renderer bundle reaches into main at
 *  runtime — every other cross-boundary import in this app is type-only. */
export const SYMPHONY_STATUSES = [
  'CANCELLED',
  'NEW',
  'COMPLETED',
  'WORKING',
  'FAILED'
] as const satisfies readonly string[]

export async function getRequestTree(
  query: SymphonyRequestTreeQuery
): Promise<SymphonyRequestTreePage> {
  return window.api.symphony.getRequestTree(query) as Promise<SymphonyRequestTreePage>
}

export async function getHistoricVariables(
  processInstanceId: string,
  page?: number,
  size?: number
): Promise<SymphonyVariablesPage> {
  return window.api.symphony.getHistoricVariables(
    processInstanceId,
    page,
    size
  ) as Promise<SymphonyVariablesPage>
}

export async function getHistoricActivities(
  processInstanceId: string,
  page?: number,
  size?: number
): Promise<SymphonyActivitiesPage> {
  return window.api.symphony.getHistoricActivities(
    processInstanceId,
    page,
    size
  ) as Promise<SymphonyActivitiesPage>
}

export async function getRequestDetailHtml(
  requestId: string,
  parentId: string | null,
  opts?: SymphonyRequestDetailOptions
): Promise<string> {
  return window.api.symphony.getRequestDetailHtml(requestId, parentId, opts)
}

export async function getExecutionTreeNode(
  nodeId: string,
  query: SymphonyExecutionNodeQuery
): Promise<string> {
  return window.api.symphony.getExecutionTreeNode(nodeId, query)
}
