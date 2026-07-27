import { Route, Routes } from 'react-router-dom'
import CaseList from './CaseList'
import CaseDetail from './CaseDetail'
import FullFieldConfig from './FullFieldConfig'
import RipMfaList from './RipMfaList'
import RipMfaDetail from './RipMfaDetail'
import RipLogs from './RipLogs'
import SympleWorkflowDetail from './SympleWorkflowDetail'
import DevOpsWorkItems from './DevOpsWorkItems'

export function AppRoutes(): React.JSX.Element {
  return (
    <Routes>
      <Route path="/" element={<CaseList />} />
      <Route path="/helpdesk.ticket/:id" element={<CaseDetail />} />
      <Route path="/full-field-config/:model/:record" element={<FullFieldConfig />} />
      <Route path="/rip/mfa" element={<RipMfaList />} />
      <Route path="/rip/mfa/:id" element={<RipMfaDetail />} />
      <Route path="/rip/logs" element={<RipLogs />} />
      <Route path="/symple.workflow/:id" element={<SympleWorkflowDetail />} />
      <Route path="/devops/work-items" element={<DevOpsWorkItems />} />
    </Routes>
  )
}
