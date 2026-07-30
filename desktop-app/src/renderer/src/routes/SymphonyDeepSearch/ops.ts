import type { SweepStringOp } from '@/lib/symphonyDeepSearch'

/** The four match operators, all linear — see the no-regex note on SweepPredicate. */
export const OPS: { value: SweepStringOp; label: string }[] = [
  { value: 'contains', label: 'contains' },
  { value: 'equals', label: 'equals' },
  { value: 'startsWith', label: 'starts with' },
  { value: 'endsWith', label: 'ends with' }
]
