export type SortKey = 'name' | 'date' | 'size'

export type VariableFilter = {
  name: string
  value: string
  types: string[]
  caseSensitive: boolean
  sortKey: SortKey
}

export const EMPTY_VARIABLE_FILTER: VariableFilter = {
  name: '',
  value: '',
  types: [],
  caseSensitive: false,
  sortKey: 'name'
}
