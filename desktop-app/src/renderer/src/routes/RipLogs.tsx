import dayjs from 'dayjs'
import { useRef, useState } from 'react'
import ReactJson from 'react-json-view'
import { odooSearchRead } from '@/lib/odoo-api'
import { IconEye } from '@tabler/icons-react'
import { useInfiniteQuery } from '@tanstack/react-query'
import {
  Badge,
  Button,
  Center,
  Container,
  Group,
  Loader,
  Modal,
  Stack,
  Table,
  Tabs,
  TagsInput,
  Text
} from '@mantine/core'
import { DateInput } from '@mantine/dates'
import RelationLink from '@/components/RelationLink'
import UiCard from '@/components/UiCard'
import { useInfiniteScroll } from '@/hooks/useInfiniteScroll'
import { constructOdooDomain } from '@/utils/odoo'

interface RipLog {
  id: number
  endpoint: string
  method: string
  status: number
  args: string
  content: string
  response_content: string
  create_date: string
}

const truncate = (str: string | undefined, max = 20) =>
  str && str.length > max ? `${str.slice(0, max)}…` : (str ?? '')

const parseJson = (str: string | undefined) => {
  if (!str) {
    return {}
  }
  try {
    return JSON.parse(str)
  } catch {
    return { raw: str }
  }
}

