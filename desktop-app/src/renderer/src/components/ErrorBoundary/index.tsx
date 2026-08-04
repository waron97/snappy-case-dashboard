import { Component, type ReactNode } from 'react'
import { Alert, Button, Center, Code, Group, Stack, Text } from '@mantine/core'
import { IconAlertTriangle, IconArrowLeft, IconRefresh, IconReload } from '@tabler/icons-react'

type Props = {
  children: ReactNode
  /** Extra recovery action shown alongside Retry/Reload, e.g. "Close tab" or "Back to list". */
  onRecover?: () => void
  recoverLabel?: string
}

type State = {
  error: Error | null
}

// Class component: componentDidCatch/getDerivedStateFromError have no hook
// equivalent, so this is the one place in the app that can't be a function.
export default class ErrorBoundary extends Component<Props, State> {
  state: State = { error: null }

  static getDerivedStateFromError(error: Error): State {
    return { error }
  }

  componentDidCatch(error: Error, info: React.ErrorInfo): void {
    console.error('ErrorBoundary caught:', error, info.componentStack)
  }

  reset = (): void => {
    this.setState({ error: null })
  }

  render(): ReactNode {
    const { error } = this.state
    if (!error) return this.props.children

    return (
      <Center h="100%" mih={300} p="xl">
        <Stack maw={640} w="100%">
          <Alert color="red" icon={<IconAlertTriangle size={16} />} title="Something crashed">
            <Stack gap="xs">
              <Text size="sm">{error.message || 'Unknown error'}</Text>
              <Code block style={{ maxHeight: 160, overflow: 'auto', fontSize: 11 }}>
                {error.stack ?? String(error)}
              </Code>
            </Stack>
          </Alert>
          <Group>
            <Button size="xs" leftSection={<IconRefresh size={14} />} onClick={this.reset}>
              Try again
            </Button>
            {this.props.onRecover && (
              <Button
                size="xs"
                variant="light"
                leftSection={<IconArrowLeft size={14} />}
                onClick={() => {
                  this.props.onRecover?.()
                  this.reset()
                }}
              >
                {this.props.recoverLabel ?? 'Go back'}
              </Button>
            )}
            <Button
              size="xs"
              variant="subtle"
              color="gray"
              leftSection={<IconReload size={14} />}
              onClick={() => window.location.reload()}
            >
              Reload app
            </Button>
          </Group>
        </Stack>
      </Center>
    )
  }
}
