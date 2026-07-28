import type { MantineColorSchemeManager } from '@mantine/core'
import { getUiPref, setUiPref } from './uiPrefs'

const PREF_KEY = 'mantineColorScheme'

function isValidScheme(value: unknown): value is 'dark' | 'light' | 'auto' {
  return value === 'dark' || value === 'light' || value === 'auto'
}

/**
 * Mantine's built-in localStorageColorSchemeManager calls
 * localStorage.getItem() synchronously during MantineProvider's first
 * render. Under Electron's file:// origin (required for HashRouter),
 * Chromium's localStorage takes ~3.5s to respond on its first touch in a
 * session, blocking the entire app's initial paint on it. This manager
 * returns the default immediately and reads the real, IPC-backed
 * preference (src/main/backend/uiPrefs.ts) in the background instead —
 * a plain main-process file read has none of that cost.
 */
export function deferredUiPrefColorSchemeManager(): MantineColorSchemeManager {
  return {
    get: (defaultValue) => defaultValue,
    set: (value) => setUiPref(PREF_KEY, value),
    subscribe: (onUpdate) => {
      getUiPref<unknown>(PREF_KEY, undefined).then((stored) => {
        if (isValidScheme(stored)) onUpdate(stored)
      })
    },
    unsubscribe: () => {},
    clear: () => setUiPref(PREF_KEY, undefined)
  }
}
