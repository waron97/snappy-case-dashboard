import { createContext } from 'react'

export type CaseTab = {
  id: 'list' | number
  label: string
  // true once the user has manually renamed this tab — blocks the
  // auto-label-from-case-name sync (CaseDetail's onNameResolved) from
  // clobbering it.
  renamed?: boolean
}

export type CaseTabsContextValue = {
  tabs: CaseTab[]
  activeId: 'list' | number
  openCase: (id: number) => void
  closeCase: (id: number) => void
  closeAll: () => void
  setActive: (id: 'list' | number) => void
  setLabel: (id: number, label: string) => void
  renameTab: (id: number, label: string) => void
}

export const CaseTabsContext = createContext<CaseTabsContextValue | null>(null)

export const LIST_TAB: CaseTab = { id: 'list', label: 'Cases' }
