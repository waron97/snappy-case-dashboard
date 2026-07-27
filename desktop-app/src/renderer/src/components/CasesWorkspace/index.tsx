import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { IconX } from '@tabler/icons-react'
import { ActionIcon, Box, Button, Container, Group, Tabs } from '@mantine/core'
import CaseList from '@/routes/CaseList'
import CaseDetail from '@/routes/CaseDetail'
import { CaseTab, useCaseTabs } from '@/lib/useCaseTabs'

function TabLabel({
  label,
  onRename
}: {
  label: string
  onRename: (value: string) => void
}): React.JSX.Element {
  const [editing, setEditing] = useState(false)
  const [value, setValue] = useState(label)

  if (editing) {
    return (
      <input
        autoFocus
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onClick={(e) => e.stopPropagation()}
        onMouseDown={(e) => e.stopPropagation()}
        onKeyDown={(e) => {
          e.stopPropagation()
          if (e.key === 'Enter') {
            onRename(value)
            setEditing(false)
          } else if (e.key === 'Escape') {
            setValue(label)
            setEditing(false)
          }
        }}
        onBlur={() => {
          onRename(value)
          setEditing(false)
        }}
        style={{
          background: 'transparent',
          border: 'none',
          borderBottom: '1px solid currentColor',
          font: 'inherit',
          color: 'inherit',
          width: `${Math.max(value.length, 4)}ch`,
          outline: 'none'
        }}
      />
    )
  }

  return (
    <span
      onDoubleClick={(e) => {
        e.stopPropagation()
        setValue(label)
        setEditing(true)
      }}
    >
      {label}
    </span>
  )
}

export default function CasesWorkspace(): React.JSX.Element {
  const { tabs, activeId, setActive, closeCase, closeAll, setLabel, renameTab } = useCaseTabs()
  const navigate = useNavigate()

  function handleChange(value: string | null): void {
    if (!value) return
    const id = value === 'list' ? 'list' : parseInt(value, 10)
    setActive(id)
    navigate(id === 'list' ? '/' : `/helpdesk.ticket/${id}`)
  }

  const caseTabs = tabs.filter((t): t is CaseTab & { id: number } => t.id !== 'list')

  return (
    <Tabs value={String(activeId)} onChange={handleChange} keepMounted>
      <Box style={{ borderBottom: '1px solid var(--mantine-color-gray-8)' }}>
        <Container size="xl">
          <Group justify="space-between" wrap="nowrap" gap="sm">
            <Tabs.List style={{ flex: 1, minWidth: 0 }}>
              <Tabs.Tab value="list">Cases</Tabs.Tab>
              {caseTabs.map((tab) => (
                <Tabs.Tab
                  key={tab.id}
                  value={String(tab.id)}
                  rightSection={
                    <ActionIcon
                      size="xs"
                      variant="subtle"
                      component="span"
                      onClick={(e) => {
                        e.stopPropagation()
                        closeCase(tab.id)
                      }}
                    >
                      <IconX size={12} />
                    </ActionIcon>
                  }
                >
                  <TabLabel label={tab.label} onRename={(value) => renameTab(tab.id, value)} />
                </Tabs.Tab>
              ))}
            </Tabs.List>
            {caseTabs.length > 0 && (
              <Button size="xs" variant="subtle" color="gray" onClick={closeAll}>
                Close all
              </Button>
            )}
          </Group>
        </Container>
      </Box>

      <Tabs.Panel value="list">
        <CaseList />
      </Tabs.Panel>
      {caseTabs.map((tab) => (
        <Tabs.Panel key={tab.id} value={String(tab.id)}>
          <CaseDetail
            id={tab.id}
            isActive={activeId === tab.id}
            onNameResolved={(name) => setLabel(tab.id, name)}
          />
        </Tabs.Panel>
      ))}
    </Tabs>
  )
}
