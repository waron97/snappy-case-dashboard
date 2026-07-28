import { createContext, useContext } from 'react'
import { OneToMany } from '@/lib/odoo-api'

export type WorkflowRecord = {
  id: number
  name: string
  triplet_phase_id: OneToMany
}

export type PhaseRecord = {
  id: number
  name: string
  set_result_automatically: string | false
}

export type WorkflowContextValue = {
  // Data
  workflow: WorkflowRecord | undefined
  phases: PhaseRecord[]
  // Actions
}

export const WorkflowContext = createContext<WorkflowContextValue | null>(null)

export function useWorkflowContext(): WorkflowContextValue {
  const ctx = useContext(WorkflowContext)
  if (!ctx) {
    throw new Error('useWorkflowContext must be used inside WorkflowContext.Provider')
  }
  return ctx
}
