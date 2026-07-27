import { createContext, useContext, useEffect, useState, type ReactNode } from 'react'
import type { Settings } from '../../../main/backend/settings'

export type { Settings }

interface SettingsContextValue {
  settings: Settings | null
  isConfigured: boolean
  loading: boolean
  save: (settings: Settings) => Promise<void>
}

const SettingsContext = createContext<SettingsContextValue | null>(null)

export function SettingsProvider({ children }: { children: ReactNode }): React.JSX.Element {
  const [settings, setSettings] = useState<Settings | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let cancelled = false
    window.api.settings.get().then((s) => {
      if (!cancelled) {
        setSettings(s as Settings)
        setLoading(false)
      }
    })
    return (): void => {
      cancelled = true
    }
  }, [])

  const save = async (next: Settings): Promise<void> => {
    await window.api.settings.save(next)
    setSettings(next)
  }

  const isConfigured = Boolean(settings?.odooUid && settings?.odooApiKey)

  return (
    <SettingsContext.Provider value={{ settings, isConfigured, loading, save }}>
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
