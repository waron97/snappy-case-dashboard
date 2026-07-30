import { useMutation, useQuery, useQueryClient, type UseQueryResult } from '@tanstack/react-query'
import { useEffect, useRef } from 'react'

export type {
  CreateSweepInput,
  SweepClause,
  SweepClauseMode,
  SweepCounters,
  SweepHit,
  SweepJob,
  SweepListFilter,
  SweepOptions,
  SweepPauseReason,
  SweepPredicate,
  SweepProgress,
  SweepSnapshot,
  SweepStatus,
  SweepStringMatch,
  SweepStringOp
} from '../../../main/backend/symphony/sweepTypes'

import type {
  CreateSweepInput,
  SweepHit,
  SweepJob,
  SweepListFilter,
  SweepOptions,
  SweepPredicate,
  SweepProgress,
  SweepSnapshot
} from '../../../main/backend/symphony/sweepTypes'

// Pure helpers, no electron import in that module — safe to pull into the bundle.
export {
  isClauseEmpty,
  isPredicateEmpty,
  normalizePredicate
} from '../../../main/backend/symphony/sweepTypes'

const api = (): typeof window.api.symphony.deepSearch => window.api.symphony.deepSearch

export const sweepListKey = ['symphony', 'deepSearch', 'jobs'] as const
export const sweepKey = (jobId: string): unknown[] => ['symphony', 'deepSearch', 'job', jobId]

export function useSweeps(): UseQueryResult<SweepJob[], Error> {
  return useQuery({
    queryKey: sweepListKey,
    queryFn: () => api().list() as Promise<SweepJob[]>,
    retry: false
  })
}

/**
 * Subscribes to the main-process progress push. Mount this ONCE, high in the
 * tree — it is the only place in the renderer that touches the IPC listener, so
 * every component keeps reading sweep state through react-query as usual.
 *
 * Deltas carry a monotonic `seq`. A gap means a push was dropped (the renderer
 * reloads on profile switch and under HMR, and sends to a destroyed webContents
 * vanish silently), so the snapshot is refetched rather than trusted.
 */
export function useSweepProgressBridge(): void {
  const queryClient = useQueryClient()
  const lastSeqRef = useRef(new Map<string, number>())

  useEffect(() => {
    const unsubscribe = api().onProgress((raw) => {
      const progress = raw as SweepProgress
      const previous = lastSeqRef.current.get(progress.jobId)
      lastSeqRef.current.set(progress.jobId, progress.seq)

      const key = sweepKey(progress.jobId)
      const existing = queryClient.getQueryData<SweepSnapshot>(key)
      const hasGap = previous != null && progress.seq !== previous + 1

      if (!existing || hasGap) {
        queryClient.invalidateQueries({ queryKey: key })
      } else {
        queryClient.setQueryData<SweepSnapshot>(key, {
          job: progress.job,
          hits: [...existing.hits, ...progress.newHits]
        })
      }

      // The list view only shows headers, so patch it in place rather than
      // refetching every job on every tick.
      queryClient.setQueryData<SweepJob[]>(sweepListKey, (jobs) =>
        jobs ? jobs.map((j) => (j.id === progress.jobId ? progress.job : j)) : jobs
      )
    })
    return unsubscribe
  }, [queryClient])
}

export function useSweep(jobId: string): UseQueryResult<SweepSnapshot | null, Error> {
  return useQuery({
    queryKey: sweepKey(jobId),
    queryFn: () => api().snapshot(jobId) as Promise<SweepSnapshot | null>,
    // Progress arrives by push; this is only the initial read and the resync.
    staleTime: Infinity,
    retry: false
  })
}

export type SweepActions = {
  create: (input: CreateSweepInput) => Promise<SweepJob>
  update: (args: {
    jobId: string
    name?: string
    predicate?: SweepPredicate
    /** Changing this discards the job's results — see updateSweep in the engine. */
    filter?: SweepListFilter
    options?: Partial<SweepOptions>
  }) => Promise<SweepJob>
  start: (jobId: string) => Promise<SweepJob>
  pause: (jobId: string) => Promise<SweepJob>
  remove: (jobId: string) => Promise<void>
}

export function useSweepActions(): SweepActions {
  const queryClient = useQueryClient()

  const invalidate = (jobId?: string): void => {
    queryClient.invalidateQueries({ queryKey: sweepListKey })
    if (jobId) {
      queryClient.invalidateQueries({ queryKey: sweepKey(jobId) })
    }
  }

  const create = useMutation({
    mutationFn: (input: CreateSweepInput) => api().create(input) as Promise<SweepJob>,
    onSuccess: (job) => invalidate(job.id)
  })

  const update = useMutation({
    mutationFn: ({
      jobId,
      ...patch
    }: {
      jobId: string
      name?: string
      predicate?: SweepPredicate
      filter?: SweepListFilter
      options?: Partial<SweepOptions>
    }) => api().update(jobId, patch) as Promise<SweepJob>,
    onSuccess: (job) => invalidate(job.id)
  })

  const start = useMutation({
    mutationFn: (jobId: string) => api().start(jobId) as Promise<SweepJob>,
    onSuccess: (job) => invalidate(job.id)
  })

  const pause = useMutation({
    mutationFn: (jobId: string) => api().pause(jobId) as Promise<SweepJob>,
    onSuccess: (job) => invalidate(job.id)
  })

  const remove = useMutation({
    mutationFn: (jobId: string) => api().remove(jobId),
    onSuccess: () => invalidate()
  })

  return {
    create: create.mutateAsync,
    update: update.mutateAsync,
    start: start.mutateAsync,
    pause: pause.mutateAsync,
    remove: remove.mutateAsync
  }
}

/**
 * Deliberately no percentage helper.
 *
 * The API never reports how many requests match a filter — `maximumRecordsNumber`
 * is the server's enumeration cap (a constant 10000), not a total. Any bar would
 * therefore be dividing by a number we invented, so the UI shows counts only.
 */

export type { SweepHit as DeepSearchHit }

/**
 * Order-independent identity for a request filter. JSON.stringify alone is not
 * enough: a filter built in the renderer and one replayed from disk have the
 * same fields in different orders, which would read as always-dirty.
 */
export function sweepFilterKey(filter: SweepListFilter): string {
  return JSON.stringify([
    filter.processKey,
    filter.startTimeInitStr,
    filter.startTimeEndStr,
    filter.requestId,
    filter.processId,
    filter.referenceId,
    filter.externalKey,
    [...filter.statuses].sort(),
    filter.deadJob
  ])
}
