import { app, safeStorage } from 'electron'
import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'

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
    const buffer = readFileSync(path)
    const json = safeStorage.isEncryptionAvailable()
      ? safeStorage.decryptString(buffer)
      : buffer.toString('utf-8')
    cache = JSON.parse(json)
  } catch {
    cache = {}
  }
  return cache!
}

function persist(store: UiPrefsStore): void {
  cache = store
  const json = JSON.stringify(store)

  const buffer = safeStorage.isEncryptionAvailable()
    ? safeStorage.encryptString(json)
    : Buffer.from(json, 'utf-8')
  writeFileSync(uiPrefsPath(), buffer)
}

export function getUiPrefs(): UiPrefsStore {
  return load()
}

export function setUiPref(key: string, value: unknown): void {
  const store = load()
  persist({ ...store, [key]: value })
}
