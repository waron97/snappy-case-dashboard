export type { DevOpsWorkItem } from '../../../main/backend/devops'
import type { DevOpsWorkItem } from '../../../main/backend/devops'

export async function getMyWorkItems(): Promise<DevOpsWorkItem[]> {
  return window.api.devops.getMyWorkItems() as Promise<DevOpsWorkItem[]>
}
