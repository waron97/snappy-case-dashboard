import { useEffect, useState } from 'react'
import { odooRead, odooWrite } from '@/lib/odoo-api'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { toast } from 'react-toastify'
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
  const [initialized, setInitialized] = useState(false)

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

  useEffect(() => {
    if (data?.[0]?.code !== undefined) {
      setDraft(data[0].code)
      setInitialized(true)
    }
  }, [data])

  // -------------------------------------
  // Functions
  // -------------------------------------

  async function handleSave() {
    try {
      await odooWrite('rip.model.function.access', [id], { code: draft })
      queryClient.invalidateQueries({ queryKey: ['mfa', id, 'code'] })
    } catch (err) {
      toast(err instanceof Error ? err.message : 'Unknown error. Check browser console.')

      console.error(err)
    }
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const savedCode: string = data?.[0]?.code ?? ''
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
