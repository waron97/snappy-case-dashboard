import { createContext } from 'react'

export type CaseWorkspaceTab =
  | { kind: 'list' }
  | { kind: 'case'; id: number; label: string; renamed?: boolean }
  | { kind: 'field-config'; model: string; recordId: number; label: string; renamed?: boolean }

export function tabKey(tab: CaseWorkspaceTab): string {
  if (tab.kind === 'list') return 'list'
  if (tab.kind === 'case') return `case:${tab.id}`
  return `field-config:${tab.model}:${tab.recordId}`
}

export function tabPath(tab: CaseWorkspaceTab): string {
  if (tab.kind === 'list') return '/'
  if (tab.kind === 'case') return `/helpdesk.ticket/${tab.id}`
  return `/full-field-config/${tab.model}/${tab.recordId}`
}

export type CaseTabsContextValue = {
  tabs: CaseWorkspaceTab[]
  activeKey: string
  openCase: (id: number) => void
  openFieldConfig: (model: string, recordId: number) => void
  closeTab: (key: string) => void
  closeAll: () => void
  loadTabs: (tabs: CaseWorkspaceTab[]) => void
  setActive: (key: string) => void
  setLabel: (key: string, label: string) => void
  renameTab: (key: string, label: string) => void
}

export const CaseTabsContext = createContext<CaseTabsContextValue | null>(null)

export const LIST_TAB: CaseWorkspaceTab = { kind: 'list' }
