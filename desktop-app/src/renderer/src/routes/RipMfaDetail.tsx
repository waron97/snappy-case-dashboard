import { Link } from 'react-router-dom'
import { IconCode } from '@tabler/icons-react'
import { odooRead } from '@/lib/odoo-api'
import { useQuery } from '@tanstack/react-query'
import {
  Anchor,
  Button,
  Center,
  Container,
  Grid,
  Group,
  Loader,
  Space,
  Stack,
  Text,
  Title
} from '@mantine/core'
import MfaCode from '@/components/MfaCode'
import MfaMetadata from '@/components/MfaMetadata'
import MfaRecentCalls from '@/components/MfaRecentCalls'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { useResolvedTabName, useVisitedGate } from '@/lib/tabActive'
import { useRefreshQueries } from '@/lib/refresh'
import { useSettings } from '@/lib/settings'

type Props = {
  id: number
  isActive?: boolean
  onNameResolved?: (name: string) => void
}

export default function MFARecord({ id, isActive = false, onNameResolved }: Props) {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  // `id` arrives from the tab payload, not useParams: this renders outside
  // <Routes>, so useParams would return {} and every read would hit NaN.
  const { activeProfile: settings } = useSettings()
  const visited = useVisitedGate(isActive)

  // -------------------------------------
  // Queries
  // -------------------------------------

  // Prefix covers the whole tab — title here, plus MfaCode's 'code',
  // MfaMetadata's 'metadata' and MfaRecentCalls' 'recent-calls'.
  useRefreshQueries(['mfa', id])

  const { data, isLoading, error } = useQuery({
    queryKey: ['mfa', id, 'title'],
    queryFn: () => odooRead('rip.model.function.access', [id], ['name', 'model_name']),
    enabled: visited
  })

  // -------------------------------------
  // Effects
  // -------------------------------------

  const titleRecord = data?.[0]
  useDocumentTitle(titleRecord ? `MFA ${titleRecord.name}` : undefined, isActive)
  useResolvedTabName(
    titleRecord ? `${titleRecord.model_name}/${titleRecord.name}` : undefined,
    onNameResolved
  )

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // Nothing below this point mounts until the tab has been looked at — which is
  // what keeps MfaCode's CodeMirror instance out of a restored-but-unvisited tab.
  if (!visited || isLoading) {
    return (
      <Center py="xl">
        <Loader />
      </Center>
    )
  }

  const record = data?.[0]

  if (!record || error) {
    return (
      <Container size="lg" py="xl">
        <Center py="xl">
          <Text c="red">
            Failed to load function: {error instanceof Error ? error.message : 'Not found'}
          </Text>
        </Center>
      </Container>
    )
  }

  // -------------------------------------

  return (
    <Container size="xl" py="md">
      <Group gap="md" justify="space-between">
        <Title fz={28}>
          {record.model_name}/{record.name} (#{id})
        </Title>
        <Group gap="sm">
          <Anchor
            href={`${settings?.odooUrl}/web#id=${id}&model=rip.model.function.access&view_type=form`}
            target="_blank"
          >
            <Button bg="#714B67">ODOO</Button>
          </Anchor>
          <Link to={`/full-field-config/rip.model.function.access/${id}`}>
            <Button>
              <IconCode />
            </Button>
          </Link>
        </Group>
      </Group>

      <Space h={32} />

      <Grid gutter="md">
        <Grid.Col span={8}>
          <MfaCode id={id} />
        </Grid.Col>
        <Grid.Col span={4}>
          <Stack gap="md">
            <MfaMetadata id={id} />
            <MfaRecentCalls id={id} />
          </Stack>
        </Grid.Col>
      </Grid>
    </Container>
  )
}
