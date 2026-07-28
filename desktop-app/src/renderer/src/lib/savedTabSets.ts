import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import type { SavedTabSet } from '../../../main/backend/savedTabSets'
import type { CaseWorkspaceTab } from '@/lib/caseWorkspaceContext'

export type { SavedTabSet }

interface SaveTabSetInput {
  id?: string
  name: string
  tabs: CaseWorkspaceTab[]
}

export function useSavedTabSets(profileId: string | null): {
  items: SavedTabSet[]
  isLoading: boolean
  save: (input: SaveTabSetInput) => Promise<SavedTabSet>
  remove: (id: string) => Promise<void>
} {
  const queryClient = useQueryClient()
  const queryKey = ['savedTabSets', profileId]

  const { data, isLoading } = useQuery({
    queryKey,
    queryFn: () => window.api.savedTabSets.list(profileId as string) as Promise<SavedTabSet[]>,
    enabled: profileId != null
  })

  const saveMutation = useMutation({
    mutationFn: (input: SaveTabSetInput) => {
      if (!profileId) throw new Error('No active profile')
      return window.api.savedTabSets.save({ ...input, profileId }) as Promise<SavedTabSet>
    },
    onSuccess: () => queryClient.invalidateQueries({ queryKey })
  })

  const removeMutation = useMutation({
    mutationFn: (id: string) => window.api.savedTabSets.remove(id) as Promise<void>,
    onSuccess: () => queryClient.invalidateQueries({ queryKey })
  })

  return {
    items: data ?? [],
    isLoading,
    save: saveMutation.mutateAsync,
    remove: removeMutation.mutateAsync
  }
}
