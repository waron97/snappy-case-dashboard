import { createContext, useContext, useEffect, useState } from 'react'

/**
 * Whether the tab panel a component lives in is the visible one.
 *
 * Provided per panel by CasesWorkspace. The default is `true` so anything
 * rendered outside the tab strip (the settings page, the Ctrl+E modal, the
 * save-tab-set dialog) behaves exactly as it did before this existed.
 *
 * Two things need it beyond fetch gating: Mantine's Modal/Drawer/Popover portal
 * to document.body, so an overlay left open in a background panel is *not*
 * hidden by the panel's `display: none` — it floats over whichever tab you
 * switched to, and its lockScroll/trapFocus keep working there. Gating `opened`
 * on this context is the fix.
 */
const TabActiveContext = createContext(true)

export const TabActiveProvider = TabActiveContext.Provider

export function useTabIsActive(): boolean {
  return useContext(TabActiveContext)
}

/**
 * Every open tab's panel stays mounted (CasesWorkspace uses keepMounted), so a
 * restored session would otherwise fetch every tab at once — one Symphony
 * process's variables alone can be several megabytes, and an MFA record holds
 * five queries plus a CodeMirror instance. So a tab fetches only once it has
 * actually been visited — and keeps its data afterwards so switching back is
 * instant.
 *
 * Note what this does and does not buy: it suppresses the *first* fetch for a
 * never-visited tab. Once visited, that panel's queries are live for the rest of
 * the session — window-focus refetches, polls and retries included.
 */
export function useVisitedGate(isActive: boolean): boolean {
  // Render-phase adjustment rather than an effect: the gate has to be true on
  // the very first render in which the tab becomes active, or the query would
  // stay disabled for one extra frame. This is React's documented pattern for
  // deriving state from props (it re-renders immediately, before committing).
  const [visited, setVisited] = useState(isActive)
  if (isActive && !visited) {
    setVisited(true)
  }
  return visited
}

/** useVisitedGate for components deep inside a panel, which would otherwise need
 *  `isActive` prop-drilled through every intermediate component. */
export function useTabVisited(): boolean {
  return useVisitedGate(useTabIsActive())
}

/** Pushes a resolved label up to the tab strip, mirroring CaseDetail. setLabel
 *  ignores it once the user has renamed the tab by hand. */
export function useResolvedTabName(
  name: string | undefined,
  onNameResolved: ((name: string) => void) | undefined
): void {
  useEffect(() => {
    if (name) {
      onNameResolved?.(name)
    }
  }, [name, onNameResolved])
}
