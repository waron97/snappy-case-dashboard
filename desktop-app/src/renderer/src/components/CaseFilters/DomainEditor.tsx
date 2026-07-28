import { json } from '@codemirror/lang-json'
import { vim, Vim } from '@replit/codemirror-vim'
import { vscodeDark } from '@uiw/codemirror-theme-vscode'
import ReactCodeMirror from '@uiw/react-codemirror'
import { useEffect } from 'react'

type Props = {
  value: string
  onChange: (v: string) => void
  onWriteCommand: () => void
}

export default function DomainEditor(props: Props) {
  const { value, onChange, onWriteCommand } = props

  useEffect(() => {
    Vim.defineEx('write', 'w', () => onWriteCommand())
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <ReactCodeMirror
      value={value}
      theme={vscodeDark}
      extensions={[json(), vim()]}
      onChange={onChange}
      basicSetup={{ lineNumbers: true }}
      minHeight="120px"
    />
  )
}
