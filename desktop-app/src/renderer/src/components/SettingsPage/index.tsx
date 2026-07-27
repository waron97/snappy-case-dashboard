import { useState } from 'react'
import { IconPlus, IconTrash } from '@tabler/icons-react'
import {
  ActionIcon,
  Box,
  Button,
  Container,
  Divider,
  Group,
  NavLink,
  PasswordInput,
  Stack,
  Text,
  TextInput,
  Title
} from '@mantine/core'
import { useSettings, type Profile, type ProfileCredentials } from '@/lib/settings'

const EMPTY_CREDENTIALS: ProfileCredentials = {
  keycloakUrl: '',
  keycloakClientId: '',
  keycloakClientSecret: '',
  keycloakServiceUsername: '',
  keycloakServicePassword: '',
  odooUrl: '',
  odooDb: '',
  odooUid: '',
  odooApiKey: '',
  b2wUrl: '',
  devopsOrg: '',
  devopsPat: ''
}

function newDraft(): Profile {
  return { id: '', name: 'New profile', ...EMPTY_CREDENTIALS }
}

export default function SettingsPage(): React.JSX.Element {
  const { profiles, activeProfile, saveProfile, deleteProfile, setActiveProfile } = useSettings()
  const [draft, setDraft] = useState<Profile | null>(null)
  const [selectedId, setSelectedId] = useState<string | null>(null)
  const [saving, setSaving] = useState(false)

  const selectedProfile =
    draft ?? profiles.find((p) => p.id === selectedId) ?? activeProfile ?? profiles[0] ?? null

  // Reset the edit buffer whenever the selected profile identity changes
  // (user picked a different one, a new draft started, or the save/delete
  // handlers below moved the selection) — adjusting state during render
  // instead of in an effect, since this *is* "state derived from a prop".
  const [formData, setFormData] = useState<Profile | null>(selectedProfile)
  const [syncedKey, setSyncedKey] = useState<string | null>(selectedProfile?.id ?? null)
  if ((selectedProfile?.id ?? null) !== syncedKey) {
    setSyncedKey(selectedProfile?.id ?? null)
    setFormData(selectedProfile)
  }

  function selectProfile(profile: Profile): void {
    setDraft(null)
    setSelectedId(profile.id)
  }

  function startNewProfile(): void {
    setDraft(newDraft())
  }

  function field(key: keyof ProfileCredentials): {
    value: string
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void
    disabled: boolean
  } {
    return {
      value: formData?.[key] ?? '',
      onChange: (e) => {
        const value = e.currentTarget.value
        setFormData((prev) => (prev ? { ...prev, [key]: value } : prev))
      },
      disabled: saving
    }
  }

  async function handleSave(): Promise<void> {
    if (!formData) return
    setSaving(true)
    try {
      const saved = await saveProfile(formData)
      setDraft(null)
      setSelectedId(saved.id)
    } finally {
      setSaving(false)
    }
  }

  async function handleSetActive(): Promise<void> {
    if (!formData || formData.id === activeProfile?.id) return
    if (
      !window.confirm(
        `Switch active profile to "${formData.name}"? Open case tabs will close and the app will reload.`
      )
    ) {
      return
    }
    await setActiveProfile(formData.id)
  }

  async function handleDelete(): Promise<void> {
    if (!formData || profiles.length <= 1) return
    if (!window.confirm(`Delete profile "${formData.name}"? This cannot be undone.`)) return
    await deleteProfile(formData.id)
    const remaining = profiles.filter((p) => p.id !== formData.id)
    setSelectedId(remaining[0]?.id ?? null)
  }

  const isDraft = Boolean(draft && formData?.id === draft.id)
  const isActive = !isDraft && formData?.id === activeProfile?.id

  return (
    <Container size="xl" py="md">
      <Group align="flex-start" gap="xl">
        <Stack w={220} gap="xs">
          <Title order={4}>Profiles</Title>
          {profiles.map((p) => (
            <NavLink
              key={p.id}
              label={p.name}
              description={p.id === activeProfile?.id ? 'Active' : undefined}
              active={p.id === selectedId && !isDraft}
              onClick={() => selectProfile(p)}
            />
          ))}
          {draft && <NavLink label={draft.name} description="Unsaved" active onClick={() => {}} />}
          <Button leftSection={<IconPlus size={16} />} variant="light" onClick={startNewProfile}>
            New profile
          </Button>
        </Stack>

        <Box flex={1} maw={520}>
          {formData ? (
            <Stack gap="md">
              <Group justify="space-between">
                <Title order={3}>{isDraft ? 'New Profile' : formData.name}</Title>
                {isActive && (
                  <Text c="teal" fw={600}>
                    Active
                  </Text>
                )}
              </Group>

              <TextInput
                label="Profile name"
                value={formData.name}
                onChange={(e) => {
                  const value = e.currentTarget.value
                  setFormData((prev) => (prev ? { ...prev, name: value } : prev))
                }}
                disabled={saving}
              />

              <Divider />
              <Text fw={600}>Keycloak</Text>
              <TextInput
                label="Keycloak URL"
                placeholder="https://keycloak.example.com/..."
                {...field('keycloakUrl')}
              />
              <TextInput label="Client ID" {...field('keycloakClientId')} />
              <PasswordInput label="Client Secret" {...field('keycloakClientSecret')} />
              <TextInput label="Service Username" {...field('keycloakServiceUsername')} />
              <PasswordInput label="Service Password" {...field('keycloakServicePassword')} />

              <Divider />
              <Text fw={600}>Odoo</Text>
              <TextInput
                label="Odoo URL"
                placeholder="https://odoo.example.com"
                {...field('odooUrl')}
              />
              <TextInput label="Odoo DB" {...field('odooDb')} />
              <TextInput label="Your Odoo UID" placeholder="2" {...field('odooUid')} />
              <PasswordInput label="Your Odoo API Key" {...field('odooApiKey')} />

              <Divider />
              <Text fw={600}>Bit2win</Text>
              <TextInput label="Bit2win URL" {...field('b2wUrl')} />

              <Divider />
              <Text fw={600}>Azure DevOps</Text>
              <TextInput label="Organization" {...field('devopsOrg')} />
              <PasswordInput label="Personal Access Token (optional)" {...field('devopsPat')} />

              <Group justify="space-between" mt="md">
                <Group>
                  <Button onClick={handleSave} loading={saving}>
                    Save
                  </Button>
                  {!isDraft && !isActive && (
                    <Button variant="light" onClick={handleSetActive} disabled={saving}>
                      Set as active
                    </Button>
                  )}
                </Group>
                {!isDraft && (
                  <ActionIcon
                    color="red"
                    variant="subtle"
                    onClick={handleDelete}
                    disabled={saving || profiles.length <= 1}
                    title={
                      profiles.length <= 1 ? 'Cannot delete the only profile' : 'Delete profile'
                    }
                  >
                    <IconTrash size={18} />
                  </ActionIcon>
                )}
              </Group>
            </Stack>
          ) : (
            <Text c="dimmed">No profile selected.</Text>
          )}
        </Box>
      </Group>
    </Container>
  )
}
