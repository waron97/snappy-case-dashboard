import { Link, useLocation } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
import { ActionIcon, Box, Container, Group, MantineProvider, Title } from '@mantine/core'
import { IconSettings } from '@tabler/icons-react'
import { QueryProvider } from '@/components/QueryProvider'
import HeaderNav from '@/components/HeaderNav'
import ProfileSwitcher from '@/components/ProfileSwitcher'
import OdooNavigateModal from '@/components/OdooNavigateModal'
import UpdateNotifier from '@/components/UpdateNotifier'
import CasesWorkspace from '@/components/CasesWorkspace'
import ErrorBoundary from '@/components/ErrorBoundary'
import SymphonyCatalogWarmup from '@/components/SymphonyCatalogWarmup'
import { CaseTabsProvider } from '@/lib/caseWorkspace'
import { deferredUiPrefColorSchemeManager } from '@/lib/colorSchemeManager'
import { SettingsProvider, useSettings } from '@/lib/settings'
import SettingsPage from '@/components/SettingsPage'
import { theme } from './theme'

const colorSchemeManager = deferredUiPrefColorSchemeManager()

function Shell(): React.JSX.Element {
  const { isConfigured, loading, activeProfile } = useSettings()
  // Every path except this one maps to a tab; TAB_ROUTES in
  // lib/caseWorkspaceContext.ts is the app's only route table.
  const isSettings = useLocation().pathname === '/settings'

  return (
    <QueryProvider>
      {/* Wraps the header too: HeaderNav opens tabs directly (a <Link> can't
          open a second RIP logs tab — the URL wouldn't change). Mounting it
          while unconfigured is harmless, it holds state and reads one uiPref;
          what stays gated on isConfigured is CasesWorkspace, so a first-run
          user still fires no Odoo queries with blank credentials. */}
      <CaseTabsProvider>
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
                  <ActionIcon
                    component={Link}
                    to="/settings"
                    variant="subtle"
                    size="lg"
                    color="gray"
                  >
                    <IconSettings size={20} />
                  </ActionIcon>
                </Group>
              </div>
            </Container>
          </header>
        </Box>
        {isSettings ? (
          <ErrorBoundary>
            <SettingsPage />
          </ErrorBoundary>
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
              <>
                <SymphonyCatalogWarmup />
                {/* Unmounted rather than hidden while /settings is open: every open
                  case tab polls Odoo every 3-30s, and those polls aren't gated on
                  tab activity, so hiding it would keep them running against
                  half-edited credentials. The tab *list* survives regardless —
                  it lives in the provider above. */}
                <ErrorBoundary>
                  <CasesWorkspace />
                </ErrorBoundary>
              </>
            )}
          </>
        )}
      </CaseTabsProvider>
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