export default function RipLogs() {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [filters, setFilters] = useState<{
    endpoint: string[]
    args: string[]
    content: string[]
    method: string[]
    status: string[]
    response_content: string[]
    startDate: string | null
    endDate: string | null
  }>({
    endpoint: [],
    args: [],
    content: [],
    method: [],
    status: [],
    response_content: [],
    startDate: null,
    endDate: null
  })

  const [selected, setSelected] = useState<RipLog | null>(null)

  const sentinelRef = useRef<HTMLDivElement>(null)

  // -------------------------------------
  // Queries
  // -------------------------------------

  const { data, isLoading, isError, error, fetchNextPage, hasNextPage, isFetchingNextPage } =
    useInfiniteQuery({
      queryKey: ['rip.request.log', filters],
      queryFn: ({ pageParam = 0 }) =>
        odooSearchRead(
          'rip.request.log',
          [
            ...constructOdooDomain({
              endpoint: {
                operator: 'ilike',
                value: filters.endpoint
              },
              args: {
                operator: 'ilike',
                value: filters.args
              },
              content: {
                operator: 'ilike',
                value: filters.content
              },
              status: {
                operator: 'ilike',
                value: filters.status.map((s) => parseInt(s, 10))
              },
              method: {
                operator: 'ilike',
                value: filters.method
              },
              response_content: {
                operator: 'ilike',
                value: filters.response_content
              }
            }),
            ...(filters.startDate ? [['create_date', '>=', filters.startDate]] : []),
            ...(filters.endDate ? [['create_date', '<=', filters.endDate]] : [])
          ],
          [
            'id',
            'create_date',
            'endpoint',
            'method',
            'status',
            'args',
            'content',
            'response_content'
          ],
          pageParam,
          20,
          'create_date DESC'
        ),
      getNextPageParam: (lastPage, allPages) =>
        lastPage.length === 20 ? allPages.length * 20 : undefined,
      initialPageParam: 0
    })

  useInfiniteScroll({ sentinelRef, hasNextPage, isFetchingNextPage, fetchNextPage })

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const logs = data?.pages.flatMap((page) => page) ?? []

  const rows = logs.map((item: RipLog) => (
    <Table.Tr key={item.id}>
      <Table.Td>
        <RelationLink model="rip.request.log" pgId={item.id} name={item.endpoint} />
      </Table.Td>
      <Table.Td>{item.method}</Table.Td>
      <Table.Td>
        <Badge color={item.status >= 200 && item.status < 300 ? 'green' : 'red'}>
          {item.status}
        </Badge>
      </Table.Td>
      <Table.Td>{truncate(item.args)}</Table.Td>
      <Table.Td>{truncate(item.content)}</Table.Td>
      <Table.Td>{truncate(item.response_content)}</Table.Td>
      <Table.Td>{dayjs(item.create_date).format('D/M/YY HH:mm')}</Table.Td>
      <Table.Td>
        <Button onClick={() => setSelected(item)}>
          <IconEye size={18} />
        </Button>
      </Table.Td>
    </Table.Tr>
  ))

  // -------------------------------------

  if (isError) {
    return (
      <Container size="xl" py="xl">
        <Center py="xl">
          <Text c="red">
            Failed to load logs: {error instanceof Error ? error.message : 'Unknown error'}
          </Text>
        </Center>
      </Container>
    )
  }

  return (
    <Container size="xl" py="sm">
      <Stack gap="md" pt="md">
        <UiCard title="Filters">
          <Stack gap="sm">
            <Group grow>
              <TagsInput
                label="Endpoint"
                value={filters.endpoint}
                onChange={(endpoint: string[]) => setFilters({ ...filters, endpoint })}
              />
              <TagsInput
                label="Method"
                value={filters.method}
                onChange={(method: string[]) => setFilters({ ...filters, method })}
              />
              <TagsInput
                label="Status"
                value={filters.status}
                onChange={(status: string[]) => setFilters({ ...filters, status })}
              />
            </Group>
            <Group grow>
              <TagsInput
                label="Args"
                value={filters.args}
                onChange={(args: string[]) => setFilters({ ...filters, args })}
              />
              <TagsInput
                label="Content"
                value={filters.content}
                onChange={(content: string[]) => setFilters({ ...filters, content })}
              />
              <TagsInput
                label="Response Content"
                value={filters.response_content}
                onChange={(response_content: string[]) =>
                  setFilters({ ...filters, response_content })
                }
              />
            </Group>
            <Group grow>
              <DateInput
                label="Start date"
                value={filters.startDate}
                onChange={(v) => setFilters({ ...filters, startDate: v })}
                clearable
              />
              <DateInput
                label="End date"
                value={filters.endDate}
                onChange={(v) => setFilters({ ...filters, endDate: v })}
                clearable
              />
            </Group>
          </Stack>
        </UiCard>

        <Table striped highlightOnHover>
          <Table.Thead>
            <Table.Tr>
              <Table.Th>Endpoint</Table.Th>
              <Table.Th>Method</Table.Th>
              <Table.Th>Status</Table.Th>
              <Table.Th>Args</Table.Th>
              <Table.Th>Content</Table.Th>
              <Table.Th>Response Content</Table.Th>
              <Table.Th>Create Date</Table.Th>
              <Table.Th />
            </Table.Tr>
          </Table.Thead>
          <Table.Tbody>{rows}</Table.Tbody>
        </Table>

        <div ref={sentinelRef} style={{ height: '1px' }} />

        {(isLoading || isFetchingNextPage) && (
          <Center py="xl">
            <Loader size="sm" />
          </Center>
        )}
      </Stack>

      <Modal
        opened={!!selected}
        onClose={() => setSelected(null)}
        size="xl"
        title={selected?.endpoint}
      >
        {selected && (
          <Tabs defaultValue="general">
            <Tabs.List>
              <Tabs.Tab value="general">General</Tabs.Tab>
              <Tabs.Tab value="content">Content</Tabs.Tab>
              <Tabs.Tab value="response">Response Content</Tabs.Tab>
            </Tabs.List>

            <Tabs.Panel value="general" pt="md">
              <Stack gap="xs">
                <Text>
                  <strong>Endpoint:</strong> {selected.endpoint}
                </Text>
                <Text>
                  <strong>Method:</strong> {selected.method}
                </Text>
                <Group gap="xs" align="center">
                  <Text component="span">
                    <strong>Status:</strong>
                  </Text>
                  <Badge color={selected.status >= 200 && selected.status < 300 ? 'green' : 'red'}>
                    {selected.status}
                  </Badge>
                </Group>
                <Text>
                  <strong>Create Date:</strong> {dayjs(selected.create_date).format('D/M/YY HH:mm')}
                </Text>
                <Text style={{ wordBreak: 'break-all' }}>
                  <strong>Args:</strong> {selected.args}
                </Text>
              </Stack>
            </Tabs.Panel>

            <Tabs.Panel value="content" pt="md">
              <ReactJson src={parseJson(selected.content)} theme="monokai" />
            </Tabs.Panel>

            <Tabs.Panel value="response" pt="md">
              <ReactJson src={parseJson(selected.response_content)} theme="monokai" />
            </Tabs.Panel>
          </Tabs>
        )}
      </Modal>
    </Container>
  )
}
