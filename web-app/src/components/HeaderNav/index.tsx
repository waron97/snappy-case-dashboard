'use client';

import { Button, Group } from '@mantine/core';

interface HeaderNavProps {
    showDevops?: boolean;
}

export default function HeaderNav({ showDevops }: HeaderNavProps) {
    if (!showDevops) {
        return null;
    }
    return (
        <Group gap="xs">
            <Button component="a" href="/devops/pr-list" variant="subtle" size="sm">
                Pull Requests
            </Button>
            <Button component="a" href="/devops/control" variant="subtle" size="sm">
                Control Panel
            </Button>
        </Group>
    );
}
