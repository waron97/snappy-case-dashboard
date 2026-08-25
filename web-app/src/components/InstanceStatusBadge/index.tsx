'use client';

import { Badge, Group, Loader } from '@mantine/core';
import type { InstanceStatus } from '@app/devops/actions';

const INSTANCE_COLOR: Record<InstanceStatus['status'], string> = {
    stopped: 'gray',
    starting: 'yellow',
    running: 'green',
    error: 'red',
};

const INSTANCE_LABEL: Record<InstanceStatus['status'], string> = {
    stopped: 'stopped',
    starting: 'starting',
    running: 'running',
    error: 'error',
};

export function InstanceStatusBadge({ status }: { status: InstanceStatus['status'] }) {
    if (status === 'starting') {
        return (
            <Badge color={INSTANCE_COLOR[status]} variant="light" size="lg" tt="none">
                <Group gap={6} wrap="nowrap">
                    <Loader size={10} color={INSTANCE_COLOR[status]} />
                    {INSTANCE_LABEL[status]}
                </Group>
            </Badge>
        );
    }

    return (
        <Badge
            color={INSTANCE_COLOR[status]}
            variant={status === 'running' ? 'filled' : 'light'}
            size="lg"
            tt="none"
        >
            {INSTANCE_LABEL[status]}
        </Badge>
    );
}
