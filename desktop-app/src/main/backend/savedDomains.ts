import { app } from 'electron'
import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'
import { randomUUID } from 'crypto'
import { decodeStore, encodeStore } from './storeCodec'

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

  cache = decodeStore(readFileSync(path), 'saved-domains.enc') as SavedDomainsStore
  return cache
}

function persist(store: SavedDomainsStore): void {
  cache = store
  writeFileSync(savedDomainsPath(), encodeStore(store, 'saved domains'))
}

export function listSavedDomains(): SavedDomainQuery[] {
  return load().items
}

export function saveSavedDomain(input: {
  id?: string
  name: string
  domain: string
}): SavedDomainQuery {
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
