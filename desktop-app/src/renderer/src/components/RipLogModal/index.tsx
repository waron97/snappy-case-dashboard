import dayjs from 'dayjs';
import ReactJson from 'react-json-view';
import { odooRead } from '@/lib/odoo-api';
import { useQuery } from '@tanstack/react-query';
import { Badge, Center, Group, Loader, Modal, Stack, Tabs, Text } from '@mantine/core';

type Props = {
    id: number | null;
    onClose: () => void;
};

type RipLogDetail = {
    id: number;
    endpoint: string;
    method: string;
    status: number;
    args: string;
    content: string;
    response_content: string;
    create_date: string;
};


const parseJson = (str: string | undefined) => {
    if (!str) { return {}; }
    try {
        return JSON.parse(str);
    } catch {
        return { raw: str };
    }
};

export default function RipLogModal({ id, onClose }: Props) {
    // -------------------------------------
    // Queries
    // -------------------------------------

    const { data, isLoading } = useQuery({
        queryKey: ['rip.request.log', id, 'detail'],
        queryFn: () =>
            odooRead(
                'rip.request.log',
                [id!],
                [
                    'endpoint',
                    'method',
                    'status',
                    'args',
                    'content',
                    'response_content',
                    'create_date',
                ]
            ),
        enabled: id !== null,
    });

    // -------------------------------------
    // Local Variables
    // -------------------------------------

    const log: RipLogDetail | undefined = data?.[0];

    // -------------------------------------

    return (
        <Modal opened={id !== null} onClose={onClose} size="xl" title={log?.endpoint ?? '…'}>
            {isLoading && (
                <Center py="xl">
                    <Loader size="sm" />
                </Center>
            )}
            {log && (
                <Tabs defaultValue="general">
                    <Tabs.List>
                        <Tabs.Tab value="general">General</Tabs.Tab>
                        <Tabs.Tab value="content">Content</Tabs.Tab>
                        <Tabs.Tab value="response">Response Content</Tabs.Tab>
                    </Tabs.List>

                    <Tabs.Panel value="general" pt="md">
                        <Stack gap="xs">
                            <Text>
                                <strong>Endpoint:</strong> {log.endpoint}
                            </Text>
                            <Text>
                                <strong>Method:</strong> {log.method}
                            </Text>
                            <Group gap="xs" align="center">
                                <Text component="span">
                                    <strong>Status:</strong>
                                </Text>
                                <Badge
                                    color={log.status >= 200 && log.status < 300 ? 'green' : 'red'}
                                >
                                    {log.status}
                                </Badge>
                            </Group>
                            <Text>
                                <strong>Date:</strong>{' '}
                                {dayjs(log.create_date).format('D/M/YY HH:mm')}
                            </Text>
                            <Text style={{ wordBreak: 'break-all' }}>
                                <strong>Args:</strong> {log.args}
                            </Text>
                        </Stack>
                    </Tabs.Panel>

                    <Tabs.Panel value="content" pt="md">
                        <ReactJson src={parseJson(log.content)} theme="monokai" />
                    </Tabs.Panel>

                    <Tabs.Panel value="response" pt="md">
                        <ReactJson src={parseJson(log.response_content)} theme="monokai" />
                    </Tabs.Panel>
                </Tabs>
            )}
        </Modal>
    );
}
