import { Tabs } from '@mantine/core';
import CaseChildren from '@/components/CaseChildren';
import CaseServicePoints from '@/components/CaseServicePoints';
import CaseTimeline from '@/components/CaseTimeline';
import UiCard from '@/components/UiCard';
import CaseWorkflowChart from '../CaseWorkflowChart';

type Props = {
    caseId: number;
    servicePointIds: number[];
    childIds: number[];
    workflowId: number;
    activePhaseId?: number;
};

export default function CaseTabs(props: Props) {
    const { caseId, servicePointIds, childIds, workflowId, activePhaseId } = props;

    return (
        <UiCard>
            <Tabs defaultValue="chart">
                <Tabs.List>
                    <Tabs.Tab value="chart">Chart history</Tabs.Tab>
                    <Tabs.Tab value="history">History</Tabs.Tab>
                    <Tabs.Tab value="service_points">Service Points</Tabs.Tab>
                    <Tabs.Tab value="children">Child cases</Tabs.Tab>
                </Tabs.List>

                <Tabs.Panel value="history">
                    <CaseTimeline caseId={caseId} />
                </Tabs.Panel>
                <Tabs.Panel value="service_points">
                    <CaseServicePoints caseId={caseId} pointIds={servicePointIds} />
                </Tabs.Panel>
                <Tabs.Panel value="children">
                    <CaseChildren caseId={caseId} childIds={childIds} />
                </Tabs.Panel>
                <Tabs.Panel value="chart">
                    <CaseWorkflowChart
                        caseId={caseId}
                        workflowId={workflowId}
                        activePhaseId={activePhaseId}
                    />
                </Tabs.Panel>
            </Tabs>
        </UiCard>
    );
}
