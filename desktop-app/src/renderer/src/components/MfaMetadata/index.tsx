import dayjs from 'dayjs';
import { odooRead, OneToMany } from '@/lib/odoo-api';
import { useQuery } from '@tanstack/react-query';
import { Badge, Grid, LoadingOverlay, Stack, Text } from '@mantine/core';
import RelationLink from '@/components/RelationLink';
import UiCard from '@/components/UiCard';

type Props = {
    id: number;
};

type MfaRecord = {
    id: number;
    name: string;
    model_name: string;
    create_date: string;
    create_uid: OneToMany;
    write_date: string;
    write_uid: OneToMany;
    enabled: boolean;
    model_schema_in_id: OneToMany | false;
    model_schema_out_id: OneToMany | false;
};

function Item({ label, children }: { label: string; children: React.ReactNode }) {
    return (
        <Grid.Col span={6}>
            <Stack gap={0}>
                <Text c="dimmed" size="sm">
                    {label}
                </Text>
                <Text fw="bold" component="span" display="block">
                    {children}
                </Text>
            </Stack>
        </Grid.Col>
    );
}

export default function MfaMetadata({ id }: Props) {
    const { data, isLoading } = useQuery({
        queryKey: ['mfa', id, 'metadata'],
        queryFn: () =>
            odooRead('rip.model.function.access', [id], [
                'name',
                'model_name',
                'create_date',
                'create_uid',
                'write_date',
                'write_uid',
                'enabled',
                'model_schema_in_id',
                'model_schema_out_id',
            ]),
    });

    const record: MfaRecord | undefined = data?.[0];

    return (
        <UiCard title="Metadata">
            <div style={{ position: 'relative', minHeight: 80 }}>
                <LoadingOverlay visible={isLoading} />
                {record && (
                    <Grid>
                        <Item label="Name">{record.name}</Item>
                        <Item label="Model">{record.model_name}</Item>
                        <Item label="Created by">{record.create_uid[1]}</Item>
                        <Item label="Created at">
                            {dayjs(record.create_date).format('D/M/YY HH:mm')}
                        </Item>
                        <Item label="Updated by">{record.write_uid[1]}</Item>
                        <Item label="Updated at">
                            {dayjs(record.write_date).format('D/M/YY HH:mm')}
                        </Item>
                        <Item label="Enabled">
                            <Badge color={record.enabled ? 'green' : 'gray'}>
                                {record.enabled ? 'yes' : 'no'}
                            </Badge>
                        </Item>
                        <Item label="Schema In">
                            {record.model_schema_in_id ? (
                                <RelationLink
                                    model="rip.model.schema.in"
                                    pgId={record.model_schema_in_id[0]}
                                    name={record.model_schema_in_id[1]}
                                />
                            ) : (
                                '—'
                            )}
                        </Item>
                        <Item label="Schema Out">
                            {record.model_schema_out_id ? (
                                <RelationLink
                                    model="rip.model.schema.out"
                                    pgId={record.model_schema_out_id[0]}
                                    name={record.model_schema_out_id[1]}
                                />
                            ) : (
                                '—'
                            )}
                        </Item>
                    </Grid>
                )}
            </div>
        </UiCard>
    );
}
