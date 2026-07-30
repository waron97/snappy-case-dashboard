import { lazy, Suspense } from 'react'
import { Center, Loader, Tabs } from '@mantine/core'
import CaseChildren from '@/components/CaseChildren'
import CaseSymphonyProcesses from '@/components/CaseSymphonyProcesses'
import CaseServicePoints from '@/components/CaseServicePoints'
import CaseTimeline from '@/components/CaseTimeline'
import UiCard from '@/components/UiCard'

const CaseWorkflowChart = lazy(() => import('../CaseWorkflowChart'))

type Props = {
  caseId: number
  servicePointIds: number[]
  childIds: number[]
  workflowId: number
  activePhaseId?: number
  isCaseDone: boolean
}

export default function CaseTabs(props: Props) {
  const { caseId, servicePointIds, childIds, workflowId, activePhaseId, isCaseDone } = props

  return (
    <UiCard>
      <Tabs defaultValue="chart">
        <Tabs.List>
          <Tabs.Tab value="chart">Chart history</Tabs.Tab>
          <Tabs.Tab value="history">History</Tabs.Tab>
          <Tabs.Tab value="service_points">Service Points</Tabs.Tab>
          <Tabs.Tab value="children">Child cases</Tabs.Tab>
          <Tabs.Tab value="symphony">Symphony processes</Tabs.Tab>
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
        <Tabs.Panel value="symphony">
          <CaseSymphonyProcesses caseId={caseId} />
        </Tabs.Panel>
        <Tabs.Panel value="chart">
          <Suspense
            fallback={
              <Center h={200}>
                <Loader />
              </Center>
            }
          >
            <CaseWorkflowChart
              caseId={caseId}
              workflowId={workflowId}
              activePhaseId={activePhaseId}
              isCaseDone={isCaseDone}
            />
          </Suspense>
        </Tabs.Panel>
      </Tabs>
    </UiCard>
  )
}
