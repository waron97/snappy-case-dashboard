import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { useCallback } from 'react'
import { useSettings } from '@/lib/settings'
import type { SymphonyProcessKey, SymphonyProcessKeyCatalog } from '@/lib/symphony-api'

const TTL_MS = 12 * 60 * 60 * 1000
const REFRESH_MS = 6 * 60 * 60 * 1000
/** Observed keys accumulate as the user pages the request list, so re-read often. */
const OBSERVED_TTL_MS = 5 * 60 * 1000

async function listCached(profileId: string): Promise<SymphonyProcessKeyCatalog | null> {
  return window.api.symphony.processKeys.listCached(
    profileId
  ) as Promise<SymphonyProcessKeyCatalog | null>
}

async function listObserved(profileId: string): Promise<string[]> {
  return window.api.symphony.processKeys.listObserved(profileId) as Promise<string[]>
}

async function refresh(force?: boolean): Promise<SymphonyProcessKeyCatalog> {
  return window.api.symphony.processKeys.refresh(force) as Promise<SymphonyProcessKeyCatalog>
}

export async function searchProcessKeys(nameLike: string): Promise<SymphonyProcessKey[]> {
  return window.api.symphony.processKeys.search(nameLike) as Promise<SymphonyProcessKey[]>
}

export type UseSymphonyProcessKeys = {
  keys: SymphonyProcessKey[]
  options: string[]
  /**
   * Keys seen on real request rows. Kept separate from `options` so the catalog's
   * own readiness (and hence the server-side search fallback) is unaffected by
   * them — see recordObservedProcessKeys in main's symphony/catalog.ts.
   */
  observedOptions: string[]
  /** True once there is a usable list, from disk or from the network. */
  isCatalogReady: boolean
  isSweeping: boolean
  fetchedAt: string | null
  error: Error | null
  refresh: () => void
}

/**
 * The ONLY consumer of the two process-key query keys.
 *
 * react-query's `initialData` has to be synchronous, but the persisted catalog
 * lives behind async IPC — so it is read by a first query and handed to the
 * second as initialData, gated on `cached.isFetched` so it is present by the
 * time the network query first mounts. `initialDataUpdatedAt` is the important
 * half: it tells react-query the persisted copy was fetched at `fetchedAt`, so
 * a fresh copy means the 58MB sweep never runs at all, and a stale one renders
 * instantly while refetching in the background.
 *
 * Keeping this hook the single observer matters — `initialData` is only read by
 * the first observer of a query key.
 */
export function useSymphonyProcessKeys(): UseSymphonyProcessKeys {
  const { activeProfile } = useSettings()
  const profileId = activeProfile?.id ?? null
  const queryClient = useQueryClient()

  const cached = useQuery({
    queryKey: ['symphony', 'processKeys', 'cached', profileId],
    queryFn: () => listCached(profileId as string),
    enabled: profileId != null,
    staleTime: Infinity,
    retry: false
  })

  // QueryProvider is a bare `new QueryClient()`, so retry defaults to 3 — a
  // misconfigured environment would otherwise cost three 20s sweeps.
  const catalog = useQuery({
    queryKey: ['symphony', 'processKeys', profileId],
    queryFn: () => refresh(),
    enabled: profileId != null && cached.isFetched,
    initialData: cached.data ?? undefined,
    initialDataUpdatedAt: cached.data ? Date.parse(cached.data.fetchedAt) : undefined,
    staleTime: TTL_MS,
    refetchInterval: REFRESH_MS,
    refetchIntervalInBackground: false,
    retry: false
  })

  const observed = useQuery({
    queryKey: ['symphony', 'processKeys', 'observed', profileId],
    queryFn: () => listObserved(profileId as string),
    enabled: profileId != null,
    staleTime: OBSERVED_TTL_MS,
    retry: false
  })

  // Invalidating alone would re-run the queryFn above, which cannot pass `force` —
  // so within the 12h TTL a manual reload was a no-op sweep-wise. Clicking the
  // button is an explicit "fetch it again now", so force the sweep and seed the
  // result straight into the query.
  const forced = useMutation({
    mutationFn: () => refresh(true),
    onSuccess: (data) => {
      queryClient.setQueryData(['symphony', 'processKeys', profileId], data)
      queryClient.invalidateQueries({
        queryKey: ['symphony', 'processKeys', 'observed', profileId]
      })
    }
  })

  const forceRefresh = forced.mutate
  const doRefresh = useCallback(() => {
    forceRefresh()
  }, [forceRefresh])

  const keys = catalog.data?.keys ?? []

  return {
    keys,
    options: keys.map((k) => k.name),
    observedOptions: observed.data ?? [],
    isCatalogReady: keys.length > 0,
    isSweeping: catalog.isFetching || forced.isPending,
    fetchedAt: catalog.data?.fetchedAt ?? null,
    error: (catalog.error as Error | null) ?? (forced.error as Error | null),
    refresh: doRefresh
  }
}
