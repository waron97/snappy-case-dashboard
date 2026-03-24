import dayjs from 'dayjs';
import { getAssets, odooRead, OneToMany } from '@app/api';
import { useQuery } from '@tanstack/react-query';
import { Badge, Grid, Stack, Table, Tabs, Text } from '@mantine/core';
import RelationLink from '@/components/RelationLink';

type Props = {
    id: number;
};

type ServicePointFields = {
    code: string;
    client_id: OneToMany | false;
    state: 'active' | 'inactive' | 'activating' | 'deactivating' | 'refused';
    commodity: 'pod' | 'pdr' | 'fiber' | false;
    supply_start_date: string | false;
    supply_end_date: string | false;
    pod_id: OneToMany | false;
    pdr_id: OneToMany | false;
    idr_code: string | false;
    tension: string | false;
    engaged_power: number | false;
    available_power: number | false;
    tariff_code: string | false;
    use_type: string | false;
    use_category: string | false;
    declared_annual_usage: number | false;
    distributor_annual_usage: string | false;
    distributor_practice_code: string | false;
};

const rel = (field: OneToMany | false): string | false =>
    field ? `${field[1]} (#${field[0]})` : false;

const STATE_COLORS: Record<ServicePointFields['state'], string> = {
    active: 'green',
    activating: 'blue',
    deactivating: 'orange',
    inactive: 'red',
    refused: 'red',
};

export default function ServicePoint(props: Props) {
    const { id } = props;

    const { data } = useQuery<ServicePointFields>({
        queryKey: ['service.point', id, 'popover'],
        queryFn: () =>
            odooRead(
                'service.point',
                [id],
                [
                    'code',
                    'client_id',
                    'state',
                    'commodity',
                    'supply_start_date',
                    'supply_end_date',
                    'pod_id',
                    'pdr_id',
                    'idr_code',
                    'tension',
                    'engaged_power',
                    'available_power',
                    'tariff_code',
                    'use_type',
                    'use_category',
                    'declared_annual_usage',
                    'distributor_annual_usage',
                    'distributor_practice_code',
                ]
            ).then((res) => res[0]),
    });

    const { data: assets } = useQuery({
        queryKey: ['service.point', id, 'assets'],
        enabled: !!data?.code,
        queryFn: () => getAssets({ type: 'product', prcode: data?.code }),
    });

    const item = (label: string, value: string | number) => (
        <Stack gap={0}>
            <Text c="dimmed" size="sm">
                {label}
            </Text>
            <Text fw="bold">{value}</Text>
        </Stack>
    );

    if (!data) {
        return null;
    }

    const supplyIdentifier = () => {
        if (data.commodity === 'pod' && data.pod_id) {
            return item('POD', rel(data.pod_id) as string);
        }
        if (data.commodity === 'pdr' && data.pdr_id) {
            return item('PDR', rel(data.pdr_id) as string);
        }
        if (data.commodity === 'fiber' && data.idr_code) {
            return item('IDR Code', data.idr_code);
        }
        return null;
    };

    const technicalData = () => {
        if (data.commodity === 'pod') {
            return (
                <Grid pt="md">
                    <Grid.Col span={6}>
                        <Stack gap="sm">
                            {data.tension && item('Tension', data.tension)}
                            {data.engaged_power !== false &&
                                item('Engaged power (kW)', data.engaged_power)}
                            {data.available_power !== false &&
                                item('Available power (kW)', data.available_power)}
                        </Stack>
                    </Grid.Col>
                    <Grid.Col span={6}>
                        <Stack gap="sm">
                            {data.tariff_code && item('Tariff code', data.tariff_code)}
                            {data.use_type && item('Use type', data.use_type)}
                        </Stack>
                    </Grid.Col>
                </Grid>
            );
        }
        if (data.commodity === 'pdr') {
            return (
                <Grid pt="md">
                    <Grid.Col span={6}>
                        <Stack gap="sm">
                            {data.use_category && item('Use category', data.use_category)}
                            {data.declared_annual_usage !== false &&
                                item(
                                    'Declared annual usage (Smc/year)',
                                    data.declared_annual_usage
                                )}
                        </Stack>
                    </Grid.Col>
                    <Grid.Col span={6}>
                        <Stack gap="sm">
                            {data.distributor_annual_usage &&
                                item('Distributor annual usage', data.distributor_annual_usage)}
                            {data.distributor_practice_code &&
                                item('Distributor practice code', data.distributor_practice_code)}
                        </Stack>
                    </Grid.Col>
                </Grid>
            );
        }
        return null;
    };

    const renderAssets = () => {
        if (!assets) {
            return null;
        }

        return (
            <Table>
                <Table.Thead>
                    <Table.Tr>
                        <Table.Td>ID</Table.Td>
                        <Table.Td>State</Table.Td>
                        <Table.Td>SM State</Table.Td>
                        <Table.Td>Create date</Table.Td>
                    </Table.Tr>
                </Table.Thead>
                <Table.Tbody>
                    {assets.map((asset) => {
                        return (
                            <Table.Tr key={asset._id}>
                                <Table.Td>{asset._id}</Table.Td>
                                <Table.Td>{asset.assetstatus}</Table.Td>
                                <Table.Td>{asset.sm_state}</Table.Td>
                                <Table.Td>
                                    {dayjs(asset.createdate).format('D/M/YY HH:mm')}
                                </Table.Td>
                            </Table.Tr>
                        );
                    })}
                </Table.Tbody>
            </Table>
        );
    };

    return (
        <Tabs defaultValue="base">
            <Tabs.List>
                <Tabs.Tab value="base">Base information</Tabs.Tab>
                <Tabs.Tab value="assets">Assets</Tabs.Tab>
                <Tabs.Tab value="technical">Technical data</Tabs.Tab>
            </Tabs.List>

            <Tabs.Panel value="base">
                <Grid pt="md">
                    <Grid.Col span={6}>
                        <Stack gap="sm">
                            {item('PR Code', data.code)}
                            {data.client_id && (
                                <Stack gap={0}>
                                    <Text c="dimmed" size="sm">
                                        Client
                                    </Text>
                                    <RelationLink
                                        model="res.partner"
                                        pgId={data.client_id[0]}
                                        name={data.client_id[1]}
                                    />
                                </Stack>
                            )}
                            {data.supply_start_date && item('Supply start', data.supply_start_date)}
                            {data.supply_end_date && item('Supply end', data.supply_end_date)}
                        </Stack>
                    </Grid.Col>
                    <Grid.Col span={6}>
                        <Stack gap="sm">
                            <Stack gap={0}>
                                <Text c="dimmed" size="sm">
                                    State
                                </Text>
                                <Badge color={STATE_COLORS[data.state]} variant="light">
                                    {data.state}
                                </Badge>
                            </Stack>
                            {supplyIdentifier()}
                        </Stack>
                    </Grid.Col>
                </Grid>
            </Tabs.Panel>

            <Tabs.Panel value="assets">{renderAssets()}</Tabs.Panel>

            <Tabs.Panel value="technical">{technicalData()}</Tabs.Panel>
        </Tabs>
    );
}
