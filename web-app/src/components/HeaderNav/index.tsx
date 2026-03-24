'use client';

import { IconChevronDown } from '@tabler/icons-react';
import { Button, Group, Menu } from '@mantine/core';

export default function HeaderNav() {
    return (
        <Group gap="xs">
            <Menu trigger="hover" openDelay={50} closeDelay={100}>
                <Menu.Target>
                    <Button variant="subtle" rightSection={<IconChevronDown size={14} />} size="sm">
                        CRM
                    </Button>
                </Menu.Target>
                <Menu.Dropdown>
                    <Menu.Item component="a" href="/">
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
                    <Menu.Item component="a" href="/rip/mfa">
                        MFA
                    </Menu.Item>
                    <Menu.Item component="a" href="/rip/logs">
                        Logs
                    </Menu.Item>
                </Menu.Dropdown>
            </Menu>
        </Group>
    );
}
