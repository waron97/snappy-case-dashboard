import { useEffect, useState } from 'react'
import { IconSettings } from '@tabler/icons-react'
import {
  ActionIcon,
  Button,
  Divider,
  Modal,
  PasswordInput,
  Stack,
  Text,
  TextInput
} from '@mantine/core'
import { useSettings, type Settings } from '@/lib/settings'

const EMPTY_SETTINGS: Settings = {
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

export default function SettingsModal(): React.JSX.Element {
  const { settings, save } = useSettings()
  const [opened, setOpened] = useState(false)
  const [saving, setSaving] = useState(false)
  const [formData, setFormData] = useState<Settings>(settings ?? EMPTY_SETTINGS)

  useEffect(() => {
    if (settings) {
      setFormData(settings)
    }
  }, [settings])

  function field(key: keyof Settings): {
    value: string
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void
    disabled: boolean
  } {
    return {
      value: formData[key],
      onChange: (e) => setFormData({ ...formData, [key]: e.currentTarget.value }),
      disabled: saving
    }
  }

  async function handleSubmit(): Promise<void> {
    setSaving(true)
    try {
      await save(formData)
      setOpened(false)
    } finally {
      setSaving(false)
    }
  }

  return (
    <>
      <ActionIcon variant="subtle" size="lg" color="gray" onClick={() => setOpened(true)}>
        <IconSettings size={20} />
      </ActionIcon>

      <Modal
        opened={opened}
        onClose={() => setOpened(false)}
        title="Settings"
        centered
        size="lg"
      >
        <Stack gap="md">
          <Text fw={600}>Keycloak</Text>
          <TextInput label="Keycloak URL" placeholder="https://keycloak.example.com/..." {...field('keycloakUrl')} />
          <TextInput label="Client ID" {...field('keycloakClientId')} />
          <PasswordInput label="Client Secret" {...field('keycloakClientSecret')} />
          <TextInput label="Service Username" {...field('keycloakServiceUsername')} />
          <PasswordInput label="Service Password" {...field('keycloakServicePassword')} />

          <Divider />
          <Text fw={600}>Odoo</Text>
          <TextInput label="Odoo URL" placeholder="https://odoo.example.com" {...field('odooUrl')} />
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

          <Button onClick={handleSubmit} loading={saving} fullWidth>
            Save Settings
          </Button>
        </Stack>
      </Modal>
    </>
  )
}
