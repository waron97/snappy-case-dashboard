import { useEffect, useState } from 'react'

// Renderer UI preferences (color scheme, open tabs, editor toggles) are
// backed by a plain main-process file (src/main/backend/uiPrefs.ts) via
// IPC, not localStorage — Chromium's localStorage under Electron's
// required file:// origin takes ~3.5s to respond on its first touch in a
// session; a main-process fs read has no such quirk.

type UiPrefsStore = Record<string, unknown>

// Shared across every consumer so mounting three components that each
// want a pref doesn't fire three separate IPC round-trips.
let prefsPromise: Promise<UiPrefsStore> | null = null

function loadUiPrefs(): Promise<UiPrefsStore> {
  if (!prefsPromise) {
    prefsPromise = window.api.uiPrefs.getAll() as Promise<UiPrefsStore>
  }
  return prefsPromise
}

export async function getUiPref<T>(key: string, defaultValue: T): Promise<T> {
  const store = await loadUiPrefs()
  return key in store ? (store[key] as T) : defaultValue
}

// Returns the write's promise so callers that need it to have landed before
// doing something else (e.g. reloading the window) can await it; fire-and-
// forget callers (most toggles) can just ignore the return value.
export function setUiPref(key: string, value: unknown): Promise<void> {
  if (prefsPromise) {
    prefsPromise = prefsPromise.then((store) => ({ ...store, [key]: value }))
  }
  return window.api.uiPrefs.set(key, value)
}

/** Convenience hook for a single scalar preference. */
export function useUiPref<T>(key: string, defaultValue: T): [T, (value: T) => void] {
  const [value, setValue] = useState(defaultValue)

  useEffect(() => {
    let cancelled = false
    getUiPref(key, defaultValue).then((stored) => {
      if (!cancelled) setValue(stored)
    })
    return () => {
      cancelled = true
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- read-on-mount only, keyed by `key`
  }, [key])

  function update(next: T): void {
    setValue(next)
    setUiPref(key, next)
  }

  return [value, update]
}
