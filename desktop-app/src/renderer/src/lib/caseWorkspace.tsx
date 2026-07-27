import { useCallback, useEffect, useMemo, useState } from 'react'
import { useMatch, useNavigate } from 'react-router-dom'
import { CaseTab, CaseTabsContext, LIST_TAB } from '@/lib/caseWorkspaceContext'

const STORAGE_KEY = 'caseWorkspace.openTabs.v1'

// Only the open case ids/labels are persisted, not which tab was focused —
// restoring always starts on the list tab, so there's no startup race
// between "restore the active tab" and the URL -> tabs sync effect below.
function loadPersistedTabs(): CaseTab[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) return [LIST_TAB]
    const parsed = JSON.parse(raw)
    if (!Array.isArray(parsed)) return [LIST_TAB]
    const caseTabs = parsed
      .filter((t): t is CaseTab => typeof t?.id === 'number' && typeof t?.label === 'string')
      .map((t) => ({ ...t, renamed: t.renamed === true }))
    return [LIST_TAB, ...caseTabs]
  } catch {
    return [LIST_TAB]
  }
}

export function CaseTabsProvider({ children }: { children: React.ReactNode }): React.JSX.Element {
  const [tabs, setTabs] = useState<CaseTab[]>(loadPersistedTabs)
  const [activeId, setActiveId] = useState<'list' | number>('list')
  const navigate = useNavigate()
  const matchDetail = useMatch('/helpdesk.ticket/:id')
  const matchList = useMatch('/')

  const openCase = useCallback((id: number) => {
    setTabs((prev) =>
      prev.some((t) => t.id === id) ? prev : [...prev, { id, label: `Case #${id}` }]
    )
    setActiveId(id)
  }, [])

  const setActive = useCallback((id: 'list' | number) => {
    setActiveId(id)
  }, [])

  const setLabel = useCallback((id: number, label: string) => {
    setTabs((prev) => {
      const tab = prev.find((t) => t.id === id)
      if (!tab || tab.renamed || tab.label === label) return prev
      return prev.map((t) => (t.id === id ? { ...t, label } : t))
    })
  }, [])

  const renameTab = useCallback((id: number, label: string) => {
    const trimmed = label.trim()
    if (!trimmed) return
    setTabs((prev) => prev.map((t) => (t.id === id ? { ...t, label: trimmed, renamed: true } : t)))
  }, [])

  const closeCase = useCallback(
    (id: number) => {
      setTabs((prev) => {
        const index = prev.findIndex((t) => t.id === id)
        if (index === -1) return prev
        const next = prev.filter((t) => t.id !== id)
        setActiveId((current) => {
          if (current !== id) return current
          const fallback = next[index - 1] ?? next[0] ?? LIST_TAB
          navigate(fallback.id === 'list' ? '/' : `/helpdesk.ticket/${fallback.id}`)
          return fallback.id
        })
        return next
      })
    },
    [navigate]
  )

  const closeAll = useCallback(() => {
    setTabs([LIST_TAB])
    setActiveId('list')
    navigate('/')
  }, [navigate])

  useEffect(() => {
    const caseTabs = tabs.filter((t) => t.id !== 'list')
    localStorage.setItem(STORAGE_KEY, JSON.stringify(caseTabs))
  }, [tabs])

  // Syncs URL -> tab state, so any plain <Link>/navigate() elsewhere in the
  // app (relation chips, parent/child links, Ctrl+E jump) opens/focuses a tab
  // without needing to know about the tab system at all. This has to be a
  // real useEffect, not a render-phase state adjustment: doing the tabs/activeId
  // update directly during render caused the two to oscillate indefinitely
  // under StrictMode's double-render, since it chains multiple interdependent
  // state variables (syncedKey + tabs + activeId) in one conditional block.
  const idParam = matchDetail?.params.id
  useEffect(() => {
    /* eslint-disable react-hooks/set-state-in-effect --
       Subscribing to the router (an external system), not deriving state
       from a prop — the case this lint rule is meant to steer away from. */
    if (idParam) {
      openCase(parseInt(idParam, 10))
    } else if (matchList) {
      setActive('list')
    }
    /* eslint-enable react-hooks/set-state-in-effect */
  }, [idParam, matchList, openCase, setActive])

  const value = useMemo(
    () => ({ tabs, activeId, openCase, closeCase, closeAll, setActive, setLabel, renameTab }),
    [tabs, activeId, openCase, closeCase, closeAll, setActive, setLabel, renameTab]
  )

  return <CaseTabsContext.Provider value={value}>{children}</CaseTabsContext.Provider>
}
