import { Box, LoadingOverlay, Modal, ModalProps } from '@mantine/core'
import { KeyboardEvent, ReactNode, useCallback, useRef } from 'react'
import { JsonSearchHandle, JsonSearchModalContext } from './context'

type Props = {
  opened: boolean
  onClose: () => void
  title?: ReactNode
  loading?: boolean
  size?: ModalProps['size']
  children: ReactNode
}

// Generalized shell for every "log detail" modal that shows a SearchableJsonView.
// Owns Ctrl-F capture for whichever viewer(s) it wraps: Mantine traps focus inside an
// open Modal, so listening here (rather than on window + mouse-hover) works no matter
// what's focused when the user presses Ctrl-F.
export default function SearchableJsonModal({
  opened,
  onClose,
  title,
  loading,
  size = 'xl',
  children
}: Props) {
  const handlesRef = useRef(new Set<JsonSearchHandle>())

  const register = useCallback((handle: JsonSearchHandle): (() => void) => {
    handlesRef.current.add(handle)
    return () => handlesRef.current.delete(handle)
  }, [])

  const onKeyDownCapture = (e: KeyboardEvent): void => {
    if (!(e.ctrlKey || e.metaKey) || e.key.toLowerCase() !== 'f') return
    e.preventDefault()
    const handles = [...handlesRef.current]
    const hovered = handles.filter((h) => h.isHovered())
    ;(hovered.length ? hovered : handles).forEach((h) => h.open())
  }

  const content =
    loading === undefined ? (
      children
    ) : (
      <Box pos="relative" mih={100}>
        <LoadingOverlay visible={loading} />
        {children}
      </Box>
    )

  return (
    <Modal
      opened={opened}
      onClose={onClose}
      size={size}
      title={title}
      onKeyDownCapture={onKeyDownCapture}
    >
      <JsonSearchModalContext.Provider value={{ register }}>
        {content}
      </JsonSearchModalContext.Provider>
    </Modal>
  )
}
