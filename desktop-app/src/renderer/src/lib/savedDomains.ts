import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import type { SavedDomainQuery } from '../../../main/backend/savedDomains'

export type { SavedDomainQuery }

const QUERY_KEY = ['savedDomains']

interface SaveSavedDomainInput {
  id?: string
  name: string
  domain: string
}

export function useSavedDomains(): {
  items: SavedDomainQuery[]
  isLoading: boolean
  save: (input: SaveSavedDomainInput) => Promise<SavedDomainQuery>
  remove: (id: string) => Promise<void>
} {
  const queryClient = useQueryClient()

  const { data, isLoading } = useQuery({
    queryKey: QUERY_KEY,
    queryFn: () => window.api.savedDomains.list() as Promise<SavedDomainQuery[]>
  })

  const saveMutation = useMutation({
    mutationFn: (input: SaveSavedDomainInput) =>
      window.api.savedDomains.save(input) as Promise<SavedDomainQuery>,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: QUERY_KEY })
  })

  const removeMutation = useMutation({
    mutationFn: (id: string) => window.api.savedDomains.remove(id) as Promise<void>,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: QUERY_KEY })
  })

  return {
    items: data ?? [],
    isLoading,
    save: saveMutation.mutateAsync,
    remove: removeMutation.mutateAsync
  }
}
