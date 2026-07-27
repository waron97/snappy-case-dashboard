import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { IconCode, ReactNode } from '@tabler/icons-react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { toast } from 'react-toastify';
import {
    Alert,
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
import CaseActivePhase from '@/components/CaseActivePhase';
import CaseIntegrationHistory from '@/components/CaseIntegrationHistory';
import CaseLogs from '@/components/CaseLogs';
import CaseMarketComm from '@/components/CaseMarketComm';
import CaseStagingArea from '@/components/CaseStagingArea';
import CaseTabs from '@/components/CaseTabs';
import RelationLink from '@/components/RelationLink';
import UiCard from '@/components/UiCard';
import { useDocumentTitle } from '@/hooks/useDocumentTitle';
import { useSettings } from '@/lib/settings';
import { odooRead, odooWrite, OneToMany } from '@/lib/odoo-api';

type BaseFields = {
    id: number;
    name: string;
    stage_id: OneToMany;
    ticket_type_id: OneToMany;
    triplet_subtype_id: OneToMany;
    triplet_type_id: OneToMany;
    error_message?: string;
    info_message?: string;
    workflow_id: OneToMany;
    triplet_active_phase_id: OneToMany;
    parent_case_id: OneToMany;
    child_case_ids: number[];
    market_comm_event_log_ids: number[];
    integration_history_ids: number[];
    customer_id: OneToMany;
    partner_id?: OneToMany;
    customer_code: string;
    service_point_ids: number[];
};

type Props = {
    id: number;
    isActive?: boolean;
    onNameResolved?: (name: string) => void;
};

export default function Ticket({ id, isActive = true, onNameResolved }: Props) {
    // -------------------------------------
    // Hooks
    // -------------------------------------

    const queryClient = useQueryClient();
    const { activeProfile: settings } = useSettings();
    const [isClearing, setIsClearing] = useState(false);
    const [isCaseDone, setIsCaseDone] = useState(false);
    const [isLocked, setIsLocked] = useState(true);

    useDocumentTitle(`Case #${id}`, isActive);

    // -------------------------------------
    // Queries
    // -------------------------------------

    const {
        data: baseFields,
        isLoading: isBaseLoading,
        error,
    } = useQuery<BaseFields[]>({
        queryKey: ['case', id, 'for-base-view'],
        refetchInterval: isCaseDone || !isLocked ? undefined : 3 * 1000,
        queryFn: () =>
            odooRead(
                'helpdesk.ticket',
                [id],
                [
                    'name',
                    'stage_id',
                    'ticket_type_id',
                    'error_message',
                    'info_message',
                    'workflow_id',
                    'triplet_active_phase_id',
                    'triplet_subtype_id',
                    'triplet_type_id',
                    'parent_case_id',
                    'child_case_ids',
                    'market_comm_event_log_ids',
                    'integration_history_ids',
                    'customer_id',
                    'partner_id',
                    'customer_code',
                    'service_point_ids',
                ]
            ),
    });

    // -------------------------------------
    // Effects
    // -------------------------------------

    useEffect(() => {
        const stage = baseFields?.[0]?.stage_id?.[1];
        if (
            stage === 'Solved' ||
            stage === 'Cancelled' ||
            stage === 'Done KO' ||
            stage === 'Done'
        ) {
            setIsCaseDone(true);
        } else {
            setIsCaseDone(false);
        }
    }, [baseFields]);

    useEffect(() => {
        const name = baseFields?.[0]?.name;
        if (name) {
            onNameResolved?.(name);
        }
    }, [baseFields, onNameResolved]);

    // -------------------------------------
    // Functions
    // -------------------------------------

    async function handleClearInfoMessage() {
        setIsClearing(true);
        try {
            await odooWrite('helpdesk.ticket', [caseBaseFields.id], { info_message: null });
            queryClient.invalidateQueries({ queryKey: ['case', id, 'for-base-view'] });
        } catch (err) {
            toast(err instanceof Error ? err.message : 'Unknown error. Check browser console.');
            // eslint-disable-next-line no-console
            console.error(err);
        } finally {
            setIsClearing(false);
        }
    }

    function renderBasicInfo(values: BaseFields) {
        const item = (
            label: string,
            value: ReactNode,
            href?: string,
            wrapValue: boolean = true
        ) => (
            <Grid.Col span={4}>
                <Stack gap={0}>
                    <Text c="dimmed">{label}</Text>
                    {href ? (
                        <Anchor href={href} fw="bold">
                            {value}
                        </Anchor>
                    ) : wrapValue ? (
                        <Text fw="bold">{value}</Text>
                    ) : (
                        value
                    )}
                </Stack>
            </Grid.Col>
        );

        const parent = values.parent_case_id;

        return (
            <UiCard title="Case Type">
                <Stack>
                    <Grid>
                        {item(
                            'Type',
                            <RelationLink
                                name={values.triplet_type_id[1]}
                                pgId={values.triplet_type_id[0]}
                                model="symple.triplet.type"
                            />,
                            undefined,
                            false
                        )}
                        {item(
                            'Subtype',
                            <RelationLink
                                name={values.triplet_subtype_id[1]}
                                pgId={values.triplet_subtype_id[0]}
                                model="symple.triplet.subtype"
                            />,
                            undefined,
                            false
                        )}
                        {item(
                            'Detail',
                            <RelationLink
                                name={values.ticket_type_id[1]}
                                pgId={values.ticket_type_id[0]}
                                model="helpdesk.ticket.type"
                            />,
                            undefined,
                            false
                        )}
                    </Grid>
                    <Grid>
                        {item(
                            'Stage',
                            <RelationLink
                                name={values.stage_id[1]}
                                pgId={values.stage_id[0]}
                                model="helpdesk.stage"
                            />,
                            undefined,
                            false
                        )}
                        {!!values.workflow_id?.[0] &&
                            item(
                                'Workflow',
                                <RelationLink
                                    name={values.workflow_id[1]}
                                    pgId={values.workflow_id[0]}
                                    model="symple.workflow"
                                />,
                                undefined,
                                false
                            )}
                        {!!values.triplet_active_phase_id?.[0] &&
                            item(
                                'Active phase',
                                <RelationLink
                                    name={values.triplet_active_phase_id[1]}
                                    pgId={values.triplet_active_phase_id[0]}
                                    model="symple.triplet.phase"
                                />,
                                undefined,
                                false
                            )}
                        {!!parent?.[0] &&
                            item(
                                'Parent',
                                <RelationLink
                                    name={parent[1]}
                                    pgId={parent[0]}
                                    model="helpdesk.ticket"
                                    href={`/helpdesk.ticket/${parent[0]}`}
                                />,
                                undefined,
                                false
                            )}
                    </Grid>
                    <Grid>
                        {item(
                            'Customer',
                            <RelationLink
                                name={values.customer_id[1]}
                                pgId={values.customer_id[0]}
                                model="res.partner"
                            />,
                            undefined,
                            false
                        )}
                        {item('Customer code', values.customer_code)}
                        {!!values.partner_id?.[0] &&
                            item(
                                'Contact',
                                <RelationLink
                                    name={values.partner_id[1]}
                                    pgId={values.partner_id[0]}
                                    model="res.partner"
                                />,
                                undefined,
                                false
                            )}
                    </Grid>
                </Stack>
            </UiCard>
        );
    }

    function renderLeft() {
        return (
            <Stack gap="md">
                {caseBaseFields.error_message && (
                    <Alert color="red">{caseBaseFields.error_message}</Alert>
                )}
                {caseBaseFields.info_message && (
                    <Alert color="yellow">
                        <Group justify="space-between" align="start" wrap="nowrap">
                            <Text size="sm">{caseBaseFields.info_message}</Text>
                            <Button
                                size="xs"
                                variant="subtle"
                                color="yellow"
                                style={{ flexShrink: 0 }}
                                loading={isClearing}
                                onClick={handleClearInfoMessage}
                            >
                                Clear
                            </Button>
                        </Group>
                    </Alert>
                )}
                {renderBasicInfo(caseBaseFields)}
                <CaseActivePhase
                    caseId={caseBaseFields.id}
                    workflowId={caseBaseFields.workflow_id[0]}
                    activePhaseId={caseBaseFields.triplet_active_phase_id[0]}
                    isLocked={isLocked}
                    onLockChange={setIsLocked}
                />
                <CaseTabs
                    caseId={caseBaseFields.id}
                    servicePointIds={caseBaseFields.service_point_ids}
                    childIds={caseBaseFields.child_case_ids}
                    workflowId={caseBaseFields.workflow_id[0]}
                    activePhaseId={caseBaseFields.triplet_active_phase_id[0]}
                    isCaseDone={isCaseDone}
                />
            </Stack>
        );
    }

    // -------------------------------------
    // Local Variables
    // -------------------------------------

    if (isBaseLoading) {
        return (
            <Center py="xl">
                <Loader />
            </Center>
        );
    }

    const caseBaseFields = baseFields![0];

    if (!caseBaseFields || !caseBaseFields?.id || error) {
        return (
            <Container size="lg" py="xl">
                <Center py="xl">
                    <Text c="red">
                        Failed to load case:{' '}
                        {error instanceof Error ? error.message : 'Unknown error'}
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
                    {caseBaseFields.name} (#{id})
                </Title>
                <Group gap="sm">
                    <Anchor
                        href={`${settings?.odooUrl}/web#id=${id}&model=helpdesk.ticket&view_type=form`}
                        target="_blank"
                    >
                        <Button bg="#714B67">ODOO</Button>
                    </Anchor>

                    <Link to={`/full-field-config/helpdesk.ticket/${id}`}>
                        <Button>
                            <IconCode />
                        </Button>
                    </Link>
                </Group>
            </Group>

            <Space h={32} />

            <Grid gutter="md">
                <Grid.Col span={8}>{renderLeft()}</Grid.Col>
                <Grid.Col span={4}>
                    <Stack gap="lg">
                        {caseBaseFields.market_comm_event_log_ids.length > 0 && (
                            <UiCard title="Market comm">
                                <CaseMarketComm caseId={caseBaseFields.id} />
                            </UiCard>
                        )}
                        <UiCard title="Logs">
                            <CaseLogs caseId={caseBaseFields.id} />
                        </UiCard>
                        {caseBaseFields.integration_history_ids.length > 0 && (
                            <UiCard title="Integration History">
                                <CaseIntegrationHistory caseId={caseBaseFields.id} />
                            </UiCard>
                        )}
                        <UiCard title="Staging Area">
                            <CaseStagingArea caseId={caseBaseFields.id} />
                        </UiCard>
                    </Stack>
                </Grid.Col>
            </Grid>
        </Container>
    );
}
