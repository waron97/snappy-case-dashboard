/**
 * Runs `callback` when the browser is next idle (falling back to a macrotask
 * where requestIdleCallback isn't available), and returns a function to
 * cancel it if the caller unmounts first.
 *
 * Used to defer the first localStorage touch of a session — see
 * lib/colorSchemeManager.ts for why that specific call is slow under
 * Electron's file:// origin.
 */
export function scheduleIdleTask(callback: () => void, options?: { timeout?: number }): () => void {
  if ('requestIdleCallback' in window) {
    const id = window.requestIdleCallback(callback, { timeout: options?.timeout ?? 5000 })
    return () => window.cancelIdleCallback(id)
  }
  const id = setTimeout(callback, 0)
  return () => clearTimeout(id)
}
