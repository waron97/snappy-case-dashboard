'use client';

import dayjs from 'dayjs';
import { getMyWorkItems } from '@app/devops-api';
import { useQuery } from '@tanstack/react-query';
import { IconMessageCircle } from '@tabler/icons-react';
import {
    Alert,
    Badge,
    Card,
    Center,
    Container,
    Loader,
    SimpleGrid,
    Stack,
    Text,
    Title,
} from '@mantine/core';

const STATUS_COLORS: Record<string, string> = {
    Closed: 'gray',
    Resolved: 'gray',
    Removed: 'gray',
    Active: 'blue',
    New: 'yellow',
};

function truncate(text: string, length: number): string {
    return text.length > length ? `${text.slice(0, length)}…` : text;
}

export default function DevOpsWorkItems() {
    const { data, isLoading, isError, error } = useQuery({
        queryKey: ['devops-work-items'],
        queryFn: getMyWorkItems,
    });

    if (isError) {
        return (
            <Container size="lg" py="xl">
                <Center py="xl">
                    <Text c="red">
                        Failed to load work items:{' '}
                        {error instanceof Error ? error.message : 'Unknown error'}
                    </Text>
                </Center>
            </Container>
        );
    }

    if (isLoading) {
        return (
            <Container size="lg" py="xl">
                <Center py="xl">
                    <Loader size="sm" />
                </Center>
            </Container>
        );
    }

    if (!data || data.length === 0) {
        return (
            <Container size="lg" py="xl">
                <Center py="xl">
                    <Text c="dimmed">No work items found.</Text>
                </Center>
            </Container>
        );
    }

    return (
        <Container size="xl" py="sm">
            <Stack gap="md" pt="md">
                <Title order={3}>My Work Items</Title>
                <SimpleGrid cols={{ base: 1, sm: 2, lg: 3 }} spacing="md">
                    {data.map((item) => (
                        <Card
                            key={item.id}
                            component="a"
                            href={item.url}
                            target="_blank"
                            rel="noreferrer"
                            withBorder
                            padding="md"
                        >
                            <Stack gap="xs">
                                <Badge color={STATUS_COLORS[item.status] ?? 'blue'} size="sm">
                                    {item.status}
                                </Badge>
                                <Text fw={600}>{item.title}</Text>
                                {item.description && (
                                    <Text size="sm" c="dimmed">
                                        {truncate(item.description, 200)}
                                    </Text>
                                )}
                                <Text size="sm">Assignee: {item.assignee ?? 'Unassigned'}</Text>
                                <Text size="sm">
                                    Created: {dayjs(item.createdDate).format('D/M/YY HH:mm')}
                                </Text>
                                {item.lastCommentDate ? (
                                    <Alert
                                        icon={<IconMessageCircle size={16} />}
                                        title={`${item.lastCommentAuthor ?? 'Unknown'} · ${dayjs(
                                            item.lastCommentDate
                                        ).format('D/M/YY HH:mm')}`}
                                        color="blue"
                                        variant="light"
                                    >
                                        {truncate(item.lastCommentText ?? '', 150)}
                                    </Alert>
                                ) : (
                                    <Text size="sm" c="dimmed">
                                        No comments yet
                                    </Text>
                                )}
                            </Stack>
                        </Card>
                    ))}
                </SimpleGrid>
            </Stack>
        </Container>
    );
}
