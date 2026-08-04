import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { useMatch, useNavigate } from 'react-router-dom'
import {
  CaseTabsContext,
  CaseWorkspaceTab,
  LIST_TAB,
  NO_PROCESS_ID,
  sanitizeTabs,
  tabKey,
  tabPath
} from '@/lib/caseWorkspaceContext'
import { getUiPref, setUiPref } from '@/lib/uiPrefs'
import { useSweepProgressBridge } from '@/lib/symphonyDeepSearch'

const PREF_KEY = 'caseWorkspaceOpenTabs'

// Only the open tabs are persisted, not which one was focused — restoring
// always starts on the list tab, so there's no startup race between
// "restore the active tab" and the URL -> tabs sync effect below.
async function loadPersistedTabs(): Promise<CaseWorkspaceTab[]> {
  const stored = await getUiPref<unknown>(PREF_KEY, [])
  return [LIST_TAB, ...sanitizeTabs(stored)]
}

export function CaseTabsProvider({ children }: { children: React.ReactNode }): React.JSX.Element {
  const [tabs, setTabs] = useState<CaseWorkspaceTab[]>([LIST_TAB])
  const [activeKey, setActiveKey] = useState<string>('list')
  // Guards the persist-write effect below: it must not overwrite storage
  // with the not-yet-restored [LIST_TAB] default before the deferred read
  // (see effect further down) has had a chance to run.
  const hasRestoredRef = useRef(false)
  const navigate = useNavigate()
  // Keep these patterns in sync with the isWorkspaceRoute guard in App.tsx —
  // both files have to agree on which routes CasesWorkspace owns.
  const matchCase = useMatch('/helpdesk.ticket/:id')
  const matchFieldConfig = useMatch('/full-field-config/:model/:record')
  const matchSymphonyList = useMatch('/symphony/requests')
  const matchSymphonyRequest = useMatch('/symphony/request/:requestId/:processId')
  const matchDeepSearch = useMatch('/symphony/deep-search/:jobId')
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

  // Singleton — there is only ever one Symphony list tab, so re-opening just
  // focuses it. Unlike LIST_TAB it is an ordinary closable tab.
  const openSymphonyList = useCallback(() => {
    const key = 'symphony-list'
    setTabs((prev) =>
      prev.some((t) => tabKey(t) === key)
        ? prev
        : [...prev, { kind: 'symphony-list', label: 'Symphony' }]
    )
    setActiveKey(key)
  }, [])

  const openSymphonyRequest = useCallback(
    (requestId: string, processId: string, label?: string) => {
      const key = `symphony-request:${requestId}`
      setTabs((prev) =>
        prev.some((t) => tabKey(t) === key)
          ? prev
          : [
              ...prev,
              {
                kind: 'symphony-request',
                requestId,
                processId: processId || NO_PROCESS_ID,
                label: label ?? `Req ${requestId.slice(0, 10)}`
              }
            ]
      )
      setActiveKey(key)
    },
    []
  )

  const openDeepSearch = useCallback((jobId: string, label?: string) => {
    const key = `symphony-deep-search:${jobId}`
    setTabs((prev) =>
      prev.some((t) => tabKey(t) === key)
        ? prev
        : [...prev, { kind: 'symphony-deep-search', jobId, label: label ?? 'Deep search' }]
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

  // The default Electron menu's CmdOrCtrl+W closes the whole window/app (see
  // buildAppMenu in src/main/index.ts, which deliberately drops that
  // accelerator) — here it instead closes just the active tab, matching
  // browser-tab conventions. No-op on the permanent list tab.
  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent): void {
      const isCloseShortcut = (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'w'
      if (!isCloseShortcut || activeKey === 'list') return
      e.preventDefault()
      closeTab(activeKey)
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [activeKey, closeTab])

  const closeAll = useCallback(() => {
    setTabs([LIST_TAB])
    setActiveKey('list')
    navigate('/')
  }, [navigate])

  const loadTabs = useCallback(
    (next: CaseWorkspaceTab[]) => {
      // Saved tab sets come off disk as unknown[], so they get the same
      // validation as the persisted open-tabs pref — a set written by a newer
      // build must not be able to inject a tab shape this build can't render.
      setTabs([LIST_TAB, ...sanitizeTabs(next)])
      setActiveKey('list')
      navigate('/')
    },
    [navigate]
  )

  useEffect(() => {
    if (!hasRestoredRef.current) return
    const nonListTabs = tabs.filter((t) => t.kind !== 'list')
    setUiPref(PREF_KEY, nonListTabs)
  }, [tabs])

  useEffect(() => {
    // The restore is async (an IPC round-trip, not localStorage), so merge
    // rather than overwrite: the user may have already opened a tab (e.g.
    // clicked a case from the list) in the — now much smaller, but still
    // real — window before this resolves.
    let cancelled = false
    loadPersistedTabs().then((persisted) => {
      if (cancelled) return
      setTabs((current) => {
        const currentKeys = new Set(current.map(tabKey))
        const merged = [...current, ...persisted.filter((t) => !currentKeys.has(tabKey(t)))]
        return merged
      })
      hasRestoredRef.current = true
    })
    return () => {
      cancelled = true
    }
  }, [])

  // Syncs URL -> tab state, so any plain <Link>/navigate() elsewhere in the
  // app (relation chips, parent/child links, Ctrl+E jump, the field-inspector
  // "</>" buttons) opens/focuses a tab without needing to know about the tab
  // system at all. This has to be a real useEffect, not a render-phase state
  // adjustment: doing the tabs/activeKey update directly during render caused
  // them to oscillate indefinitely under StrictMode's double-render, since it
  // chains multiple interdependent state variables in one conditional block.
  // Scalars, not the match objects: useMatch returns a fresh object every
  // render, so depending on it directly re-runs this effect constantly.
  const caseIdParam = matchCase?.params.id
  const fieldConfigModel = matchFieldConfig?.params.model
  const fieldConfigRecord = matchFieldConfig?.params.record
  const symphonyRequestId = matchSymphonyRequest?.params.requestId
  const symphonyProcessId = matchSymphonyRequest?.params.processId
  const deepSearchJobId = matchDeepSearch?.params.jobId
  const isSymphonyList = !!matchSymphonyList
  const isList = !!matchList
  useEffect(() => {
    /* eslint-disable react-hooks/set-state-in-effect --
       Subscribing to the router (an external system), not deriving state
       from a prop — the case this lint rule is meant to steer away from. */
    if (caseIdParam) {
      openCase(parseInt(caseIdParam, 10))
    } else if (fieldConfigModel && fieldConfigRecord) {
      openFieldConfig(fieldConfigModel, parseInt(fieldConfigRecord, 10))
    } else if (symphonyRequestId && symphonyProcessId) {
      openSymphonyRequest(
        decodeURIComponent(symphonyRequestId),
        decodeURIComponent(symphonyProcessId)
      )
    } else if (deepSearchJobId) {
      openDeepSearch(decodeURIComponent(deepSearchJobId))
    } else if (isSymphonyList) {
      openSymphonyList()
    } else if (isList) {
      setActive('list')
    }
    /* eslint-enable react-hooks/set-state-in-effect */
  }, [
    caseIdParam,
    fieldConfigModel,
    fieldConfigRecord,
    symphonyRequestId,
    symphonyProcessId,
    deepSearchJobId,
    isSymphonyList,
    isList,
    openCase,
    openFieldConfig,
    openSymphonyList,
    openSymphonyRequest,
    openDeepSearch,
    setActive
  ])

  const value = useMemo(
    () => ({
      tabs,
      activeKey,
      openCase,
      openFieldConfig,
      openSymphonyList,
      openSymphonyRequest,
      openDeepSearch,
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
      openSymphonyList,
      openSymphonyRequest,
      openDeepSearch,
      closeTab,
      closeAll,
      loadTabs,
      setActive,
      setLabel,
      renameTab
    ]
  )

  return (
    <CaseTabsContext.Provider value={value}>
      <SweepProgressBridge />
      {children}
    </CaseTabsContext.Provider>
  )
}

/** Single subscriber to the main-process deep-search progress push. Mounted here
 *  so it lives for as long as the workspace does, regardless of which tabs are
 *  open — a sweep keeps running with its tab closed. */
function SweepProgressBridge(): null {
  useSweepProgressBridge()
  return null
}
