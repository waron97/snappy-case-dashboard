import { lazy, Suspense, useEffect, useRef, useState } from 'react'
import { IconChevronDown, IconTrash } from '@tabler/icons-react'
import {
  ActionIcon,
  Button,
  Center,
  Checkbox,
  Group,
  Loader,
  Menu,
  Modal,
  Stack,
  TagsInput,
  TextInput
} from '@mantine/core'
import { DateInput } from '@mantine/dates'
import { useSavedDomains } from '@/lib/savedDomains'
import { useTabIsActive } from '@/lib/tabActive'

const DomainEditor = lazy(() => import('./DomainEditor'))

type Props = {
  value: { [key: string]: any }
  onChange: (v: { [key: string]: any }) => void
  toDomain?: (filters: { [key: string]: any }) => any[]
}

export default function CaseFilters(props: Props) {
  const { value: filters, onChange: setFilters, toDomain } = props

  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [draft, setDraft] = useState<string>(filters.customDomain ?? '[]')
  const [selectedId, setSelectedId] = useState<string | null>(null)
  const [saveModalOpen, setSaveModalOpen] = useState(false)
  const [saveName, setSaveName] = useState('')

  const tabIsActive = useTabIsActive()

  const { items: savedDomains, save: saveDomain, remove: removeDomain } = useSavedDomains()

  const draftRef = useRef(draft)
  const filtersRef = useRef(filters)
  const setFiltersRef = useRef(setFilters)
  filtersRef.current = filters
  setFiltersRef.current = setFilters

  // -------------------------------------
  // Effects
  // -------------------------------------

  useEffect(() => {
    draftRef.current = draft
  }, [draft])

  // -------------------------------------
  // Functions
  // -------------------------------------

  function applyDraft(): void {
    setFiltersRef.current({ ...filtersRef.current, customDomain: draftRef.current })
  }

  function selectSaved(id: string, domain: string): void {
    setDraft(domain)
    setSelectedId(id)
    setFilters({ ...filters, useCustomDomain: true, customDomain: domain })
  }

  async function handleDelete(id: string, name: string): Promise<void> {
    if (!window.confirm(`Delete saved query "${name}"?`)) return
    await removeDomain(id)
    if (id === selectedId) setSelectedId(null)
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const selectedSaved = savedDomains.find((d) => d.id === selectedId) ?? null
  const isDirty = selectedSaved != null && selectedSaved.domain !== draft

  // -------------------------------------

  return (
    <Stack gap="sm">
      {filters.useCustomDomain ? (
        <Stack>
          <Group justify="space-between">
            <Menu trigger="click" position="bottom-start">
              <Menu.Target>
                <Button
                  variant="subtle"
                  color="gray"
                  size="sm"
                  rightSection={<IconChevronDown size={14} />}
                >
                  {selectedSaved ? selectedSaved.name : 'Saved queries'}
                </Button>
              </Menu.Target>
              <Menu.Dropdown>
                {savedDomains.length === 0 && <Menu.Item disabled>No saved queries yet</Menu.Item>}
                {savedDomains.map((sd) => (
                  <Menu.Item
                    key={sd.id}
                    fw={sd.id === selectedId ? 600 : undefined}
                    onClick={() => selectSaved(sd.id, sd.domain)}
                    rightSection={
                      <ActionIcon
                        variant="subtle"
                        color="red"
                        size="sm"
                        component="span"
                        onClick={(e) => {
                          e.stopPropagation()
                          handleDelete(sd.id, sd.name)
                        }}
                      >
                        <IconTrash size={14} />
                      </ActionIcon>
                    }
                  >
                    {sd.name}
                  </Menu.Item>
                ))}
              </Menu.Dropdown>
            </Menu>
            <Group gap="xs">
              {selectedSaved && isDirty && (
                <Button
                  size="compact-sm"
                  variant="light"
                  onClick={async () => {
                    await saveDomain({
                      id: selectedSaved.id,
                      name: selectedSaved.name,
                      domain: draft
                    })
                    applyDraft()
                  }}
                >
                  Update &quot;{selectedSaved.name}&quot;
                </Button>
              )}
              <Button
                size="compact-sm"
                variant="light"
                onClick={() => {
                  setSaveName(selectedSaved?.name ?? '')
                  setSaveModalOpen(true)
                }}
              >
                Save as…
              </Button>
              <Button size="compact-sm" color="green" onClick={applyDraft}>
                Apply
              </Button>
            </Group>
          </Group>
          <Suspense
            fallback={
              <Center h={120}>
                <Loader size="sm" />
              </Center>
            }
          >
            <DomainEditor value={draft} onChange={setDraft} onWriteCommand={applyDraft} />
          </Suspense>
          <Checkbox
            label="Custom domain"
            checked={filters.useCustomDomain === true}
            onChange={(e) => {
              setSelectedId(null)
              if (e.target.checked) {
                const domain = toDomain?.(filters) ?? []
                const domainStr = JSON.stringify(domain, null, 2)
                setDraft(domainStr)
                setFilters({
                  ...filters,
                  useCustomDomain: true,
                  customDomain: domainStr
                })
              } else {
                setFilters({ ...filters, useCustomDomain: false })
              }
            }}
          />
        </Stack>
      ) : (
        <>
          <Group grow>
            <TagsInput
              label="Case Name"
              value={filters.name}
              onChange={(value: string[]) => setFilters({ ...filters, name: value || [] })}
            />
            <TagsInput
              label="Workflow"
              value={filters.workflow}
              onChange={(v) => setFilters({ ...filters, workflow: v })}
            />

            <TagsInput
              label="Active phase"
              value={filters.activePhase}
              onChange={(v) => setFilters({ ...filters, activePhase: v })}
            />
          </Group>
          <Group grow>
            <TagsInput
              label="Ticket type"
              value={filters.ticketType}
              onChange={(v) => setFilters({ ...filters, ticketType: v })}
            />
            <DateInput
              label="Creati dopo il"
              value={filters.startDate}
              onChange={(v) => setFilters({ ...filters, startDate: v })}
              clearable
            />
            <DateInput
              label="Creati prima del"
              value={filters.endDate}
              onChange={(v) => setFilters({ ...filters, endDate: v })}
              clearable
            />
          </Group>
          <Group gap="sm">
            <Checkbox
              label="Mostra case chiusi"
              checked={filters.is_close === null}
              onChange={(v) =>
                setFilters({
                  ...filters,
                  is_close: v.target.checked ? null : false
                })
              }
            />
            <Checkbox
              label="Custom domain"
              checked={filters.useCustomDomain === true}
              onChange={(e) => {
                setSelectedId(null)
                if (e.target.checked) {
                  const domain = toDomain?.(filters) ?? []
                  const domainStr = JSON.stringify(domain, null, 2)
                  setDraft(domainStr)
                  setFilters({
                    ...filters,
                    useCustomDomain: true,
                    customDomain: domainStr
                  })
                } else {
                  setFilters({ ...filters, useCustomDomain: false })
                }
              }}
            />
          </Group>
        </>
      )}
      {/* Portals to document.body, so it has to be gated on tab activity or it
          floats over whichever tab the user switches to — see SearchableJsonModal. */}
      <Modal
        opened={saveModalOpen && tabIsActive}
        onClose={() => setSaveModalOpen(false)}
        title="Save domain query"
        centered
      >
        <Stack>
          <TextInput
            label="Name"
            value={saveName}
            onChange={(e) => setSaveName(e.currentTarget.value)}
            data-autofocus
          />
          <Group justify="end">
            <Button variant="subtle" onClick={() => setSaveModalOpen(false)}>
              Cancel
            </Button>
            <Button
              disabled={!saveName.trim()}
              onClick={async () => {
                const created = await saveDomain({ name: saveName, domain: draft })
                setSelectedId(created.id)
                applyDraft()
                setSaveModalOpen(false)
              }}
            >
              Save
            </Button>
          </Group>
        </Stack>
      </Modal>
    </Stack>
  )
}
