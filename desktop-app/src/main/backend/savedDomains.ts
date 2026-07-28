import { app, safeStorage } from 'electron'
import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'
import { randomUUID } from 'crypto'

export interface SavedDomainQuery {
  id: string
  name: string
  domain: string
  createdAt: string
  updatedAt: string
}

interface SavedDomainsStore {
  items: SavedDomainQuery[]
}

function savedDomainsPath(): string {
  return join(app.getPath('userData'), 'saved-domains.enc')
}

let cache: SavedDomainsStore | null = null

function load(): SavedDomainsStore {
  if (cache) {
    return cache
  }

  const path = savedDomainsPath()
  if (!existsSync(path)) {
    cache = { items: [] }
    return cache
  }

  const buffer = readFileSync(path)
  const json = safeStorage.isEncryptionAvailable()
    ? safeStorage.decryptString(buffer)
    : buffer.toString('utf-8')
  cache = JSON.parse(json)
  return cache as SavedDomainsStore
}

function persist(store: SavedDomainsStore): void {
  cache = store
  const json = JSON.stringify(store)

  if (!safeStorage.isEncryptionAvailable()) {
    console.warn(
      'safeStorage encryption is unavailable on this system (no OS keychain provider found) — saved domains will be saved unencrypted.'
    )
  }

  const buffer = safeStorage.isEncryptionAvailable()
    ? safeStorage.encryptString(json)
    : Buffer.from(json, 'utf-8')
  writeFileSync(savedDomainsPath(), buffer)
}

export function listSavedDomains(): SavedDomainQuery[] {
  return load().items
}

export function saveSavedDomain(input: { id?: string; name: string; domain: string }): SavedDomainQuery {
  const store = load()
  const now = new Date().toISOString()
  const existing = input.id ? store.items.find((i) => i.id === input.id) : undefined
  const id = existing?.id ?? input.id ?? randomUUID()
  const saved: SavedDomainQuery = {
    id,
    name: input.name,
    domain: input.domain,
    createdAt: existing?.createdAt ?? now,
    updatedAt: now
  }
  const items = existing
    ? store.items.map((i) => (i.id === id ? saved : i))
    : [...store.items, saved]
  persist({ items })
  return saved
}

export function removeSavedDomain(id: string): void {
  const store = load()
  persist({ items: store.items.filter((i) => i.id !== id) })
}
