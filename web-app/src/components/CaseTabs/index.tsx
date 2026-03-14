'use client';

import { Tabs } from '@mantine/core';
import CaseChildren from '@/components/CaseChildren';
import CaseServicePoints from '@/components/CaseServicePoints';
import CaseTimeline from '@/components/CaseTimeline';
import UiCard from '@/components/UiCard';

type Props = {
  caseId: number;
  servicePointIds: number[];
  childIds: number[];
};

export default function CaseTabs(props: Props) {
  const { caseId, servicePointIds, childIds } = props;

  return (
    <UiCard>
      <Tabs defaultValue="history">
        <Tabs.List>
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
      </Tabs>
    </UiCard>
  );
}
