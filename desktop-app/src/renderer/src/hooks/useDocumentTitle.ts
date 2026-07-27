import { useEffect } from 'react'
import { useSettings } from '@/lib/settings'

function titlePrefix(odooDb: string | undefined): string {
  if (odooDb === 'sorgenia-test-02') {
    return '[T02] '
  }
  if (odooDb === 'sorgenia-test-01') {
    return '[T01] '
  }
  return ''
}

export function useDocumentTitle(title?: string): void {
  const { settings } = useSettings()

  useEffect(() => {
    const prefix = titlePrefix(settings?.odooDb)
    document.title = title ? `${prefix}${title}` : `${prefix}Snappy`
  }, [title, settings?.odooDb])
}
