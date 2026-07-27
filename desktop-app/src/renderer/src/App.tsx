import { Link, useMatch } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
import { Box, Container, Group, MantineProvider, Title } from '@mantine/core'
import { QueryProvider } from '@/components/QueryProvider'
import HeaderNav from '@/components/HeaderNav'
import SettingsModal from '@/components/SettingsModal'
import OdooNavigateModal from '@/components/OdooNavigateModal'
import CasesWorkspace from '@/components/CasesWorkspace'
import { CaseTabsProvider } from '@/lib/caseWorkspace'
import { SettingsProvider, useSettings } from '@/lib/settings'
import { AppRoutes } from './routes'
import { theme } from './theme'

function Shell(): React.JSX.Element {
  const { isConfigured, loading, settings } = useSettings()
  const matchList = useMatch('/')
  const matchCase = useMatch('/helpdesk.ticket/:id')
  const isCasesRoute = !!(matchList || matchCase)

  return (
    <QueryProvider>
      <Box
        py="md"
        style={{
          borderBottom: '1px solid var(--mantine-color-gray-8)',
          position: 'relative',
          zIndex: 200
        }}
      >
        <header>
          <Container size="xl">
            <div
              style={{
                display: 'grid',
                gridTemplateColumns: '1fr auto 1fr',
                alignItems: 'center'
              }}
            >
              <Group>
                <Link to="/">
                  <img src="./logo.svg" alt="Snappy" style={{ height: 60 }} />
                </Link>
              </Group>
              <HeaderNav hasDevOpsToken={Boolean(settings?.devopsPat)} />
              <Group justify="flex-end">
                <SettingsModal />
              </Group>
            </div>
          </Container>
        </header>
      </Box>
      {!loading && !isConfigured && (
        <Box
          style={{
            position: 'fixed',
            inset: 0,
            zIndex: 100,
            backgroundColor: 'rgba(0, 0, 0, 0.75)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            flexDirection: 'column',
            gap: '1rem'
          }}
        >
          <Title order={2} c="white">
            Please Configure Your Settings
          </Title>
          <Title order={4} c="dimmed">
            Click the settings icon (⚙️) in the top right to configure your credentials.
          </Title>
        </Box>
      )}
      <OdooNavigateModal />
      <ToastContainer position="bottom-right" />
      {isConfigured && (
        <CaseTabsProvider>
          <div style={{ display: isCasesRoute ? 'block' : 'none' }}>
            <CasesWorkspace />
          </div>
          <div style={{ display: isCasesRoute ? 'none' : 'block' }}>
            <AppRoutes />
          </div>
        </CaseTabsProvider>
      )}
    </QueryProvider>
  )
}

function App(): React.JSX.Element {
  return (
    <MantineProvider theme={theme} defaultColorScheme="dark">
      <SettingsProvider>
        <Shell />
      </SettingsProvider>
    </MantineProvider>
  )
}

export default App
