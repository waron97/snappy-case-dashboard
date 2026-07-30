import { useSymphonyProcessKeys } from '@/lib/symphonyProcessKeys'

/**
 * Renders nothing. Exists so the Symphony process-key catalog starts
 * downloading in the background at app start rather than the first time someone
 * opens the filter dropdown (the full sweep is ~58MB / ~20s).
 *
 * Mounted from App.tsx inside the `isConfigured` branch rather than triggered
 * from the main process on `whenReady`: at that point there may be no
 * configured profile or Keycloak credentials at all, which would guarantee a
 * failed 4-request burst on every first run, and main-process startup is
 * deliberately kept lean. This also means no new main-process timer — the
 * periodic refresh is react-query's `refetchInterval`.
 *
 * Failure is non-fatal and silent here: the process-key Select degrades to a
 * server-side `like` search, and the filter card surfaces the error.
 */
export default function SymphonyCatalogWarmup(): null {
  useSymphonyProcessKeys()
  return null
}
