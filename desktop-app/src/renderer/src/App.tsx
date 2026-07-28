import { Link, useMatch } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
import { ActionIcon, Box, Container, Group, MantineProvider, Title } from '@mantine/core'
import { IconSettings } from '@tabler/icons-react'
import { QueryProvider } from '@/components/QueryProvider'
import HeaderNav from '@/components/HeaderNav'
import ProfileSwitcher from '@/components/ProfileSwitcher'
import OdooNavigateModal from '@/components/OdooNavigateModal'
import UpdateNotifier from '@/components/UpdateNotifier'
import CasesWorkspace from '@/components/CasesWorkspace'
import { CaseTabsProvider } from '@/lib/caseWorkspace'
import { deferredUiPrefColorSchemeManager } from '@/lib/colorSchemeManager'
import { SettingsProvider, useSettings } from '@/lib/settings'
import { AppRoutes } from './routes'
import SettingsPage from './routes/Settings'
import { theme } from './theme'

const colorSchemeManager = deferredUiPrefColorSchemeManager()

function Shell(): React.JSX.Element {
  const { isConfigured, loading, activeProfile } = useSettings()
  const matchList = useMatch('/')
  const matchCase = useMatch('/helpdesk.ticket/:id')
  const matchFieldConfig = useMatch('/full-field-config/:model/:record')
  const matchSettings = useMatch('/settings')
  const isCasesRoute = !!(matchList || matchCase || matchFieldConfig)

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
              <HeaderNav hasDevOpsToken={Boolean(activeProfile?.devopsPat)} />
              <Group justify="flex-end" gap="xs">
                <ProfileSwitcher />
                <ActionIcon component={Link} to="/settings" variant="subtle" size="lg" color="gray">
                  <IconSettings size={20} />
                </ActionIcon>
              </Group>
            </div>
          </Container>
        </header>
      </Box>
      {matchSettings ? (
        <SettingsPage />
      ) : (
        <>
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
        </>
      )}
      <ToastContainer position="bottom-right" />
      <UpdateNotifier />
    </QueryProvider>
  )
}

function App(): React.JSX.Element {
  return (
    <MantineProvider
      theme={theme}
      defaultColorScheme="dark"
      colorSchemeManager={colorSchemeManager}
    >
      <SettingsProvider>
        <Shell />
      </SettingsProvider>
    </MantineProvider>
  )
}

export default App
