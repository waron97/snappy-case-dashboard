import { lazy, Suspense } from 'react'
import { Center, Loader } from '@mantine/core'
import CaseDetail from '@/routes/CaseDetail'
import FullFieldConfig from '@/routes/FullFieldConfig'
import type { OpenWorkspaceTab } from '@/lib/useCaseTabs'

// Every panel stays mounted (the parent Tabs uses keepMounted), so the Symphony
// pages are code-split to keep them out of the initial bundle — same treatment
// the workflow chart and the case-detail sidebar cards get.
const SymphonyRequests = lazy(() => import('@/routes/SymphonyRequests'))
const SymphonyRequestDetail = lazy(() => import('@/routes/SymphonyRequestDetail'))
const SymphonyDeepSearch = lazy(() => import('@/routes/SymphonyDeepSearch'))

type Props = {
  tab: OpenWorkspaceTab
  isActive: boolean
  onNameResolved: (name: string) => void
}

function unknownTab(tab: never): never {
  throw new Error(`Unknown workspace tab kind: ${JSON.stringify(tab)}`)
}

export default function TabPanelContent({
  tab,
  isActive,
  onNameResolved
}: Props): React.JSX.Element {
  switch (tab.kind) {
    case 'case':
      return <CaseDetail id={tab.id} isActive={isActive} onNameResolved={onNameResolved} />
    case 'field-config':
      return (
        <FullFieldConfig
          model={tab.model}
          recordId={tab.recordId}
          isActive={isActive}
          onNameResolved={onNameResolved}
        />
      )
    case 'symphony-list':
      return (
        <Suspense fallback={<Fallback />}>
          <SymphonyRequests isActive={isActive} />
        </Suspense>
      )
    case 'symphony-request':
      return (
        <Suspense fallback={<Fallback />}>
          <SymphonyRequestDetail
            requestId={tab.requestId}
            processId={tab.processId}
            isActive={isActive}
            onNameResolved={onNameResolved}
          />
        </Suspense>
      )
    case 'symphony-deep-search':
      return (
        <Suspense fallback={<Fallback />}>
          <SymphonyDeepSearch
            jobId={tab.jobId}
            isActive={isActive}
            onNameResolved={onNameResolved}
          />
        </Suspense>
      )
    default:
      return unknownTab(tab)
  }
}

function Fallback(): React.JSX.Element {
  return (
    <Center h={300}>
      <Loader />
    </Center>
  )
}
