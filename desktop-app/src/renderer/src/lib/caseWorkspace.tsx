import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import {
  CaseTabsContext,
  CaseWorkspaceTab,
  defaultLabel,
  isNonTabPath,
  LIST_TAB,
  sanitizeTabs,
  TabIdentity,
  tabFromPath,
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
  const { pathname } = useLocation()

  // useNavigate hands back a new function identity after every navigation (there
  // is no data router here, so useNavigateUnstable is what runs and its deps
  // include the current pathname), and useLocation returns a fresh object every
  // render. Both are mirrored into refs so that the callbacks below and the
  // URL -> tab effect can depend on the pathname *string* alone.
  const navigateRef = useRef(navigate)
  const pathnameRef = useRef(pathname)
  useEffect(() => {
    navigateRef.current = navigate
    pathnameRef.current = pathname
  }, [navigate, pathname])

  /**
   * Pure state: adds the tab if it isn't open yet, then focuses it. Never
   * navigates, which is what makes the URL -> tab effect a one-way sink and rules
   * out a URL/state ping-pong entirely.
   *
   * Append-if-absent is a contract, not an optimisation. tabKey for
   * symphony-request ignores processId so a '-' placeholder and its resolved
   * counterpart share a key; upserting here would push the placeholder back over
   * a resolved id, and would also wipe a label the user had renamed.
   */
  const applyTab = useCallback((tab: TabIdentity, label?: string) => {
    const key = tabKey(tab)
    if (tab.kind !== 'list') {
      setTabs((prev) =>
        prev.some((t) => tabKey(t) === key)
          ? prev
          : [...prev, { ...tab, label: label ?? defaultLabel(tab) }]
      )
    }
    setActiveKey(key)
  }, [])

  /** The public opener: state plus the URL. Everything user-initiated goes
   *  through here — the tab strip, the header nav, the one imperative caller. */
  const openTab = useCallback(
    (tab: TabIdentity, label?: string) => {
      applyTab(tab, label)
      const path = tabPath(tab)
      // useNavigate always pushes, unlike <Link> which self-dedupes, so
      // re-opening the tab you're already on would add a history entry per click.
      navigateRef.current(path, { replace: pathnameRef.current === path })
    },
    [applyTab]
  )

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

  // The side effects deliberately sit outside the setTabs updater: React 19's
  // StrictMode double-invokes updater functions in development, so calling
  // setActiveKey/navigate from inside one fired them repeatedly per close.
  const closeTab = useCallback(
    (key: string) => {
      const index = tabs.findIndex((t) => tabKey(t) === key)
      if (index === -1) return
      const next = tabs.filter((t) => tabKey(t) !== key)
      setTabs(next)
      if (activeKey !== key) return
      const fallback = next[index - 1] ?? next[0] ?? LIST_TAB
      setActiveKey(tabKey(fallback))
      navigateRef.current(tabPath(fallback), { replace: true })
    },
    [tabs, activeKey]
  )

  // The default Electron menu's CmdOrCtrl+W closes the whole window/app (see
  // buildAppMenu in src/main/index.ts, which deliberately drops that
  // accelerator) — here it instead closes just the active tab, matching
  // browser-tab conventions. No-op on the permanent list tab, and on paths that
  // aren't part of the workspace at all: the provider stays mounted while
  // /settings is open, where closing an invisible tab would also navigate the
  // user off a half-filled credentials form.
  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent): void {
      const isCloseShortcut = (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'w'
      if (!isCloseShortcut || activeKey === 'list' || isNonTabPath(pathname)) return
      e.preventDefault()
      closeTab(activeKey)
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [activeKey, closeTab, pathname])

  const closeAll = useCallback(() => {
    setTabs([LIST_TAB])
    setActiveKey('list')
    navigateRef.current('/')
  }, [])

  const loadTabs = useCallback((next: CaseWorkspaceTab[]) => {
    // Saved tab sets come off disk as unknown[], so they get the same
    // validation as the persisted open-tabs pref — a set written by a newer
    // build must not be able to inject a tab shape this build can't render.
    setTabs([LIST_TAB, ...sanitizeTabs(next)])
    setActiveKey('list')
    navigateRef.current('/')
  }, [])

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
  // system at all. TAB_ROUTES in caseWorkspaceContext.ts is the only route table
  // in the app; there is no <Routes> switch to keep in sync with it.
  //
  // This has to be a real useEffect, not a render-phase state adjustment: doing
  // the tabs/activeKey update directly during render caused them to oscillate
  // indefinitely under StrictMode's double-render, since it chains multiple
  // interdependent state variables in one conditional block. It is safe under
  // that double-invocation because applyTab is idempotent — setTabs returns
  // `prev` for a tab that's already open, and setActiveKey bails on an equal
  // string.
  useEffect(() => {
    /* eslint-disable react-hooks/set-state-in-effect --
       Subscribing to the router (an external system), not deriving state
       from a prop — the case this lint rule is meant to steer away from. */
    const tab = tabFromPath(pathname)
    if (tab) {
      applyTab(tab)
    } else if (!isNonTabPath(pathname)) {
      // No <Routes> fallback exists any more, so an unknown URL would otherwise
      // leave the last active tab on screen under a URL that disagrees with it —
      // and a reload would make that mismatch stick. `replace` so Back doesn't
      // bounce straight back into the bad URL.
      navigateRef.current('/', { replace: true })
    }
    /* eslint-enable react-hooks/set-state-in-effect */
  }, [pathname, applyTab])

  const value = useMemo(
    () => ({
      tabs,
      activeKey,
      openTab,
      closeTab,
      closeAll,
      loadTabs,
      setLabel,
      renameTab
    }),
    [tabs, activeKey, openTab, closeTab, closeAll, loadTabs, setLabel, renameTab]
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
