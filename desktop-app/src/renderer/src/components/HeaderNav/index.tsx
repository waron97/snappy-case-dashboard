import { Link } from 'react-router-dom'
import { IconChevronDown } from '@tabler/icons-react'
import { Button, Group, Menu } from '@mantine/core'

type Props = {
  hasDevOpsToken: boolean
}

export default function HeaderNav({ hasDevOpsToken }: Props): React.JSX.Element {
  return (
    <Group gap="xs">
      <Menu trigger="hover" openDelay={50} closeDelay={100}>
        <Menu.Target>
          <Button variant="subtle" rightSection={<IconChevronDown size={14} />} size="sm">
            CRM
          </Button>
        </Menu.Target>
        <Menu.Dropdown>
          <Menu.Item component={Link} to="/">
            Cases
          </Menu.Item>
        </Menu.Dropdown>
      </Menu>

      <Menu trigger="hover" openDelay={50} closeDelay={100}>
        <Menu.Target>
          <Button variant="subtle" rightSection={<IconChevronDown size={14} />} size="sm">
            RIP
          </Button>
        </Menu.Target>
        <Menu.Dropdown>
          <Menu.Item component={Link} to="/rip/mfa">
            MFA
          </Menu.Item>
          <Menu.Item component={Link} to="/rip/logs">
            Logs
          </Menu.Item>
        </Menu.Dropdown>
      </Menu>

      {hasDevOpsToken && (
        <Menu trigger="hover" openDelay={50} closeDelay={100}>
          <Menu.Target>
            <Button variant="subtle" rightSection={<IconChevronDown size={14} />} size="sm">
              DevOps
            </Button>
          </Menu.Target>
          <Menu.Dropdown>
            <Menu.Item component={Link} to="/devops/work-items">
              My Work Items
            </Menu.Item>
          </Menu.Dropdown>
        </Menu>
      )}
    </Group>
  )
}
