import { lazy, Suspense } from 'react'
import { Center, Loader } from '@mantine/core'
import { Route, Routes } from 'react-router-dom'

const MfaWorkspace = lazy(() => import('@/components/MfaWorkspace'))
const RipLogs = lazy(() => import('./RipLogs'))
const SympleWorkflowDetail = lazy(() => import('./SympleWorkflowDetail'))
const DevOpsWorkItems = lazy(() => import('./DevOpsWorkItems'))

function RouteFallback(): React.JSX.Element {
  return (
    <Center h="100%" mt="xl">
      <Loader />
    </Center>
  )
}

export function AppRoutes(): React.JSX.Element {
  return (
    <Suspense fallback={<RouteFallback />}>
      <Routes>
        <Route path="/rip/mfa/:id?" element={<MfaWorkspace />} />
        <Route path="/rip/logs" element={<RipLogs />} />
        <Route path="/symple.workflow/:id" element={<SympleWorkflowDetail />} />
        <Route path="/devops/work-items" element={<DevOpsWorkItems />} />
      </Routes>
    </Suspense>
  )
}
