import { useState } from 'react'
import { IconChevronDown, IconTrash, IconX } from '@tabler/icons-react'
import {
  ActionIcon,
  Box,
  Button,
  Container,
  Group,
  Menu,
  Modal,
  Stack,
  Tabs,
  TextInput
} from '@mantine/core'
import CaseList from '@/routes/CaseList'
import ErrorBoundary from '@/components/ErrorBoundary'
import TabPanelContent from '@/components/CasesWorkspace/TabPanelContent'
import { CaseWorkspaceTab, OpenWorkspaceTab, tabKey, useCaseTabs } from '@/lib/useCaseTabs'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { TabActiveProvider } from '@/lib/tabActive'
import { useSettings } from '@/lib/settings'
import { useSavedTabSets } from '@/lib/savedTabSets'

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

// Local name-input state lives here rather than in CasesWorkspace so that
// typing doesn't re-render the whole tab tree (every open CaseDetail/
// FullFieldConfig is kept mounted via `keepMounted` and none are memoized).
function SaveTabSetModal({
  opened,
  initialName,
  onClose,
  onSave
}: {
  opened: boolean
  initialName: string
  onClose: () => void
  onSave: (name: string) => void | Promise<void>
}): React.JSX.Element {
  const [name, setName] = useState(initialName)

  return (
    <Modal opened={opened} onClose={onClose} title="Save tab set" centered>
      <Stack>
        <TextInput
          label="Name"
          value={name}
          onChange={(e) => setName(e.currentTarget.value)}
          data-autofocus
        />
        <Group justify="end">
          <Button variant="subtle" onClick={onClose}>
            Cancel
          </Button>
          <Button disabled={!name.trim()} onClick={() => onSave(name)}>
            Save
          </Button>
        </Group>
      </Stack>
    </Modal>
  )
}

export default function CasesWorkspace(): React.JSX.Element {
  const { tabs, activeKey, openTab, closeTab, closeAll, loadTabs, setLabel, renameTab } =
    useCaseTabs()
  const { activeProfile } = useSettings()

  // The list tab sets no title of its own, so without this the last closed tab's
  // title would linger in the window bar.
  useDocumentTitle('Cases', activeKey === 'list')
  const {
    items: savedTabSets,
    save: saveTabSet,
    remove: removeTabSet
  } = useSavedTabSets(activeProfile?.id ?? null)
  const [selectedSetId, setSelectedSetId] = useState<string | null>(null)
  const [saveModalOpen, setSaveModalOpen] = useState(false)

  function handleChange(key: string | null): void {
    if (!key) return
    const tab = tabs.find((t) => tabKey(t) === key)
    if (!tab) return
    // openTab both focuses and moves the URL; it already de-duplicates, so
    // clicking the tab you're on is a no-op rather than a history entry.
    openTab(tab)
  }

  const openTabs = tabs.filter((t): t is OpenWorkspaceTab => t.kind !== 'list')

  const selectedSet = savedTabSets.find((s) => s.id === selectedSetId) ?? null
  // Label-sensitive as well as key-sensitive, so renaming a tab surfaces
  // "Update" — and order-insensitive, so reordering doesn't.
  const tabSignature = (t: OpenWorkspaceTab): string => `${tabKey(t)}::${t.label}`
  const currentSignature = openTabs.map(tabSignature).sort().join(',')
  const savedSignature = selectedSet
    ? (selectedSet.tabs as OpenWorkspaceTab[]).map(tabSignature).sort().join(',')
    : null
  const isDirty = selectedSet != null && savedSignature !== currentSignature

  function handleLoad(id: string, savedTabs: unknown[]): void {
    setSelectedSetId(id)
    loadTabs(savedTabs as CaseWorkspaceTab[])
  }

  async function handleDeleteSet(id: string, name: string): Promise<void> {
    if (!window.confirm(`Delete saved tab set "${name}"?`)) return
    await removeTabSet(id)
    if (id === selectedSetId) setSelectedSetId(null)
  }

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
            <Group gap="xs" wrap="nowrap">
              <Menu trigger="click" position="bottom-end">
                <Menu.Target>
                  <Button
                    size="xs"
                    variant="subtle"
                    color="gray"
                    rightSection={<IconChevronDown size={14} />}
                  >
                    {selectedSet ? selectedSet.name : 'Saved tab sets'}
                  </Button>
                </Menu.Target>
                <Menu.Dropdown>
                  {savedTabSets.length === 0 && (
                    <Menu.Item disabled>No saved tab sets yet</Menu.Item>
                  )}
                  {savedTabSets.map((s) => (
                    <Menu.Item
                      key={s.id}
                      fw={s.id === selectedSetId ? 600 : undefined}
                      onClick={() => handleLoad(s.id, s.tabs)}
                      rightSection={
                        <ActionIcon
                          variant="subtle"
                          color="red"
                          size="sm"
                          component="span"
                          onClick={(e) => {
                            e.stopPropagation()
                            handleDeleteSet(s.id, s.name)
                          }}
                        >
                          <IconTrash size={14} />
                        </ActionIcon>
                      }
                    >
                      {s.name}
                    </Menu.Item>
                  ))}
                  <Menu.Divider />
                  <Menu.Item
                    disabled={openTabs.length === 0}
                    onClick={() => setSaveModalOpen(true)}
                  >
                    Save current as…
                  </Menu.Item>
                  {selectedSet && isDirty && (
                    <Menu.Item
                      onClick={async () => {
                        await saveTabSet({
                          id: selectedSet.id,
                          name: selectedSet.name,
                          tabs: openTabs
                        })
                      }}
                    >
                      Update &quot;{selectedSet.name}&quot;
                    </Menu.Item>
                  )}
                </Menu.Dropdown>
              </Menu>
              {openTabs.length > 0 && (
                <Button
                  size="xs"
                  variant="subtle"
                  color="gray"
                  onClick={() => {
                    setSelectedSetId(null)
                    closeAll()
                  }}
                >
                  Close all
                </Button>
              )}
            </Group>
          </Group>
        </Container>
      </Box>

      <SaveTabSetModal
        key={`${selectedSetId ?? 'new'}:${saveModalOpen}`}
        opened={saveModalOpen}
        initialName={selectedSet?.name ?? ''}
        onClose={() => setSaveModalOpen(false)}
        onSave={async (name) => {
          const created = await saveTabSet({ name, tabs: openTabs })
          setSelectedSetId(created.id)
          setSaveModalOpen(false)
        }}
      />

      <Tabs.Panel value="list">
        <TabActiveProvider value={activeKey === 'list'}>
          <ErrorBoundary>
            <CaseList />
          </ErrorBoundary>
        </TabActiveProvider>
      </Tabs.Panel>
      {openTabs.map((tab) => {
        const key = tabKey(tab)
        const isActive = activeKey === key
        return (
          <Tabs.Panel key={key} value={key}>
            {/* Panels stay mounted, so anything portalled out of one (Modal,
                Drawer) needs to know whether its tab is the visible one. */}
            <TabActiveProvider value={isActive}>
              <ErrorBoundary onRecover={() => closeTab(key)} recoverLabel="Close tab">
                <TabPanelContent
                  tab={tab}
                  isActive={isActive}
                  onNameResolved={(name) => setLabel(key, name)}
                />
              </ErrorBoundary>
            </TabActiveProvider>
          </Tabs.Panel>
        )
      })}
    </Tabs>
  )
}
