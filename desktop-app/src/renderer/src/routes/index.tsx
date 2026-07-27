import { Route, Routes } from 'react-router-dom'
import MfaWorkspace from '@/components/MfaWorkspace'
import RipLogs from './RipLogs'
import SympleWorkflowDetail from './SympleWorkflowDetail'
import DevOpsWorkItems from './DevOpsWorkItems'

export function AppRoutes(): React.JSX.Element {
  return (
    <Routes>
      <Route path="/rip/mfa/:id?" element={<MfaWorkspace />} />
      <Route path="/rip/logs" element={<RipLogs />} />
      <Route path="/symple.workflow/:id" element={<SympleWorkflowDetail />} />
      <Route path="/devops/work-items" element={<DevOpsWorkItems />} />
    </Routes>
  )
}
