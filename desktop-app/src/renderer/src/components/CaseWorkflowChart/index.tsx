import { useMemo } from 'react'
import { odooRead, odooSearchRead, OneToMany } from '@/lib/odoo-api'
import { useQuery } from '@tanstack/react-query'
import WorkflowFlowChart from '../WorkflowFlowChart'

type CaseHistory = {
  id: number
  active_phase_id: OneToMany
  phase_result_id: OneToMany
  phase_id: OneToMany
  error_message?: string
  date: string
}

export default function CaseWorkflowChart({
  workflowId,
  caseId,
  activePhaseId,
  isCaseDone
}: {
  workflowId: number
  caseId: number
  activePhaseId?: number
  isCaseDone: boolean
}) {
  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: workflowFields } = useQuery<{ id: number; triplet_phase_id: OneToMany }>({
    queryKey: ['symple.workflow', workflowId, 'for-workflow-chart'],
    queryFn: () =>
      odooRead('symple.workflow', [workflowId], ['triplet_phase_id']).then((res) => res[0])
  })

  const { data: caseHistory } = useQuery<CaseHistory[]>({
    queryKey: ['symple.triplet.phase.history', caseId],
    refetchInterval: isCaseDone ? undefined : 3 * 1000,
    enabled: !!caseId,
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase.history',
        [['ticket_id', '=', caseId]],
        ['active_phase_id', 'phase_result_id', 'error_message', 'date', 'phase_id'],
        0,
        undefined,
        'id desc'
      )
  })

  const [crossedPhases, crossedResults] = useMemo(() => {
    const crossedPhases = new Set<number>()
    const crossedResults = new Set<number>()

    if (!caseHistory) {
      return [crossedResults, crossedResults]
    }

    caseHistory.forEach((entry) => {
      if (entry?.phase_id?.[0]) {
        crossedPhases.add(entry.phase_id[0])
      }

      if (entry.phase_result_id?.[0]) {
        crossedResults.add(entry.phase_result_id[0])
      }
    })

    return [crossedPhases, crossedResults]
  }, [caseHistory])

  return (
    <WorkflowFlowChart
      workflowId={workflowId}
      crossedPhases={crossedPhases}
      crossedResults={crossedResults}
      activePhaseId={activePhaseId}
      startPhaseId={workflowFields?.triplet_phase_id?.[0]}
    />
  )
}
