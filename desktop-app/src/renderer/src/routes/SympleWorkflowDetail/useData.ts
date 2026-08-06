import { useQuery } from '@tanstack/react-query'
import { odooRead, odooSearchRead } from '@/lib/odoo-api'
import { PhaseRecord, WorkflowRecord } from './context'

/** `enabled` guards both an unparseable id (a NaN would have read record [NaN])
 *  and a tab that has never been visited — see useVisitedGate in lib/tabActive. */
export default function useData(workflowId: number, enabled = true) {
  const canFetch = enabled && Number.isInteger(workflowId)

  const { data: workflow } = useQuery<WorkflowRecord>({
    queryKey: ['symple.workflow', workflowId],
    queryFn: () =>
      odooRead('symple.workflow', [workflowId], ['name', 'triplet_phase_id']).then((r) => r[0]),
    enabled: canFetch
  })

  const { data: phases = [] } = useQuery<PhaseRecord[]>({
    queryKey: ['symple.triplet.phase', { workflowId }],
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase',
        [['workflow_id', '=', workflowId]],
        ['name', 'set_result_automatically']
      ),
    enabled: canFetch
  })

  return { workflow, phases }
}
