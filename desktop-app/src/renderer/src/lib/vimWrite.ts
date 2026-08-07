import { useEffect, useRef } from 'react'
import { Vim } from '@replit/codemirror-vim'
import type { EditorView } from '@uiw/react-codemirror'

type WriteHandler = () => void | Promise<void>

/**
 * `:w` for the app's CodeMirror editors.
 *
 * Vim.defineEx registers an ex command globally across every mounted
 * codemirror-vim instance, not per editor — so the editors that want `:w`
 * cannot each define their own, or whichever mounted last would answer `:w` for
 * all of them. (The domain editor did define its own, and since the case list is
 * a permanently mounted tab, it was the one that won.) Instead there is a single
 * definition here that dispatches through a registry keyed by EditorView, so
 * `:w` always runs the handler of whichever editor is actually focused.
 *
 * Same reasoning as the `:f` (format) command in components/PythonEditor, which
 * gets away with one global definition because it reads and writes through the
 * `cm` it is handed rather than through a closure.
 */
const handlers = new WeakMap<EditorView, WriteHandler>()

Vim.defineEx('write', 'w', (cm) => {
  handlers.get(cm.cm6)?.()
})

/**
 * Registers `handler` as this editor's `:w`.
 *
 * A missing handler leaves `:w` a no-op for that editor, mirroring a Save button
 * that isn't rendered because there is nothing to save.
 */
export function useVimWrite(view: EditorView | null, handler: WriteHandler | undefined): void {
  const handlerRef = useRef(handler)

  useEffect(() => {
    handlerRef.current = handler
  }, [handler])

  useEffect(() => {
    if (!view) return
    handlers.set(view, () => handlerRef.current?.())
    return () => {
      handlers.delete(view)
    }
  }, [view])
}
