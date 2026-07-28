import type { MantineColorSchemeManager } from '@mantine/core'
import { scheduleIdleTask } from './idleTask'

const STORAGE_KEY = 'mantine-color-scheme-value'

function isValidScheme(value: string | null): value is 'dark' | 'light' | 'auto' {
  return value === 'dark' || value === 'light' || value === 'auto'
}

/**
 * Chromium's localStorage under a file:// origin (required for HashRouter)
 * takes ~3.5s to respond on its first touch in a session. Mantine's built-in
 * localStorageColorSchemeManager calls localStorage.getItem() synchronously
 * during MantineProvider's first render, blocking the entire app's initial
 * paint on it. This manager returns the default immediately and reads the
 * persisted value in the background instead.
 */
export function deferredLocalStorageColorSchemeManager(): MantineColorSchemeManager {
  let handleStorageEvent: ((event: StorageEvent) => void) | undefined
  let cancelIdleRead: (() => void) | undefined

  return {
    get: (defaultValue) => defaultValue,
    set: (value) => {
      try {
        window.localStorage.setItem(STORAGE_KEY, value)
      } catch (error) {
        console.warn('[colorSchemeManager] unable to save color scheme', error)
      }
    },
    subscribe: (onUpdate) => {
      // The first localStorage touch this session is the slow one (see
      // above) — schedule it for idle time so it doesn't compete with
      // whatever the user is doing right after launch.
      cancelIdleRead = scheduleIdleTask(() => {
        try {
          const stored = window.localStorage.getItem(STORAGE_KEY)
          if (isValidScheme(stored)) onUpdate(stored)
        } catch {
          // ignore — keep the default
        }
      })

      handleStorageEvent = (event) => {
        if (event.storageArea === window.localStorage && event.key === STORAGE_KEY) {
          if (isValidScheme(event.newValue)) onUpdate(event.newValue)
        }
      }
      window.addEventListener('storage', handleStorageEvent)
    },
    unsubscribe: () => {
      cancelIdleRead?.()
      if (handleStorageEvent) window.removeEventListener('storage', handleStorageEvent)
    },
    clear: () => {
      try {
        window.localStorage.removeItem(STORAGE_KEY)
      } catch {
        // ignore
      }
    }
  }
}
