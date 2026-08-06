import { useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import { IconAlertTriangle, IconEye } from '@tabler/icons-react'
import { useInfiniteQuery } from '@tanstack/react-query'
import {
  ActionIcon,
  Alert,
  Badge,
  Center,
  Container,
  Group,
  Loader,
  Stack,
  Table,
  Text,
  Tooltip
} from '@mantine/core'
import UiCard from '@/components/UiCard'
import SymphonyFilters from '@/components/SymphonyFilters'
import {
  EMPTY_SYMPHONY_FILTERS,
  toRequestTreeQuery,
  toSweepListFilter,
  type SymphonyFilterState
} from '@/components/SymphonyFilters/types'
import { useSweepActions } from '@/lib/symphonyDeepSearch'
import { useCaseTabs } from '@/lib/useCaseTabs'
import { useInfiniteScroll } from '@/hooks/useInfiniteScroll'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { getRequestTree, type SymphonyRequestRow } from '@/lib/symphony-api'
import { formatSymphonyTimestamp } from '@/lib/symphonyDates'
import { tabPath } from '@/lib/useCaseTabs'

const PAGE_SIZE = 200

/** The server's iconColor is a CSS fragment (`color:green;`), not a Mantine hue. */
function statusColor(row: SymphonyRequestRow): string {
  const raw = row.iconConfig?.iconColor ?? ''
  if (raw.includes('green')) return 'green'
  if (raw.includes('red')) return 'red'
  if (raw.includes('orange')) return 'orange'
  if (raw.includes('blue')) return 'blue'
  if (raw.includes('gray') || raw.includes('grey')) return 'gray'
  return row.status === 'FAILED' ? 'red' : row.status === 'COMPLETED' ? 'green' : 'blue'
}

type Props = {
  isActive?: boolean
}

export default function SymphonyRequests({ isActive }: Props): React.JSX.Element {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [filters, setFilters] = useState<SymphonyFilterState>(EMPTY_SYMPHONY_FILTERS)
  const [createError, setCreateError] = useState<string | null>(null)
  const sentinelRef = useRef<HTMLDivElement>(null)
  const { openTab } = useCaseTabs()
  const { create } = useSweepActions()

  useDocumentTitle('Symphony', isActive)

  // -------------------------------------
  // Functions
  // -------------------------------------

  // The job is persisted BEFORE the tab opens: that's what gives the tab a
  // stable URL identity and makes the sweep resumable. A "new unsaved" deep
  // search would break both.
  async function handleDeepSearch(draft: SymphonyFilterState): Promise<void> {
    setCreateError(null)
    try {
      const job = await create({
        name: draft.processKey ? `${draft.processKey} search` : 'Deep search',
        // Starts with one blank condition so the sweep page opens ready to fill in.
        predicate: {
          clauses: [
            {
              id: 'clause-0',
              name: { op: 'contains', value: '' },
              value: { op: 'contains', value: '' }
            }
          ],
          mode: 'all' as const,
          caseSensitive: false
        },
        filter: toSweepListFilter(draft)
      })
      openTab({ kind: 'symphony-deep-search', jobId: job.id }, job.name)
    } catch (err) {
      setCreateError(err instanceof Error ? err.message : String(err))
    }
  }

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data, isLoading, isError, error, fetchNextPage, hasNextPage, isFetchingNextPage } =
    useInfiniteQuery({
      queryKey: ['symphony', 'requests', filters],
      // recordsLoaded is an offset, not a page number.
      queryFn: ({ pageParam }) => getRequestTree(toRequestTreeQuery(filters, PAGE_SIZE, pageParam)),
      getNextPageParam: (lastPage, allPages) =>
        lastPage.moreRecords ? allPages.length * PAGE_SIZE : undefined,
      initialPageParam: 0,
      retry: false
    })

  useInfiniteScroll({ sentinelRef, hasNextPage, isFetchingNextPage, fetchNextPage })

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const pages = data?.pages ?? []
  const rows = pages.flatMap((p) => p.rows)
  const lastPage = pages[pages.length - 1]
  // The server refuses to enumerate past maximumRecordsNumber (10000), so a
  // broad filter silently truncates unless we say so.
  const truncated = Boolean(lastPage?.tableLimit)
  const cap = lastPage?.maximumRecordsNumber

  return (
    <Container size="xl" py="sm">
      <Stack gap="md">
        <SymphonyFilters value={filters} onApply={setFilters} onDeepSearch={handleDeepSearch} />

        {createError && (
          <Alert color="red" icon={<IconAlertTriangle size={16} />} title="Could not start a sweep">
            {createError}
          </Alert>
        )}

        {isError && (
          <Alert color="red" icon={<IconAlertTriangle size={16} />} title="Request failed">
            {(error as Error)?.message ?? 'Unknown error'}
          </Alert>
        )}

        {truncated && (
          <Alert color="yellow" icon={<IconAlertTriangle size={16} />}>
            The server stopped enumerating at {cap?.toLocaleString()} results. Narrow the date range
            or add a process key to see everything that matches.
          </Alert>
        )}

        <UiCard
          title="Requests"
          rightElement={
            <Text size="xs" c="dimmed">
              {rows.length} loaded
              {hasNextPage ? '+' : ''}
            </Text>
          }
        >
          <Table striped highlightOnHover>
            <Table.Thead>
              <Table.Tr>
                <Table.Th>Status</Table.Th>
                <Table.Th>Process Key</Table.Th>
                <Table.Th>Request Id</Table.Th>
                <Table.Th>Received</Table.Th>
                <Table.Th>Children</Table.Th>
                <Table.Th />
              </Table.Tr>
            </Table.Thead>
            <Table.Tbody>
              {rows.map((row) => (
                <Table.Tr key={row.requestId}>
                  <Table.Td>
                    <Group gap={4} wrap="nowrap">
                      <Badge color={statusColor(row)} variant="light">
                        {row.status}
                      </Badge>
                      {row.deadJob && (
                        <Badge color="grape" variant="outline">
                          dead
                        </Badge>
                      )}
                    </Group>
                  </Table.Td>
                  <Table.Td>
                    <Text size="sm">{row.processKey}</Text>
                  </Table.Td>
                  <Table.Td>
                    <Tooltip label={row.requestId}>
                      <Text size="xs" ff="monospace">
                        {row.requestId.slice(0, 16)}…
                      </Text>
                    </Tooltip>
                  </Table.Td>
                  <Table.Td>
                    <Text size="xs">{formatSymphonyTimestamp(row.createdDate)}</Text>
                  </Table.Td>
                  <Table.Td>
                    {row.hasChilds && (
                      <Badge variant="default">{row.childs > 0 ? row.childs : '›'}</Badge>
                    )}
                  </Table.Td>
                  <Table.Td>
                    <ActionIcon
                      component={Link}
                      variant="subtle"
                      to={tabPath({
                        kind: 'symphony-request',
                        requestId: row.requestId,
                        processId: row.processId
                      })}
                    >
                      <IconEye size={16} />
                    </ActionIcon>
                  </Table.Td>
                </Table.Tr>
              ))}
            </Table.Tbody>
          </Table>

          {!isLoading && rows.length === 0 && (
            <Center py="lg">
              <Text c="dimmed" size="sm">
                No requests match these filters.
              </Text>
            </Center>
          )}

          {(isLoading || isFetchingNextPage) && (
            <Center py="md">
              <Loader size="sm" />
            </Center>
          )}

          <div ref={sentinelRef} style={{ height: '1px' }} />
        </UiCard>
      </Stack>
    </Container>
  )
}
