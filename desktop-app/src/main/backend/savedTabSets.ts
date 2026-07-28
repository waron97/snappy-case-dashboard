import { app, safeStorage } from 'electron'
import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'
import { randomUUID } from 'crypto'

export interface SavedTabSet {
  id: string
  profileId: string
  name: string
  tabs: unknown[]
  createdAt: string
  updatedAt: string
}

interface SavedTabSetsStore {
  items: SavedTabSet[]
}

function savedTabSetsPath(): string {
  return join(app.getPath('userData'), 'saved-tab-sets.enc')
}

let cache: SavedTabSetsStore | null = null

function load(): SavedTabSetsStore {
  if (cache) {
    return cache
  }

  const path = savedTabSetsPath()
  if (!existsSync(path)) {
    cache = { items: [] }
    return cache
  }

  const buffer = readFileSync(path)
  const json = safeStorage.isEncryptionAvailable()
    ? safeStorage.decryptString(buffer)
    : buffer.toString('utf-8')
  cache = JSON.parse(json)
  return cache as SavedTabSetsStore
}

function persist(store: SavedTabSetsStore): void {
  cache = store
  const json = JSON.stringify(store)

  if (!safeStorage.isEncryptionAvailable()) {
    console.warn(
      'safeStorage encryption is unavailable on this system (no OS keychain provider found) — saved tab sets will be saved unencrypted.'
    )
  }

  const buffer = safeStorage.isEncryptionAvailable()
    ? safeStorage.encryptString(json)
    : Buffer.from(json, 'utf-8')
  writeFileSync(savedTabSetsPath(), buffer)
}

export function listSavedTabSets(profileId: string): SavedTabSet[] {
  return load().items.filter((i) => i.profileId === profileId)
}

export function saveSavedTabSet(input: {
  id?: string
  profileId: string
  name: string
  tabs: unknown[]
}): SavedTabSet {
  const store = load()
  const now = new Date().toISOString()
  const existing = input.id ? store.items.find((i) => i.id === input.id) : undefined
  const id = existing?.id ?? input.id ?? randomUUID()
  const saved: SavedTabSet = {
    id,
    profileId: input.profileId,
    name: input.name,
    tabs: input.tabs,
    createdAt: existing?.createdAt ?? now,
    updatedAt: now
  }
  const items = existing
    ? store.items.map((i) => (i.id === id ? saved : i))
    : [...store.items, saved]
  persist({ items })
  return saved
}

export function removeSavedTabSet(id: string): void {
  const store = load()
  persist({ items: store.items.filter((i) => i.id !== id) })
}
