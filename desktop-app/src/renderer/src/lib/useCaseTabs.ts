import { useContext } from 'react'
import { CaseTabsContext, CaseTabsContextValue } from '@/lib/caseWorkspaceContext'

export type { CaseWorkspaceTab } from '@/lib/caseWorkspaceContext'
export { tabKey, tabPath } from '@/lib/caseWorkspaceContext'

export function useCaseTabs(): CaseTabsContextValue {
  const ctx = useContext(CaseTabsContext)
  if (!ctx) {
    throw new Error('useCaseTabs must be used within a CaseTabsProvider')
  }
  return ctx
}
