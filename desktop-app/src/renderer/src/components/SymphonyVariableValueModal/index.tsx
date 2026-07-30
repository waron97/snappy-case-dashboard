import { useState } from 'react'
import { Alert, Badge, Button, Code, Group, ScrollArea, Stack, Text } from '@mantine/core'
import SearchableJsonView, { SearchableJsonModal } from '@/components/SearchableJsonView'
import { parseJsonDeep } from '@/utils/json'
import { formatSymphonyTimestamp } from '@/lib/symphonyDates'
import type { SymphonyVariable } from '@/lib/symphony-api'

/**
 * react-json-view builds a DOM node per key, so handing it a megabyte-scale
 * object locks the renderer. Above this size the raw text is shown instead,
 * behind an explicit opt-in.
 */
const EAGER_RENDER_LIMIT = 250_000

const SCALAR_TYPES = new Set(['boolean', 'integer', 'long', 'double', 'short', 'date'])

type Props = {
  variable: SymphonyVariable | null
  onClose: () => void
}

export default function SymphonyVariableValueModal({
  variable,
  onClose
}: Props): React.JSX.Element {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [forceJson, setForceJson] = useState(false)
  const [showRaw, setShowRaw] = useState(false)

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const value = variable?.varValue ?? ''
  const isScalar = variable ? SCALAR_TYPES.has(variable.varType) : false
  const isHuge = value.length > EAGER_RENDER_LIMIT
  // Only parse when we're actually going to render a tree — parseJsonDeep walks
  // the whole document, which is wasted work for the raw view.
  const parsed = !isScalar && (!isHuge || forceJson) && !showRaw ? parseJsonDeep(value) : null

  function handleClose(): void {
    setForceJson(false)
    setShowRaw(false)
    onClose()
  }

  return (
    <SearchableJsonModal
      opened={variable != null}
      onClose={handleClose}
      size="90%"
      title={
        variable && (
          <Group gap="xs">
            <Text fw={600} ff="monospace">
              {variable.varName}
            </Text>
            <Badge variant="light">{variable.varType}</Badge>
            <Text size="xs" c="dimmed">
              {value.length.toLocaleString()} chars ·{' '}
              {formatSymphonyTimestamp(variable.varDate, 'D/M/YY HH:mm:ss.SSS')}
            </Text>
            {parsed?.kind === 'json' && parsed.didUnwrap && (
              <Badge color="grape" variant="light">
                nested JSON unwrapped
              </Badge>
            )}
          </Group>
        )
      }
    >
      {variable && (
        <Stack gap="sm">
          {isHuge && !forceJson && !isScalar && (
            <Alert color="yellow">
              <Group justify="space-between" wrap="nowrap">
                <Text size="sm">
                  This value is {value.length.toLocaleString()} characters. Rendering it as a JSON
                  tree may freeze the window.
                </Text>
                <Button size="xs" variant="light" onClick={() => setForceJson(true)}>
                  Render as JSON anyway
                </Button>
              </Group>
            </Alert>
          )}

          {parsed?.kind === 'json' ? (
            <>
              <Group justify="end">
                <Button size="xs" variant="subtle" color="gray" onClick={() => setShowRaw(true)}>
                  Show raw
                </Button>
              </Group>
              <SearchableJsonView src={parsed.value as object} theme="monokai" />
            </>
          ) : (
            <>
              {!isScalar && (
                <Group justify="end">
                  <Button
                    size="xs"
                    variant="subtle"
                    color="gray"
                    onClick={() => {
                      setShowRaw(false)
                      setForceJson(true)
                    }}
                  >
                    Try parsing as JSON
                  </Button>
                </Group>
              )}
              <ScrollArea.Autosize mah={600}>
                <Code block style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
                  {value}
                </Code>
              </ScrollArea.Autosize>
            </>
          )}
        </Stack>
      )}
    </SearchableJsonModal>
  )
}
