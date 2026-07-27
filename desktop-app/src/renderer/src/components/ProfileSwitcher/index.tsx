import { Link } from 'react-router-dom'
import { IconChevronDown } from '@tabler/icons-react'
import { Button, Menu } from '@mantine/core'
import { useSettings } from '@/lib/settings'

export default function ProfileSwitcher(): React.JSX.Element | null {
  const { profiles, activeProfile, setActiveProfile } = useSettings()

  if (!activeProfile) return null

  async function handleSelect(id: string): Promise<void> {
    if (id === activeProfile?.id) return
    const target = profiles.find((p) => p.id === id)
    if (
      !window.confirm(
        `Switch active profile to "${target?.name}"? Open case tabs will close and the app will reload.`
      )
    ) {
      return
    }
    await setActiveProfile(id)
  }

  return (
    <Menu trigger="click" position="bottom-end">
      <Menu.Target>
        <Button
          variant="subtle"
          color="gray"
          size="sm"
          rightSection={<IconChevronDown size={14} />}
        >
          {activeProfile.name}
        </Button>
      </Menu.Target>
      <Menu.Dropdown>
        {profiles.map((p) => (
          <Menu.Item
            key={p.id}
            onClick={() => handleSelect(p.id)}
            fw={p.id === activeProfile.id ? 600 : undefined}
          >
            {p.name}
            {p.id === activeProfile.id ? ' (active)' : ''}
          </Menu.Item>
        ))}
        <Menu.Divider />
        <Menu.Item component={Link} to="/settings">
          Manage profiles…
        </Menu.Item>
      </Menu.Dropdown>
    </Menu>
  )
}
