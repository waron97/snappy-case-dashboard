import { createContext, useContext } from 'react'

export type JsonSearchHandle = {
  open: () => void
  isHovered: () => boolean
}

export type JsonSearchModalContextValue = {
  register: (handle: JsonSearchHandle) => () => void
}

// Provided by SearchableJsonModal, consumed by SearchableJsonView - lets Ctrl-F be
// captured at the modal level (Mantine traps focus inside it while open) instead of
// requiring the mouse to be hovering the exact JSON tree.
export const JsonSearchModalContext = createContext<JsonSearchModalContextValue | null>(null)

export function useJsonSearchModalContext(): JsonSearchModalContextValue | null {
  return useContext(JsonSearchModalContext)
}
