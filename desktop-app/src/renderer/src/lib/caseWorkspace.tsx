import { useCallback, useEffect, useMemo, useState } from 'react'
import { useMatch, useNavigate } from 'react-router-dom'
import {
  CaseTabsContext,
  CaseWorkspaceTab,
  LIST_TAB,
  tabKey,
  tabPath
} from '@/lib/caseWorkspaceContext'

const STORAGE_KEY = 'caseWorkspace.openTabs.v2'

// Only the open tabs are persisted, not which one was focused — restoring
// always starts on the list tab, so there's no startup race between
// "restore the active tab" and the URL -> tabs sync effect below.
function loadPersistedTabs(): CaseWorkspaceTab[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) return [LIST_TAB]
    const parsed = JSON.parse(raw)
    if (!Array.isArray(parsed)) return [LIST_TAB]
    const tabs = parsed
      .filter((t): t is Extract<CaseWorkspaceTab, { kind: 'case' | 'field-config' }> => {
        if (typeof t?.label !== 'string') return false
        if (t.kind === 'case') return typeof t.id === 'number'
        if (t.kind === 'field-config')
          return typeof t.model === 'string' && typeof t.recordId === 'number'
        return false
      })
      .map((t) => ({ ...t, renamed: t.renamed === true }))
    return [LIST_TAB, ...tabs]
  } catch {
    return [LIST_TAB]
  }
}

export function CaseTabsProvider({ children }: { children: React.ReactNode }): React.JSX.Element {
  const [tabs, setTabs] = useState<CaseWorkspaceTab[]>(loadPersistedTabs)
  const [activeKey, setActiveKey] = useState<string>('list')
  const navigate = useNavigate()
  const matchCase = useMatch('/helpdesk.ticket/:id')
  const matchFieldConfig = useMatch('/full-field-config/:model/:record')
  const matchList = useMatch('/')

  const setActive = useCallback((key: string) => {
    setActiveKey(key)
  }, [])

  const openCase = useCallback((id: number) => {
    const key = `case:${id}`
    setTabs((prev) =>
      prev.some((t) => tabKey(t) === key)
        ? prev
        : [...prev, { kind: 'case', id, label: `Case #${id}` }]
    )
    setActiveKey(key)
  }, [])

  const openFieldConfig = useCallback((model: string, recordId: number) => {
    const key = `field-config:${model}:${recordId}`
    setTabs((prev) =>
      prev.some((t) => tabKey(t) === key)
        ? prev
        : [...prev, { kind: 'field-config', model, recordId, label: `${model} #${recordId}` }]
    )
    setActiveKey(key)
  }, [])

  const setLabel = useCallback((key: string, label: string) => {
    setTabs((prev) => {
      const tab = prev.find((t) => tabKey(t) === key)
      if (!tab || tab.kind === 'list' || tab.renamed || tab.label === label) return prev
      return prev.map((t) => (tabKey(t) === key && t.kind !== 'list' ? { ...t, label } : t))
    })
  }, [])

  const renameTab = useCallback((key: string, label: string) => {
    const trimmed = label.trim()
    if (!trimmed) return
    setTabs((prev) =>
      prev.map((t) =>
        tabKey(t) === key && t.kind !== 'list' ? { ...t, label: trimmed, renamed: true } : t
      )
    )
  }, [])

  const closeTab = useCallback(
    (key: string) => {
      setTabs((prev) => {
        const index = prev.findIndex((t) => tabKey(t) === key)
        if (index === -1) return prev
        const next = prev.filter((t) => tabKey(t) !== key)
        setActiveKey((current) => {
          if (current !== key) return current
          const fallback = next[index - 1] ?? next[0] ?? LIST_TAB
          navigate(tabPath(fallback))
          return tabKey(fallback)
        })
        return next
      })
    },
    [navigate]
  )

  const closeAll = useCallback(() => {
    setTabs([LIST_TAB])
    setActiveKey('list')
    navigate('/')
  }, [navigate])

  const loadTabs = useCallback(
    (next: CaseWorkspaceTab[]) => {
      setTabs([LIST_TAB, ...next.filter((t) => t.kind !== 'list')])
      setActiveKey('list')
      navigate('/')
    },
    [navigate]
  )

  useEffect(() => {
    const nonListTabs = tabs.filter((t) => t.kind !== 'list')
    localStorage.setItem(STORAGE_KEY, JSON.stringify(nonListTabs))
  }, [tabs])

  // Syncs URL -> tab state, so any plain <Link>/navigate() elsewhere in the
  // app (relation chips, parent/child links, Ctrl+E jump, the field-inspector
  // "</>" buttons) opens/focuses a tab without needing to know about the tab
  // system at all. This has to be a real useEffect, not a render-phase state
  // adjustment: doing the tabs/activeKey update directly during render caused
  // them to oscillate indefinitely under StrictMode's double-render, since it
  // chains multiple interdependent state variables in one conditional block.
  const caseIdParam = matchCase?.params.id
  const fieldConfigModel = matchFieldConfig?.params.model
  const fieldConfigRecord = matchFieldConfig?.params.record
  useEffect(() => {
    /* eslint-disable react-hooks/set-state-in-effect --
       Subscribing to the router (an external system), not deriving state
       from a prop — the case this lint rule is meant to steer away from. */
    if (caseIdParam) {
      openCase(parseInt(caseIdParam, 10))
    } else if (fieldConfigModel && fieldConfigRecord) {
      openFieldConfig(fieldConfigModel, parseInt(fieldConfigRecord, 10))
    } else if (matchList) {
      setActive('list')
    }
    /* eslint-enable react-hooks/set-state-in-effect */
  }, [
    caseIdParam,
    fieldConfigModel,
    fieldConfigRecord,
    matchList,
    openCase,
    openFieldConfig,
    setActive
  ])

  const value = useMemo(
    () => ({
      tabs,
      activeKey,
      openCase,
      openFieldConfig,
      closeTab,
      closeAll,
      loadTabs,
      setActive,
      setLabel,
      renameTab
    }),
    [
      tabs,
      activeKey,
      openCase,
      openFieldConfig,
      closeTab,
      closeAll,
      loadTabs,
      setActive,
      setLabel,
      renameTab
    ]
  )

  return <CaseTabsContext.Provider value={value}>{children}</CaseTabsContext.Provider>
}
