import { app } from 'electron'
import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'
import { decodeStore, encodeStore } from './storeCodec'

// Renderer-side UI preferences (color scheme, open tabs, editor toggles,
// etc.) used to live in localStorage. Under Electron's file:// origin
// (required for HashRouter), Chromium's localStorage backend takes ~3.5s
// to respond on its first touch in a session, which either blocks
// whatever component reads it first or has to be defer-and-merge'd around.
// A plain main-process file has no such quirk and needs none of that.
export type UiPrefsStore = Record<string, unknown>

function uiPrefsPath(): string {
  return join(app.getPath('userData'), 'ui-prefs.enc')
}

let cache: UiPrefsStore | null = null

function load(): UiPrefsStore {
  if (cache) {
    return cache
  }

  const path = uiPrefsPath()
  if (!existsSync(path)) {
    cache = {}
    return cache
  }

  try {
    cache = decodeStore(readFileSync(path), 'ui-prefs.enc') as UiPrefsStore
  } catch {
    // UI prefs are re-derivable, so an unreadable file is not worth failing over.
    cache = {}
  }
  return cache!
}

function persist(store: UiPrefsStore): void {
  cache = store
  writeFileSync(uiPrefsPath(), encodeStore(store, 'UI preferences'))
}

export function getUiPrefs(): UiPrefsStore {
  return load()
}

export function setUiPref(key: string, value: unknown): void {
  const store = load()
  persist({ ...store, [key]: value })
}
