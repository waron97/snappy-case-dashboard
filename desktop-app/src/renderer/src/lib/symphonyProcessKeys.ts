import { useQuery, useQueryClient } from '@tanstack/react-query'
import { useCallback } from 'react'
import { useSettings } from '@/lib/settings'
import type { SymphonyProcessKey, SymphonyProcessKeyCatalog } from '@/lib/symphony-api'

const TTL_MS = 12 * 60 * 60 * 1000
const REFRESH_MS = 6 * 60 * 60 * 1000

async function listCached(profileId: string): Promise<SymphonyProcessKeyCatalog | null> {
  return window.api.symphony.processKeys.listCached(
    profileId
  ) as Promise<SymphonyProcessKeyCatalog | null>
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

  const doRefresh = useCallback(() => {
    queryClient.invalidateQueries({ queryKey: ['symphony', 'processKeys', profileId] })
  }, [queryClient, profileId])

  const keys = catalog.data?.keys ?? []

  return {
    keys,
    options: keys.map((k) => k.name),
    isCatalogReady: keys.length > 0,
    isSweeping: catalog.isFetching,
    fetchedAt: catalog.data?.fetchedAt ?? null,
    error: (catalog.error as Error | null) ?? null,
    refresh: doRefresh
  }
}
