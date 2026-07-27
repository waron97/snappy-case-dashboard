import { useNavigate, useParams } from 'react-router-dom'
import { Drawer } from '@mantine/core'
import RipMfaList from '@/routes/RipMfaList'
import RipMfaDetail from '@/routes/RipMfaDetail'

export default function MfaWorkspace(): React.JSX.Element {
  const { id } = useParams()
  const navigate = useNavigate()

  return (
    <>
      <RipMfaList />
      <Drawer position="bottom" size="90%" opened={!!id} onClose={() => navigate('/rip/mfa')}>
        {id && <RipMfaDetail />}
      </Drawer>
    </>
  )
}
