import { app, safeStorage } from 'electron'
import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'
import { randomUUID } from 'crypto'

export interface ProfileCredentials {
  keycloakUrl: string
  keycloakClientId: string
  keycloakClientSecret: string
  keycloakServiceUsername: string
  keycloakServicePassword: string
  odooUrl: string
  odooDb: string
  odooUid: string
  odooApiKey: string
  b2wUrl: string
  devopsOrg: string
  devopsPat: string
}

export interface Profile extends ProfileCredentials {
  id: string
  name: string
}

export interface SettingsStore {
  profiles: Profile[]
  activeProfileId: string | null
}

const EMPTY_CREDENTIALS: ProfileCredentials = {
  keycloakUrl: '',
  keycloakClientId: '',
  keycloakClientSecret: '',
  keycloakServiceUsername: '',
  keycloakServicePassword: '',
  odooUrl: '',
  odooDb: '',
  odooUid: '',
  odooApiKey: '',
  b2wUrl: '',
  devopsOrg: '',
  devopsPat: ''
}

function settingsPath(): string {
  return join(app.getPath('userData'), 'settings.enc')
}

// Pre-profiles settings.enc was a flat ProfileCredentials object. Wrap it into
// a single "Default" profile so existing users keep their configured
// credentials without re-entering anything.
function migrate(raw: unknown): SettingsStore {
  if (raw && typeof raw === 'object' && Array.isArray((raw as SettingsStore).profiles)) {
    return raw as SettingsStore
  }
  const legacy = { ...EMPTY_CREDENTIALS, ...(raw as Partial<ProfileCredentials>) }
  const profile: Profile = { id: 'default', name: 'Default', ...legacy }
  return { profiles: [profile], activeProfileId: profile.id }
}

let cache: SettingsStore | null = null

function load(): SettingsStore {
  if (cache) {
    return cache
  }

  const path = settingsPath()
  if (!existsSync(path)) {
    cache = { profiles: [], activeProfileId: null }
    return cache
  }

  const buffer = readFileSync(path)
  const json = safeStorage.isEncryptionAvailable()
    ? safeStorage.decryptString(buffer)
    : buffer.toString('utf-8')
  const migrated = migrate(JSON.parse(json))
  cache = migrated
  persist(migrated)
  return cache
}

function persist(store: SettingsStore): void {
  cache = store
  const json = JSON.stringify(store)

  if (!safeStorage.isEncryptionAvailable()) {
    console.warn(
      'safeStorage encryption is unavailable on this system (no OS keychain provider found) — settings will be saved unencrypted.'
    )
  }

  const buffer = safeStorage.isEncryptionAvailable()
    ? safeStorage.encryptString(json)
    : Buffer.from(json, 'utf-8')
  writeFileSync(settingsPath(), buffer)
}

export function getStore(): SettingsStore {
  return load()
}

function getActiveProfile(): Profile | null {
  const { profiles, activeProfileId } = load()
  return profiles.find((p) => p.id === activeProfileId) ?? null
}

// Kept flat so keycloak.ts/odoo.ts/devops.ts (which just destructure fields)
// don't need to know profiles exist at all.
export function getSettings(): ProfileCredentials {
  return getActiveProfile() ?? EMPTY_CREDENTIALS
}

export function saveProfile(profile: Profile): Profile {
  const store = load()
  const id = profile.id || randomUUID()
  const saved: Profile = { ...profile, id }
  const index = store.profiles.findIndex((p) => p.id === id)
  const profiles =
    index === -1 ? [...store.profiles, saved] : store.profiles.map((p) => (p.id === id ? saved : p))
  const activeProfileId = store.activeProfileId ?? id
  persist({ profiles, activeProfileId })
  return saved
}

export function deleteProfile(id: string): void {
  const store = load()
  if (store.profiles.length <= 1) {
    return
  }
  const profiles = store.profiles.filter((p) => p.id !== id)
  const activeProfileId = store.activeProfileId === id ? profiles[0].id : store.activeProfileId
  persist({ profiles, activeProfileId })
}

export function setActiveProfile(id: string): void {
  const store = load()
  if (!store.profiles.some((p) => p.id === id)) {
    return
  }
  persist({ ...store, activeProfileId: id })
}

export function isConfigured(): boolean {
  const { odooUid, odooApiKey } = getSettings()
  return Boolean(odooUid && odooApiKey)
}
