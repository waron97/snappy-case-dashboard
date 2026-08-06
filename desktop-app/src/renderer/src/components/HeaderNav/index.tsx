import { IconChevronDown } from '@tabler/icons-react'
import { Button, Group, Menu } from '@mantine/core'
import { LIST_TAB, newInstance, useCaseTabs } from '@/lib/useCaseTabs'

type Props = {
  hasDevOpsToken: boolean
}

// These are openTab calls rather than <Link>s because RIP logs and the MFA list
// are multi-instance: a second <Link to="/rip/logs"> wouldn't change the
// pathname, so the URL -> tab effect would never fire and no second tab would
// appear. The singleton items go through openTab too, for one code path.
export default function HeaderNav({ hasDevOpsToken }: Props): React.JSX.Element {
  const { tabs, openTab } = useCaseTabs()

  return (
    <Group gap="xs">
      <Menu trigger="hover" openDelay={50} closeDelay={100}>
        <Menu.Target>
          <Button variant="subtle" rightSection={<IconChevronDown size={14} />} size="sm">
            CRM
          </Button>
        </Menu.Target>
        <Menu.Dropdown>
          <Menu.Item onClick={() => openTab(LIST_TAB)}>Cases</Menu.Item>
          <Menu.Item onClick={() => openTab({ kind: 'symphony-list' })}>Symphony</Menu.Item>
        </Menu.Dropdown>
      </Menu>

      <Menu trigger="hover" openDelay={50} closeDelay={100}>
        <Menu.Target>
          <Button variant="subtle" rightSection={<IconChevronDown size={14} />} size="sm">
            RIP
          </Button>
        </Menu.Target>
        <Menu.Dropdown>
          <Menu.Item onClick={() => openTab(...newInstance('rip-mfa-list', tabs))}>MFA</Menu.Item>
          <Menu.Item onClick={() => openTab(...newInstance('rip-logs', tabs))}>Logs</Menu.Item>
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
            <Menu.Item onClick={() => openTab({ kind: 'devops-work-items' })}>
              My Work Items
            </Menu.Item>
          </Menu.Dropdown>
        </Menu>
      )}
    </Group>
  )
}
