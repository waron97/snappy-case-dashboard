import { useState } from 'react'
import { IconChevronDown } from '@tabler/icons-react'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { toast } from 'react-toastify'
import { Button, Menu } from '@mantine/core'
import { odooSearchRead, odooWrite } from '@/lib/odoo-api'

type Props = {
  caseId: number
  activePhaseId: number | undefined
}

export default function PhaseResultSelector({ caseId, activePhaseId }: Props) {
  const [submitting, setSubmitting] = useState(false)

  const queryClient = useQueryClient()

  const { data: phaseResults } = useQuery<{ id: number; name: string }[]>({
    queryKey: ['phase-results', { activePhaseId }],
    enabled: !!activePhaseId,
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase.result',
        [['starting_phase_ids', 'in', [activePhaseId!]]],
        ['id', 'name']
      )
  })

  async function handleSelect(resultId: number) {
    setSubmitting(true)
    try {
      await odooWrite(
        'helpdesk.ticket',
        [caseId],
        { triplet_phase_result_id: resultId },
        { bypass_ticket_check_write_allowed: true }
      )
      queryClient.invalidateQueries({ queryKey: ['case', caseId, 'for-active-phase'] })
      queryClient.invalidateQueries({ queryKey: ['case-history', caseId] })
    } catch (err) {
      if (err instanceof Error) {
        toast(err.message)
        // eslint-disable-next-line
                console.error(err);
      } else {
        toast('Unknown error. Check browser console.')
        // eslint-disable-next-line
                console.error(err);
      }
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <Menu disabled={submitting || !activePhaseId}>
      <Menu.Target>
        <Button
          disabled={!activePhaseId}
          loading={submitting}
          rightSection={<IconChevronDown size={16} />}
        >
          Set result
        </Button>
      </Menu.Target>
      <Menu.Dropdown>
        {phaseResults?.map((result) => (
          <Menu.Item key={result.id} onClick={() => handleSelect(result.id)}>
            {result.name}
          </Menu.Item>
        ))}
      </Menu.Dropdown>
    </Menu>
  )
}
