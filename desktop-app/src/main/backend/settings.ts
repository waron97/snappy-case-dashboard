import { app, safeStorage } from 'electron'
import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'

export interface Settings {
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

const EMPTY_SETTINGS: Settings = {
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

let cache: Settings | null = null

export function getSettings(): Settings {
  if (cache) {
    return cache
  }

  const path = settingsPath()
  if (!existsSync(path)) {
    cache = { ...EMPTY_SETTINGS }
    return cache
  }

  const buffer = readFileSync(path)
  const json = safeStorage.isEncryptionAvailable()
    ? safeStorage.decryptString(buffer)
    : buffer.toString('utf-8')
  cache = { ...EMPTY_SETTINGS, ...(JSON.parse(json) as Partial<Settings>) }
  return cache
}

export function saveSettings(settings: Settings): void {
  cache = settings
  const json = JSON.stringify(settings)

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

export function isConfigured(): boolean {
  const { odooUid, odooApiKey } = getSettings()
  return Boolean(odooUid && odooApiKey)
}
