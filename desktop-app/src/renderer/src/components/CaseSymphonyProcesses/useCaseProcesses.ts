import { useQuery, type UseQueryResult } from '@tanstack/react-query'
import { odooRead, odooSearchRead } from '@/lib/odoo-api'

export type CaseProcessOrigin = 'current' | 'history' | 'wizard'

export type CaseSymphonyProcess = {
  /** A Symphony id — may be a request id OR a process-instance id. */
  id: string
  origin: CaseProcessOrigin
  processName: string | null
  wizardStatus: string | null
  wizardStateCode: string | null
  cancelReason: string | null
  /** Odoo row id, for stable ordering (higher = written later). */
  sortKey: number
}

const str = (value: string | false | null | undefined): string | null =>
  typeof value === 'string' && value.length > 0 ? value : null

/** A model that isn't installed must degrade to "no rows", not to an error —
 *  which modules are present varies by environment. */
function isMissingModel(err: unknown): boolean {
  return /doesn'?t exist|does not exist/i.test(err instanceof Error ? err.message : String(err))
}

async function optional<T>(promise: Promise<T[]>): Promise<T[]> {
  try {
    return await promise
  } catch (err) {
    if (isMissingModel(err)) {
      return []
    }
    throw err
  }
}

/**
 * The case's CURRENT long-running-process id.
 *
 * `helpdesk.ticket.symphonie_process` ("Symphonie Long Running Process ID").
 */
async function fetchCurrent(caseId: number): Promise<CaseSymphonyProcess[]> {
  const rows: { symphonie_process: string | false }[] = await odooRead(
    'helpdesk.ticket',
    [caseId],
    ['symphonie_process']
  )
  const id = str(rows[0]?.symphonie_process)
  return id
    ? [
        {
          id,
          origin: 'current',
          processName: null,
          wizardStatus: null,
          wizardStateCode: null,
          cancelReason: null,
          sortKey: Number.MAX_SAFE_INTEGER
        }
      ]
    : []
}

/**
 * Every value `symphonie_process` has ever held.
 *
 * `helpdesk.ticket.write()` appends a `symphony.case.id` row on every write of
 * that field, so this model is the case's process history — the previous ids are
 * not lost when the field is overwritten.
 */
async function fetchHistory(caseId: number): Promise<CaseSymphonyProcess[]> {
  const rows: { id: number; symphony_process_id: string | false }[] = await odooSearchRead(
    'symphony.case.id',
    [['case_id', '=', caseId]],
    ['id', 'symphony_process_id'],
    0,
    200,
    'id DESC'
  )
  return rows
    .filter((r) => str(r.symphony_process_id))
    .map((r) => ({
      id: str(r.symphony_process_id) as string,
      origin: 'history' as const,
      processName: null,
      wizardStatus: null,
      wizardStateCode: null,
      cancelReason: null,
      sortKey: r.id
    }))
}

/**
 * Ids recorded when a wizard completes.
 *
 * `set_instance_key(instance_key, process_name, state_code, status)` on the
 * `symple.pb.instance.key.mixin` stores the `instancekey` returned by the b2w
 * wizard-dispatch endpoint, together with the process name and the wizard's
 * outcome — the only source here that carries more than a bare id.
 *
 * `res_model` is a stored related char, so it is filtered directly rather than
 * traversing `res_model_id`.
 */
async function fetchWizardKeys(caseId: number): Promise<CaseSymphonyProcess[]> {
  const rows: {
    id: number
    instance_key: string | false
    process_name: string | false
    wizard_result_state_code: string | false
    wizard_result_status: string | false
    wizard_cancel_reason: string | false
  }[] = await odooSearchRead(
    'symple.pb.instance.key',
    [
      ['res_id', '=', caseId],
      ['res_model', '=', 'helpdesk.ticket']
    ],
    [
      'id',
      'instance_key',
      'process_name',
      'wizard_result_state_code',
      'wizard_result_status',
      'wizard_cancel_reason'
    ],
    0,
    200,
    'id DESC'
  )
  return rows
    .filter((r) => str(r.instance_key))
    .map((r) => ({
      id: str(r.instance_key) as string,
      origin: 'wizard' as const,
      processName: str(r.process_name),
      wizardStatus: str(r.wizard_result_status),
      wizardStateCode: str(r.wizard_result_state_code),
      cancelReason: str(r.wizard_cancel_reason),
      sortKey: r.id
    }))
}

/**
 * Every Symphony id Odoo associates with a case, from all three places it keeps
 * them, merged and de-duplicated.
 *
 * Sources are fetched independently so one missing model cannot empty the tab.
 * On a duplicate id the richer record wins: wizard (has a process name and
 * outcome) > current > history.
 */
export function useCaseSymphonyProcesses(
  caseId: number
): UseQueryResult<CaseSymphonyProcess[], Error> {
  return useQuery({
    queryKey: ['case', caseId, 'symphony-processes'],
    queryFn: async () => {
      const [wizard, current, history] = await Promise.all([
        optional(fetchWizardKeys(caseId)),
        optional(fetchCurrent(caseId)),
        optional(fetchHistory(caseId))
      ])
      const byId = new Map<string, CaseSymphonyProcess>()
      // Insertion order encodes the precedence above.
      for (const row of [...wizard, ...current, ...history]) {
        const existing = byId.get(row.id)
        if (!existing) {
          byId.set(row.id, row)
        } else if (existing.origin === 'history' && row.origin !== 'history') {
          byId.set(row.id, row)
        }
      }
      return [...byId.values()].sort((a, b) => b.sortKey - a.sortKey)
    },
    retry: false
  })
}
