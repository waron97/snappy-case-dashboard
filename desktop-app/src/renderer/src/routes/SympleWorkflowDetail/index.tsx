import { Link, useParams } from 'react-router-dom'
import { IconCode } from '@tabler/icons-react'
import { Anchor, Button, Container, Group, Space, Tabs, Title } from '@mantine/core'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { useSettings } from '@/lib/settings'
import { WorkflowContext } from './context'
import useActions from './useActions'
import useData from './useData'
import PhasesAndResults from './tabs/PhasesAndResults'

// -------------------------------------
// Component
// -------------------------------------

export default function SympleWorkflow() {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const params = useParams()
  const id = Number(params.id)
  const { activeProfile: settings } = useSettings()

  // -------------------------------------
  // Queries
  // -------------------------------------

  const data = useData(id)
  const actions = useActions(id)

  // -------------------------------------
  // Effects
  // -------------------------------------

  useDocumentTitle(data.workflow ? `${data.workflow.name} (#${id})` : undefined)

  // -------------------------------------
  // Functions
  // -------------------------------------

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // -------------------------------------

  return (
    <WorkflowContext.Provider value={{ ...data, ...actions }}>
      <Container size="xl" py="md">
        <Group justify="space-between">
          <Title fz={28}>
            {data.workflow?.name ?? '…'} (#{id})
          </Title>
          <Group gap="sm">
            <Anchor
              href={`${settings?.odooUrl}/web#id=${id}&model=symple.workflow&view_type=form`}
              target="_blank"
            >
              <Button bg="#714B67">ODOO</Button>
            </Anchor>
            <Link to={`/full-field-config/symple.workflow/${id}`}>
              <Button>
                <IconCode />
              </Button>
            </Link>
          </Group>
        </Group>

        <Space h={32} />

        <Tabs defaultValue="overview">
          <Tabs.List>
            <Tabs.Tab value="overview">Phases and Results</Tabs.Tab>
          </Tabs.List>

          <Tabs.Panel value="overview" pt="md">
            <PhasesAndResults />
          </Tabs.Panel>
        </Tabs>
      </Container>
    </WorkflowContext.Provider>
  )
}
