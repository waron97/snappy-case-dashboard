import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { IconX } from '@tabler/icons-react'
import { ActionIcon, Box, Button, Container, Group, Tabs } from '@mantine/core'
import CaseList from '@/routes/CaseList'
import CaseDetail from '@/routes/CaseDetail'
import FullFieldConfig from '@/routes/FullFieldConfig'
import { CaseWorkspaceTab, tabKey, tabPath, useCaseTabs } from '@/lib/useCaseTabs'

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
  const { tabs, activeKey, setActive, closeTab, closeAll, setLabel, renameTab } = useCaseTabs()
  const navigate = useNavigate()

  function handleChange(key: string | null): void {
    if (!key) return
    const tab = tabs.find((t) => tabKey(t) === key)
    if (!tab) return
    setActive(key)
    navigate(tabPath(tab))
  }

  const openTabs = tabs.filter(
    (t): t is CaseWorkspaceTab & { kind: 'case' | 'field-config' } => t.kind !== 'list'
  )

  return (
    <Tabs value={activeKey} onChange={handleChange} keepMounted>
      <Box style={{ borderBottom: '1px solid var(--mantine-color-gray-8)' }}>
        <Container size="xl">
          <Group justify="space-between" wrap="nowrap" gap="sm">
            <Tabs.List style={{ flex: 1, minWidth: 0 }}>
              <Tabs.Tab value="list">Cases</Tabs.Tab>
              {openTabs.map((tab) => {
                const key = tabKey(tab)
                return (
                  <Tabs.Tab
                    key={key}
                    value={key}
                    rightSection={
                      <ActionIcon
                        size="xs"
                        variant="subtle"
                        component="span"
                        onClick={(e) => {
                          e.stopPropagation()
                          closeTab(key)
                        }}
                      >
                        <IconX size={12} />
                      </ActionIcon>
                    }
                  >
                    <TabLabel label={tab.label} onRename={(value) => renameTab(key, value)} />
                  </Tabs.Tab>
                )
              })}
            </Tabs.List>
            {openTabs.length > 0 && (
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
      {openTabs.map((tab) => {
        const key = tabKey(tab)
        return (
          <Tabs.Panel key={key} value={key}>
            {tab.kind === 'case' ? (
              <CaseDetail
                id={tab.id}
                isActive={activeKey === key}
                onNameResolved={(name) => setLabel(key, name)}
              />
            ) : (
              <FullFieldConfig
                model={tab.model}
                recordId={tab.recordId}
                isActive={activeKey === key}
                onNameResolved={(name) => setLabel(key, name)}
              />
            )}
          </Tabs.Panel>
        )
      })}
    </Tabs>
  )
}
