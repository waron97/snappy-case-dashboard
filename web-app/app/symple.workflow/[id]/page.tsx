'use client';

import Link from 'next/link';
import { useParams } from 'next/navigation';
import { IconCode } from '@tabler/icons-react';
import { Anchor, Button, Container, Group, Space, Tabs, Title } from '@mantine/core';
import { WorkflowContext } from './context';
import PhasesAndResults from './tabs/PhasesAndResults';
import useActions from './useActions';
import useData from './useData';

// -------------------------------------
// Component
// -------------------------------------

export default function SympleWorkflow() {
    // -------------------------------------
    // Hooks
    // -------------------------------------

    const params = useParams();
    const id = Number(params.id);

    // -------------------------------------
    // Queries
    // -------------------------------------

    const data = useData(id);
    const actions = useActions(id);

    // -------------------------------------
    // Effects
    // -------------------------------------

    // -------------------------------------
    // Functions
    // -------------------------------------

    // -------------------------------------
    // Local Variables
    // -------------------------------------

    // -------------------------------------

    return (
        <WorkflowContext.Provider value={{ ...data, ...actions }}>
            <Container size="xl" py="md">
                <Group justify="space-between">
                    <Title fz={28}>
                        {data.workflow?.name ?? '…'} (#{id})
                    </Title>
                    <Group gap="sm">
                        <Anchor
                            href={`${process.env.ODOO_URL}/web#id=${id}&model=symple.workflow&view_type=form`}
                            target="_blank"
                        >
                            <Button bg="#714B67">ODOO</Button>
                        </Anchor>
                        <Link href={`/full-field-config/symple.workflow/${id}`}>
                            <Button>
                                <IconCode />
                            </Button>
                        </Link>
                    </Group>
                </Group>

                <Space h={32} />

                <Tabs defaultValue="overview">
                    <Tabs.List>
                        <Tabs.Tab value="overview">Phases and Results</Tabs.Tab>
                    </Tabs.List>

                    <Tabs.Panel value="overview" pt="md">
                        <PhasesAndResults />
                    </Tabs.Panel>
                </Tabs>
            </Container>
        </WorkflowContext.Provider>
    );
}
