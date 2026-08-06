import { lazy, Suspense } from 'react'
import { Center, Loader } from '@mantine/core'
import CaseDetail from '@/routes/CaseDetail'
import FullFieldConfig from '@/routes/FullFieldConfig'
import { unknownTab } from '@/lib/caseWorkspaceContext'
import type { OpenWorkspaceTab } from '@/lib/useCaseTabs'

// Every panel stays mounted (the parent Tabs uses keepMounted), so the heavier
// pages are code-split to keep them out of the initial bundle — same treatment
// the workflow chart and the case-detail sidebar cards get. Note this defers the
// *initial* download only: restoring a saved tab set renders all of its panels
// at once, hidden or not, so their chunks are fetched at startup anyway. Under
// file:// that's cheap. What actually defers the work is the visited gate each
// page applies to its own queries.
const SymphonyRequests = lazy(() => import('@/routes/SymphonyRequests'))
const SymphonyRequestDetail = lazy(() => import('@/routes/SymphonyRequestDetail'))
const SymphonyDeepSearch = lazy(() => import('@/routes/SymphonyDeepSearch'))
const RipLogs = lazy(() => import('@/routes/RipLogs'))
const RipMfaList = lazy(() => import('@/routes/RipMfaList'))
const RipMfaDetail = lazy(() => import('@/routes/RipMfaDetail'))
const SympleWorkflowDetail = lazy(() => import('@/routes/SympleWorkflowDetail'))
const DevOpsWorkItems = lazy(() => import('@/routes/DevOpsWorkItems'))

type Props = {
  tab: OpenWorkspaceTab
  isActive: boolean
  onNameResolved: (name: string) => void
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
    case 'rip-logs':
      return (
        <Suspense fallback={<Fallback />}>
          <RipLogs isActive={isActive} />
        </Suspense>
      )
    case 'rip-mfa-list':
      return (
        <Suspense fallback={<Fallback />}>
          <RipMfaList isActive={isActive} />
        </Suspense>
      )
    case 'rip-mfa':
      return (
        <Suspense fallback={<Fallback />}>
          <RipMfaDetail id={tab.id} isActive={isActive} onNameResolved={onNameResolved} />
        </Suspense>
      )
    case 'symple-workflow':
      return (
        <Suspense fallback={<Fallback />}>
          <SympleWorkflowDetail id={tab.id} isActive={isActive} onNameResolved={onNameResolved} />
        </Suspense>
      )
    case 'devops-work-items':
      return (
        <Suspense fallback={<Fallback />}>
          <DevOpsWorkItems isActive={isActive} />
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
