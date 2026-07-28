import { useEffect, useMemo, useRef, useState } from 'react'
import { python } from '@codemirror/lang-python'
import { indentUnit } from '@codemirror/language'
import { Vim, vim } from '@replit/codemirror-vim'
import { IconHelpCircle, IconKeyboard, IconWand } from '@tabler/icons-react'
import { vscodeDark } from '@uiw/codemirror-theme-vscode'
import ReactCodeMirror, { EditorState, EditorView, keymap, Prec } from '@uiw/react-codemirror'
import init, { format } from '@wasm-fmt/ruff_fmt/web'
import { ActionIcon, Button, Group, Stack, Text, Tooltip } from '@mantine/core'

const ruffReady = init()

function moveByLines(view: EditorView, delta: number): boolean {
  const { state } = view
  const sel = state.selection.main
  const line = state.doc.lineAt(sel.head)
  const col = sel.head - line.from
  const targetNum = Math.max(1, Math.min(state.doc.lines, line.number + delta))
  const targetLine = state.doc.line(targetNum)
  const newPos = Math.min(targetLine.from + col, targetLine.to)
  view.dispatch({ selection: { anchor: newPos }, scrollIntoView: true })
  return true
}

type Props = {
  value: string
  onChange?: (v: string) => void
  onSave?: () => Promise<void>
  readOnly?: boolean
  height?: string
  maxHeight?: string
}

export default function PythonEditor({
  value,
  onChange,
  onSave,
  readOnly,
  height,
  maxHeight = '600px'
}: Props) {
  const [saving, setSaving] = useState(false)
  const [vimEnabled, setVimEnabled] = useState(
    () => localStorage.getItem('pythonEditor.vimEnabled') !== 'false'
  )

  function toggleVim() {
    setVimEnabled((v) => {
      localStorage.setItem('pythonEditor.vimEnabled', String(!v))
      return !v
    })
  }

  const valueRef = useRef(value)
  const onChangeRef = useRef(onChange)

  useEffect(() => {
    valueRef.current = value
    onChangeRef.current = onChange
  }, [value, onChange])

  async function formatCode(code: string): Promise<string> {
    await ruffReady
    try {
      return format(code)
    } catch {
      return code
    }
  }

  async function handleFormat() {
    onChangeRef.current?.(await formatCode(valueRef.current))
  }

  useEffect(() => {
    // Vim.defineEx registers this ex command globally across every mounted
    // CodeMirror-vim instance, not per-editor — read/write via the `cm`
    // argument so `:f` always targets whichever editor is actually focused.
    Vim.defineEx('format', 'f', async (cm) => {
      cm.setValue(await formatCode(cm.getValue()))
    })
  }, [])

  const extensions = useMemo(() => {
    return [
      python(),
      ...(vimEnabled ? [vim()] : []),
      indentUnit.of('    '),
      EditorState.tabSize.of(4),
      Prec.highest(
        keymap.of([
          { key: 'Ctrl-d', run: (view) => moveByLines(view, 10) },
          { key: 'Ctrl-u', run: (view) => moveByLines(view, -10) }
        ])
      )
    ]
  }, [vimEnabled])

  return (
    <Stack gap="md">
      <Group justify="end">
        {onSave && (
          <Button
            size="compact-sm"
            color="green"
            loading={saving}
            onClick={async () => {
              setSaving(true)
              try {
                await onSave()
              } finally {
                setSaving(false)
              }
            }}
          >
            Save
          </Button>
        )}
        <Tooltip label={vimEnabled ? 'Disable Vim mode' : 'Enable Vim mode'}>
          <ActionIcon variant={vimEnabled ? 'filled' : 'subtle'} color="gray" onClick={toggleVim}>
            <IconKeyboard size={16} />
          </ActionIcon>
        </Tooltip>
        <Tooltip label="Format with Ruff (:f)">
          <ActionIcon variant="subtle" color="gray" onClick={handleFormat}>
            <IconWand size={16} />
          </ActionIcon>
        </Tooltip>
        <Tooltip
          label={
            <>
              <Text fw={600} mb={4}>
                Vim shortcuts
              </Text>
              <Text>:f — format</Text>
              <Text>i / Esc — insert / normal</Text>
              <Text>yy / p — copy / paste line</Text>
              <Text>dd — delete line</Text>
              <Text>Ctrl-d / Ctrl-u — jump 10 lines</Text>
            </>
          }
          multiline
          maw={220}
          withArrow
        >
          <ActionIcon variant="subtle" color="gray">
            <IconHelpCircle size={16} />
          </ActionIcon>
        </Tooltip>
      </Group>
      <ReactCodeMirror
        value={value}
        readOnly={readOnly}
        onChange={onChange}
        theme={vscodeDark}
        extensions={extensions}
        maxHeight={maxHeight}
        height={height}
        basicSetup={{
          lineNumbers: true,
          foldGutter: true,
          highlightActiveLine: true,
          dropCursor: true,
          allowMultipleSelections: true,
          indentOnInput: true
        }}
      />
    </Stack>
  )
}
