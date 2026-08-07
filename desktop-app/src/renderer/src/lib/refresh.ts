import { createContext, useContext, useEffect, useRef } from 'react'
import { QueryKey, useQueryClient } from '@tanstack/react-query'
import { useTabIsActive } from '@/lib/tabActive'

/**
 * A counter bumped by the tab strip's refresh button. The value is meaningless —
 * only the fact that it changed matters.
 *
 * A counter rather than a registry of callbacks because every panel is already
 * mounted and already subscribed to this context: one bump re-renders all of
 * them and each decides for itself whether it is the tab the user is looking at.
 * Nothing has to be registered, unregistered, or keyed by tab.
 */
const RefreshContext = createContext(0)

export const RefreshProvider = RefreshContext.Provider

/**
 * Runs `handler` when the refresh button is pressed *while this component's tab
 * is the visible one*.
 *
 * Scoping to the active tab is the whole point: panels stay mounted, so an
 * unscoped invalidate would refetch every open tab at once — including the ones
 * useVisitedGate deliberately kept quiet.
 *
 * Works at any depth, because useTabIsActive does: call it next to the useQuery
 * it refreshes rather than hoisting a list of keys up to the page, and a query
 * added later can bring its own refresh with it.
 */
export function useRefresh(handler: () => void): void {
  const tick = useContext(RefreshContext)
  const isActive = useTabIsActive()

  const handlerRef = useRef(handler)
  const isActiveRef = useRef(isActive)
  const seenTick = useRef(tick)

  useEffect(() => {
    handlerRef.current = handler
    isActiveRef.current = isActive
  })

  useEffect(() => {
    // Not a bump — just this component mounting. A tab opened after the button
    // has already been pressed starts at a non-zero tick, so "tick > 0" would
    // refresh it spuriously on mount; comparing against what we last saw won't.
    if (seenTick.current === tick) return
    seenTick.current = tick
    if (isActiveRef.current) {
      handlerRef.current()
    }
  }, [tick])
}

/**
 * useRefresh for the usual case: mark these query keys stale so react-query
 * refetches them. Keys match by prefix, so ['case', id] also covers
 * ['case', id, 'symphony-processes'].
 */
export function useRefreshQueries(...keys: QueryKey[]): void {
  const queryClient = useQueryClient()

  useRefresh(() => {
    for (const queryKey of keys) {
      queryClient.invalidateQueries({ queryKey })
    }
  })
}
