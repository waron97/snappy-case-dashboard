import { json } from '@codemirror/lang-json'
import { vim } from '@replit/codemirror-vim'
import { vscodeDark } from '@uiw/codemirror-theme-vscode'
import ReactCodeMirror, { EditorView } from '@uiw/react-codemirror'
import { useState } from 'react'
import { useVimWrite } from '@/lib/vimWrite'

type Props = {
  value: string
  onChange: (v: string) => void
  onWriteCommand: () => void
}

export default function DomainEditor(props: Props) {
  const { value, onChange, onWriteCommand } = props

  const [view, setView] = useState<EditorView | null>(null)

  // Registered per editor rather than via a bare Vim.defineEx: the case list is
  // permanently mounted, so a global definition here answered `:w` in the Python
  // editors too.
  useVimWrite(view, onWriteCommand)

  return (
    <ReactCodeMirror
      value={value}
      theme={vscodeDark}
      extensions={[json(), vim()]}
      onChange={onChange}
      basicSetup={{ lineNumbers: true }}
      minHeight="120px"
      onCreateEditor={setView}
    />
  )
}
