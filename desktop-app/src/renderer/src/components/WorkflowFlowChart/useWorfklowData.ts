import { useEffect, useMemo, useState } from 'react'
import { odooSearchRead, OneToMany } from '@/lib/odoo-api'
import { useQuery } from '@tanstack/react-query'
import { ChartPhase, ChartResult } from './layout'

type RawPhase = Omit<ChartPhase, 'stage_code'> & { helpdesk_stage_id: OneToMany }

export default function useWorkflowData(workflowId: number, startPhaseId?: number) {
  // -------------------------------------
  // State
  // -------------------------------------

  const [phases, setPhases] = useState<RawPhase[]>([])
  const [results, setResults] = useState<ChartResult[]>([])

  const [phaseIdsToFill, setPhaseIdsToFill] = useState<number[]>([])
  const [resultIdsToFill, setResultIdsToFill] = useState<number[]>([])

  const [isDone, setIsDone] = useState(false)

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data: initialPhases } = useQuery<RawPhase[]>({
    enabled: !!workflowId && !isDone,
    queryKey: ['symple.triplet.phase', { workflowId }, 'for-workflow-chart'],
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase',
        [['workflow_id', '=', workflowId]],
        ['name', 'allowed_phase_result_ids', 'helpdesk_stage_id']
      )
  })

  const { data: initialResults } = useQuery<ChartResult[]>({
    enabled: !!workflowId && !isDone,
    queryKey: ['symple.triplet.phase.result', { workflowId }, 'for-workflow-chart'],
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase.result',
        [['workflow_id', '=', workflowId]],
        ['name', 'starting_phase_ids', 'next_phase_id']
      )
  })

  const { data: complementPhases } = useQuery<RawPhase[]>({
    enabled: !!workflowId && phaseIdsToFill.length > 0 && !isDone,
    queryKey: ['symple.triplet.phase', { ids: phaseIdsToFill }, 'for-workflow-chart'],
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase',
        [['id', 'in', phaseIdsToFill]],
        ['name', 'allowed_phase_result_ids', 'helpdesk_stage_id']
      )
  })

  const { data: complementResults } = useQuery<ChartResult[]>({
    enabled: !!workflowId && resultIdsToFill.length > 0 && !isDone,
    queryKey: ['symple.triplet.phase.result', { ids: resultIdsToFill }, 'for-workflow-chart'],
    queryFn: () =>
      odooSearchRead(
        'symple.triplet.phase.result',
        [['id', 'in', resultIdsToFill]],
        ['name', 'starting_phase_ids', 'next_phase_id']
      )
  })

  // -------------------------------------
  // Methods
  // -------------------------------------

  function findPhase(id: number): RawPhase | null {
    return (
      initialPhases?.find((p) => p.id === id) || complementPhases?.find((p) => p.id === id) || null
    )
  }

  function findResult(id: number): ChartResult | null {
    return (
      initialResults?.find((p) => p.id === id) ||
      complementResults?.find((p) => p.id === id) ||
      null
    )
  }

  function traverse(
    startId: number,
    phases: RawPhase[] = [],
    results: ChartResult[] = []
  ): [RawPhase[], ChartResult[]] {
    const phase = findPhase(startId)
    if (!phase) {
      throw new MissingPhaseError(startId)
    }

    let newPhases = [...phases]
    let newResults = [...results]

    newPhases.push(phase)

    const resultIds = phase.allowed_phase_result_ids

    for (const resultId of resultIds) {
      if (newResults.some((r) => r.id === resultId)) {
        continue
      }

      const result = findResult(resultId)

      if (!result) {
        throw new MissingResultError(resultId)
      }

      newResults.push(result)
      const nextPhaseId = result.next_phase_id?.[0]
      if (nextPhaseId && !newPhases.some((p) => p.id === nextPhaseId)) {
        ;[newPhases, newResults] = traverse(nextPhaseId, newPhases, newResults)
      }
    }

    return [newPhases, newResults]
  }

  // -------------------------------------
  // Effects
  // -------------------------------------

  useEffect(() => {
    if (isDone) {
      return
    }

    if (!initialPhases || !initialResults || !startPhaseId) {
      return
    }

    try {
      const [partialPhases, partialResults] = traverse(startPhaseId)
      setPhases(partialPhases)
      setResults(partialResults)
      setIsDone(true)
    } catch (err) {
      if (err instanceof MissingPhaseError) {
        setPhaseIdsToFill([...phaseIdsToFill, err.id])
      } else if (err instanceof MissingResultError) {
        setResultIdsToFill([...resultIdsToFill, err.id])
      } else {
        throw err
      }
    }
  }, [initialPhases, initialResults, complementPhases, complementResults, isDone, startPhaseId])

  // -------------------------------------
  // Stage codes (to detect happy-flow terminals)
  // -------------------------------------

  const stageIds = useMemo(() => {
    const ids = new Set<number>()
    phases.forEach((p) => {
      const stageId = p.helpdesk_stage_id?.[0]
      if (stageId) {
        ids.add(stageId)
      }
    })
    return Array.from(ids)
  }, [phases])

  const { data: stages } = useQuery<{ id: number; stage_code: string | false }[]>({
    enabled: stageIds.length > 0,
    queryKey: ['helpdesk.stage', { ids: stageIds }, 'for-workflow-chart'],
    queryFn: () => odooSearchRead('helpdesk.stage', [['id', 'in', stageIds]], ['stage_code'])
  })

  const phasesWithStageCode = useMemo<ChartPhase[]>(() => {
    const stageCodeById = new Map(stages?.map((s) => [s.id, s.stage_code]))
    return phases.map((phase) => ({
      id: phase.id,
      name: phase.name,
      allowed_phase_result_ids: phase.allowed_phase_result_ids,
      stage_code: stageCodeById.get(phase.helpdesk_stage_id?.[0])
    }))
  }, [phases, stages])

  return { phases: phasesWithStageCode, results }
}

class MissingPhaseError extends Error {
  id: number

  constructor(id: number) {
    super(`Phase not found: ${id}`)
    this.id = id
  }
}

class MissingResultError extends Error {
  id: number

  constructor(id: number) {
    super(`Phase not found: ${id}`)
    this.id = id
  }
}
