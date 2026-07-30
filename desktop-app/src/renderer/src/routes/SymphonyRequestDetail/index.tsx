import { IconAlertTriangle, IconInfoCircle } from '@tabler/icons-react'
import { useQuery } from '@tanstack/react-query'
import {
  Alert,
  Badge,
  Container,
  Grid,
  Group,
  Loader,
  Space,
  Text,
  Title,
  Tooltip
} from '@mantine/core'
import SymphonyActivities from '@/components/SymphonyActivities'
import SymphonyVariables from '@/components/SymphonyVariables'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { getRequestTree } from '@/lib/symphony-api'
import { useResolvedTabName, useSymphonyVariables } from '@/lib/symphonyDetail'
import { formatSymphonyTimestamp } from '@/lib/symphonyDates'
import { NO_PROCESS_ID } from '@/lib/useCaseTabs'

type Props = {
  requestId: string
  processId: string
  isActive?: boolean
  onNameResolved?: (name: string) => void
}

export default function SymphonyRequestDetail({
  requestId,
  processId,
  isActive = false,
  onNameResolved
}: Props): React.JSX.Element {
  // -------------------------------------
  // Queries
  // -------------------------------------

  // The list row already carries everything in the header, so this only runs
  // when the tab was opened without one — a restored deep link, or a click on an
  // execution-tree child node, whose HTML has no processId.
  const needsLookup = !processId || processId === NO_PROCESS_ID
  const {
    data: row,
    isError,
    error,
    isFetching,
    isFetched
  } = useQuery({
    queryKey: ['symphony', 'request', requestId],
    queryFn: async () => {
      // Deliberately permissive: this looks up ONE already-known request, so it
      // must find it whatever its state — including if it is a dead job.
      // No status filter and no deadJob: both are allowlists that drop rows.
      // Filtering by the five known statuses hid a RESUBMIT request entirely,
      // which is what made an existing process look like it did not exist.
      const base = {
        pageSize: '1',
        sorters: [{ dir: 'desc' as const, field: 'createdDate' }]
      }
      const byRequest = await getRequestTree({ ...base, requestId })
      if (byRequest.rows[0]) {
        return byRequest.rows[0]
      }
      // Odoo's symphony.process stores a single "Process ID" that may be either a
      // request id or a process-instance id, and nothing records which. So fall
      // back to the other lookup rather than showing an empty page.
      const byProcess = await getRequestTree({ ...base, processId: requestId })
      return byProcess.rows[0] ?? null
    },
    enabled: isActive || needsLookup,
    staleTime: 60 * 1000,
    retry: false
  })

  // -------------------------------------
  // Effects
  // -------------------------------------

  const lookupDone = isFetched && !isFetching
  // No request row does NOT mean no process. A long-running process instance can
  // exist with variables and activities while having no row in the request tree
  // (verified: id aB2WC26845281-… returns 0 rows from getRequestTree by either
  // requestId or processId, yet has 59 variables and 31 activities). So once the
  // lookup comes back empty, fall back to treating the id as a process instance
  // rather than showing nothing.
  const noRequestRow = needsLookup && lookupDone && !row && !isError
  const resolvedProcessId = needsLookup
    ? (row?.processId ?? (noRequestRow ? requestId : null))
    : processId
  const isResolving = needsLookup && !row && !isError && !lookupDone

  // A process instance with no request row still names itself: its own variables
  // carry `processKey` and the originating `requestId`. Same query key as the
  // variables card, so this shares that fetch rather than repeating it.
  const { data: variables } = useSymphonyVariables(resolvedProcessId, isActive)
  const varValue = (name: string): string | null =>
    variables?.find((v) => v.varName === name)?.varValue || null
  const processKey = row?.processKey ?? (noRequestRow ? varValue('processKey') : null)
  const originRequestId = noRequestRow ? varValue('requestId') : null

  useDocumentTitle(processKey ? `${processKey} — Symphony` : 'Symphony request', isActive)

  // Feeds the tab strip's auto-title, same contract as CaseDetail.
  useResolvedTabName(processKey ?? undefined, onNameResolved)

  return (
    <Container size="xl" py="md">
      <Group justify="space-between" align="start">
        <div>
          <Title fz={24}>{processKey ?? 'Symphony request'}</Title>
          <Group gap="xs" mt={4}>
            {row && (
              <Badge
                color={
                  row.status === 'FAILED' ? 'red' : row.status === 'COMPLETED' ? 'green' : 'blue'
                }
                variant="light"
              >
                {row.status}
              </Badge>
            )}
            {row?.deadJob && (
              <Badge color="grape" variant="outline">
                dead job
              </Badge>
            )}
            <Tooltip label="Request id">
              <Text size="xs" c="dimmed" ff="monospace">
                {row?.requestId ?? requestId}
              </Text>
            </Tooltip>
            {resolvedProcessId && (
              <Tooltip
                label={noRequestRow ? 'Process instance id (read directly)' : 'Process instance id'}
              >
                <Text size="xs" c="dimmed" ff="monospace">
                  {resolvedProcessId}
                </Text>
              </Tooltip>
            )}
          </Group>
          {row && (
            <Text size="xs" c="dimmed" mt={2}>
              Received {formatSymphonyTimestamp(row.createdDate, 'D/M/YY HH:mm:ss.SSS')} · last
              modified {formatSymphonyTimestamp(row.lastModifiedDate, 'D/M/YY HH:mm:ss.SSS')}
            </Text>
          )}
        </div>
      </Group>

      <Space h="md" />

      {isError && (
        <>
          <Alert color="red" icon={<IconAlertTriangle size={16} />} title="Lookup failed">
            {(error as Error)?.message ?? 'Could not load this request'}
          </Alert>
          <Space h="md" />
        </>
      )}

      {isResolving && (
        <>
          {/* Progress, not a problem — so no warning styling. */}
          <Group gap="xs">
            <Loader size="xs" />
            <Text size="sm" c="dimmed">
              Looking up the process instance for this id…
            </Text>
          </Group>
          <Space h="md" />
        </>
      )}

      {noRequestRow && (
        <>
          <Alert color="gray" icon={<IconInfoCircle size={16} />} title="No request record">
            Symphony&apos;s request list has no entry for this id, so there is no status or timing
            to show. It is being read as a process instance instead — long-running processes exist
            without a request row.
            {originRequestId
              ? ` Its variables name the originating request as ${originRequestId}.`
              : ' If the cards below are empty too, the run is not in Symphony at all.'}
          </Alert>
          <Space h="md" />
        </>
      )}

      <Grid gutter="md">
        <Grid.Col span={{ base: 12, lg: 8 }}>
          {/* `pending` keeps the cards from asserting "none recorded" before they
              even have a process instance to ask about. */}
          <SymphonyVariables
            processInstanceId={resolvedProcessId}
            isActive={isActive}
            pending={isResolving}
          />
        </Grid.Col>
        <Grid.Col span={{ base: 12, lg: 4 }}>
          <SymphonyActivities
            processInstanceId={resolvedProcessId}
            isActive={isActive}
            pending={isResolving}
          />
        </Grid.Col>
      </Grid>
    </Container>
  )
}
