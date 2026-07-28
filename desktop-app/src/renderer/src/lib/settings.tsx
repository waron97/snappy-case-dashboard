import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react'
import type { Profile, ProfileCredentials, SettingsStore } from '../../../main/backend/settings'
import { setUiPref } from '@/lib/uiPrefs'

export type { Profile, ProfileCredentials, SettingsStore }

interface SettingsContextValue {
  profiles: Profile[]
  activeProfile: Profile | null
  isConfigured: boolean
  loading: boolean
  saveProfile: (profile: Profile) => Promise<Profile>
  deleteProfile: (id: string) => Promise<void>
  setActiveProfile: (id: string) => Promise<void>
  refresh: () => Promise<void>
}

const SettingsContext = createContext<SettingsContextValue | null>(null)

export function SettingsProvider({ children }: { children: ReactNode }): React.JSX.Element {
  const [store, setStore] = useState<SettingsStore | null>(null)
  const [loading, setLoading] = useState(true)

  const refresh = useCallback(async (): Promise<void> => {
    const next = (await window.api.settings.getStore()) as SettingsStore
    setStore(next)
  }, [])

  useEffect(() => {
    let cancelled = false
    window.api.settings.getStore().then((next) => {
      if (!cancelled) {
        setStore(next as SettingsStore)
        setLoading(false)
      }
    })
    return (): void => {
      cancelled = true
    }
  }, [])

  const saveProfile = useCallback(
    async (profile: Profile): Promise<Profile> => {
      const saved = (await window.api.settings.saveProfile(profile)) as Profile
      await refresh()
      return saved
    },
    [refresh]
  )

  const deleteProfile = useCallback(
    async (id: string): Promise<void> => {
      await window.api.settings.deleteProfile(id)
      await refresh()
    },
    [refresh]
  )

  const setActiveProfile = useCallback(async (id: string): Promise<void> => {
    await window.api.settings.setActiveProfile(id)
    // Full reload guarantees no stale React Query cache, cached Keycloak
    // token, or open case tabs referencing the previous environment.
    await setUiPref('caseWorkspaceOpenTabs', [])
    window.location.reload()
  }, [])

  const profiles = store?.profiles ?? []
  const activeProfile = profiles.find((p) => p.id === store?.activeProfileId) ?? null
  const isConfigured = Boolean(activeProfile?.odooUid && activeProfile?.odooApiKey)

  return (
    <SettingsContext.Provider
      value={{
        profiles,
        activeProfile,
        isConfigured,
        loading,
        saveProfile,
        deleteProfile,
        setActiveProfile,
        refresh
      }}
    >
      {children}
    </SettingsContext.Provider>
  )
}

export function useSettings(): SettingsContextValue {
  const ctx = useContext(SettingsContext)
  if (!ctx) {
    throw new Error('useSettings must be used within a SettingsProvider')
  }
  return ctx
}
