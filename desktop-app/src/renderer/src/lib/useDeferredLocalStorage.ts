import { useEffect, useState } from 'react'
import { scheduleIdleTask } from './idleTask'

/**
 * A localStorage-backed value that never blocks first render on it.
 *
 * Chromium's localStorage under a file:// origin (required for HashRouter)
 * takes ~3.5s to respond on its first touch in a session. Reading it
 * synchronously — e.g. in a useState lazy initializer — blocks that
 * component's first render, and everything above it with no Suspense
 * boundary, on that cost (this is exactly what happened in
 * MantineProvider's default color-scheme manager, and in
 * CaseTabsProvider's tab restore before both were fixed to defer their
 * reads instead — see lib/colorSchemeManager.ts and lib/caseWorkspace.tsx).
 *
 * This hook returns `defaultValue` immediately and applies the real stored
 * value, if any, once an idle-time read resolves. Writes go straight to
 * localStorage — by the time a user acts on something backed by this hook,
 * the session's one slow first touch has near-certainly already happened
 * elsewhere (or here, in the background), so writes don't need deferring.
 */
export function useDeferredLocalStorage<T>(
  key: string,
  defaultValue: T,
  options?: { serialize?: (value: T) => string; deserialize?: (raw: string) => T | undefined }
): [T, (value: T) => void] {
  const serialize = options?.serialize ?? ((value: T) => String(value))
  const deserialize = options?.deserialize ?? ((raw: string) => raw as unknown as T)
  const [value, setValueState] = useState(defaultValue)

  useEffect(() => {
    return scheduleIdleTask(() => {
      try {
        const raw = localStorage.getItem(key)
        if (raw !== null) {
          const parsed = deserialize(raw)
          if (parsed !== undefined) setValueState(parsed)
        }
      } catch {
        // ignore — keep the default
      }
    })
    // eslint-disable-next-line react-hooks/exhaustive-deps -- read-on-mount only
  }, [])

  function setValue(next: T): void {
    setValueState(next)
    try {
      localStorage.setItem(key, serialize(next))
    } catch (error) {
      console.warn(`[useDeferredLocalStorage] unable to persist "${key}"`, error)
    }
  }

  return [value, setValue]
}
