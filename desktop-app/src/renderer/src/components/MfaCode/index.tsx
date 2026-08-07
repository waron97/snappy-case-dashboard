import { useEffect, useState } from 'react'
import { odooRead, odooWrite } from '@/lib/odoo-api'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { LoadingOverlay } from '@mantine/core'
import PythonEditor from '@/components/PythonEditor'
import UiCard from '@/components/UiCard'

type Props = {
  id: number
}

export default function MfaCode({ id }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [draft, setDraft] = useState('')
  // Which record the draft was seeded from, rather than a plain boolean: the
  // seed must happen exactly once per record (see the effect below).
  const [seededFor, setSeededFor] = useState<number | null>(null)

  const queryClient = useQueryClient()

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data, isLoading } = useQuery({
    queryKey: ['mfa', id, 'code'],
    queryFn: () => odooRead('rip.model.function.access', [id], ['code'])
  })

  // -------------------------------------
  // Effects
  // -------------------------------------

  // Seeds the editor once per record, NOT on every `data` identity. `data` is an
  // array, so it is a new object after every refetch — and the query client is a
  // bare `new QueryClient()` (refetchOnWindowFocus: true, staleTime: 0), so
  // syncing on `data` meant alt-tabbing away and back silently overwrote the
  // user's unsaved code. This panel now stays mounted for the whole session, so
  // that would have fired for every open MFA tab on every window focus.
  useEffect(() => {
    if (seededFor === id) return
    const code = data?.[0]?.code
    if (code === undefined) return
    setDraft(code)
    setSeededFor(id)
  }, [data, id, seededFor])

  // -------------------------------------
  // Functions
  // -------------------------------------

  // Errors deliberately propagate: PythonEditor's save path reports them (and
  // reports success), so catching here would toast twice — once for the failure,
  // once for the "Saved" this swallowed rejection would look like.
  async function handleSave() {
    await odooWrite('rip.model.function.access', [id], { code: draft })
    queryClient.invalidateQueries({ queryKey: ['mfa', id, 'code'] })
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const savedCode: string = data?.[0]?.code ?? ''
  const initialized = seededFor === id
  const isDirty = initialized && draft !== savedCode

  // -------------------------------------

  return (
    <UiCard>
      <div style={{ position: 'relative', minHeight: 200 }}>
        <LoadingOverlay visible={isLoading} />
        {initialized && (
          <PythonEditor
            value={draft}
            onChange={setDraft}
            onSave={isDirty ? handleSave : undefined}
            maxHeight="800px"
          />
        )}
      </div>
    </UiCard>
  )
}
