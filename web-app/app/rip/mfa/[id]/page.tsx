'use client';

import { useEffect } from 'react';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import { odooRead } from '@app/api';
import { IconCode } from '@tabler/icons-react';
import { useQuery } from '@tanstack/react-query';
import {
    Anchor,
    Button,
    Center,
    Container,
    Grid,
    Group,
    Loader,
    Space,
    Stack,
    Text,
    Title,
} from '@mantine/core';
import MfaCode from '@/components/MfaCode';
import MfaMetadata from '@/components/MfaMetadata';
import MfaRecentCalls from '@/components/MfaRecentCalls';

export default function MFARecord() {
    // -------------------------------------
    // Hooks
    // -------------------------------------

    const { id } = useParams();
    const numId = parseInt(String(id), 10);

    // -------------------------------------
    // Queries
    // -------------------------------------

    const { data, isLoading, error } = useQuery({
        queryKey: ['mfa', numId, 'title'],
        queryFn: () => odooRead('rip.model.function.access', [numId], ['name', 'model_name']),
    });

    // -------------------------------------
    // Effects
    // -------------------------------------

    useEffect(() => {
        const record = data?.[0];
        if (record) {
            // Preserve the server-rendered env prefix (e.g. "[T01] ") from the default title
            const prefix = document.title.replace(/Snappy$/, '');
            document.title = `${prefix}MFA ${record.name}`;
        }
    }, [data]);

    // -------------------------------------
    // Local Variables
    // -------------------------------------

    if (isLoading) {
        return (
            <Center py="xl">
                <Loader />
            </Center>
        );
    }

    const record = data?.[0];

    if (!record || error) {
        return (
            <Container size="lg" py="xl">
                <Center py="xl">
                    <Text c="red">
                        Failed to load function:{' '}
                        {error instanceof Error ? error.message : 'Not found'}
                    </Text>
                </Center>
            </Container>
        );
    }

    // -------------------------------------

    return (
        <Container size="xl" py="md">
            <Group gap="md" justify="space-between">
                <Title fz={28}>
                    {record.model_name}/{record.name} (#{id})
                </Title>
                <Group gap="sm">
                    <Anchor
                        href={`${process.env.ODOO_URL}/web#id=${id}&model=rip.model.function.access&view_type=form`}
                        target="_blank"
                    >
                        <Button bg="#714B67">ODOO</Button>
                    </Anchor>
                    <Link href={`/full-field-config/rip.model.function.access/${id}`}>
                        <Button>
                            <IconCode />
                        </Button>
                    </Link>
                </Group>
            </Group>

            <Space h={32} />

            <Grid gutter="md">
                <Grid.Col span={8}>
                    <MfaCode id={numId} />
                </Grid.Col>
                <Grid.Col span={4}>
                    <Stack gap="md">
                        <MfaMetadata id={numId} />
                        <MfaRecentCalls id={numId} />
                    </Stack>
                </Grid.Col>
            </Grid>
        </Container>
    );
}
