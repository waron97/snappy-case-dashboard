import { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Button, Group, Modal, Stack, Text, TextInput } from '@mantine/core'
import { useHotkeys } from '@mantine/hooks'

function parseOdooUrl(raw: string): { model: string; id: number } | null {
  try {
    const url = new URL(raw)
    const hash = url.hash.startsWith('#') ? url.hash.slice(1) : url.hash
    const params = new URLSearchParams(hash)
    const model = params.get('model')
    const idStr = params.get('id')
    if (!model || !idStr) {
      return null
    }
    const id = parseInt(idStr, 10)
    if (isNaN(id)) {
      return null
    }
    return { model, id }
  } catch {
    return null
  }
}

export default function OdooNavigateModal() {
  const navigate = useNavigate()
  const [opened, setOpened] = useState(false)
  const [url, setUrl] = useState('')
  const [error, setError] = useState<string | null>(null)
  const inputRef = useRef<HTMLInputElement>(null)

  useHotkeys([['ctrl+e', () => setOpened(true)]])

  useEffect(() => {
    if (opened) {
      const t = setTimeout(() => inputRef.current?.focus(), 50)
      return () => clearTimeout(t)
    }
    return undefined
  }, [opened])

  function handleClose() {
    setOpened(false)
    setUrl('')
    setError(null)
  }

  function handleSubmit() {
    const trimmed = url.trim()
    if (/^\d+$/.test(trimmed)) {
      handleClose()
      navigate(`/helpdesk.ticket/${trimmed}`)
      return
    }

    const parsed = parseOdooUrl(url)
    if (!parsed) {
      setError('Could not parse a model and ID from this URL.')
      return
    }
    const { model, id } = parsed
    const path =
      model === 'helpdesk.ticket' ? `/helpdesk.ticket/${id}` : `/full-field-config/${model}/${id}`
    handleClose()
    navigate(path)
  }

  return (
    <Modal opened={opened} onClose={handleClose} title="Open Odoo Record" centered>
      <Stack>
        <TextInput
          ref={inputRef}
          placeholder="https://odoo.example.com/web#id=123&model=helpdesk.ticket&view_type=form"
          value={url}
          onChange={(e) => {
            setUrl(e.currentTarget.value)
            setError(null)
          }}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              handleSubmit()
            }
          }}
          error={error}
        />
        {error && (
          <Text size="xs" c="red">
            {error}
          </Text>
        )}
        <Group justify="flex-end">
          <Button variant="default" onClick={handleClose}>
            Cancel
          </Button>
          <Button onClick={handleSubmit}>Open</Button>
        </Group>
      </Stack>
    </Modal>
  )
}
