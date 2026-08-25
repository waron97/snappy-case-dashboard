'use client';

import { Button, Group } from '@mantine/core';

export default function HeaderNav() {
    return (
        <Group gap="xs">
            <Button component="a" href="/devops/pr-list" variant="subtle" size="sm">
                Pull Requests
            </Button>
            <Button component="a" href="/devops/control" variant="subtle" size="sm">
                Control Panel
            </Button>
            <Button component="a" href="/devops/instances" variant="subtle" size="sm">
                Instances
            </Button>
        </Group>
    );
}
