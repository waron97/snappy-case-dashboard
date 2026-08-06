import { useState } from 'react'
import { Link } from 'react-router-dom'
import { IconAlertTriangle, IconChevronRight, IconEye, IconInfoCircle } from '@tabler/icons-react'
import { useQuery } from '@tanstack/react-query'
import {
  ActionIcon,
  Alert,
  Badge,
  Center,
  Group,
  Loader,
  Stack,
  Text,
  Tooltip,
  UnstyledButton
} from '@mantine/core'
import { useSymphonyExecutionTree } from '@/lib/symphonyDetail'
import { getExecutionTreeNode, type SymphonyExecutionNode } from '@/lib/symphony-api'
import { parseExecutionTree } from '@/lib/symphonyDetailHtml'
import { NO_PROCESS_ID, tabPath } from '@/lib/useCaseTabs'

const FIVE_MINUTES = 5 * 60 * 1000

type Props = {
  /** The tree root's request id — null when there is no request row to walk
   *  a tree from (a process-instance-only view, or still resolving). */
  requestId: string | null
  processKey: string | null
  isActive: boolean
  pending?: boolean
}

function statusColor(status: string | null): string {
  switch (status) {
    case 'COMPLETED':
      return 'green'
    case 'FAILED':
      return 'red'
    case 'WORKING':
      return 'blue'
    default:
      return 'gray'
  }
}

type NodeProps = {
  node: SymphonyExecutionNode
  rootId: string
  processKey: string | null
}

function SubprocessNode({ node, rootId, processKey }: NodeProps): React.JSX.Element {
  const [expanded, setExpanded] = useState(false)

  // Only the first expand fetches — a node whose children were already
  // embedded (rare, but the parser doesn't rule it out) skips the network call.
  const shouldFetch = expanded && node.children.length === 0

  const { data, isLoading, isError } = useQuery({
    queryKey: ['symphony', 'executionTreeNode', node.id],
    queryFn: async () => {
      const html = await getExecutionTreeNode(node.id, {
        processKey: processKey ?? '',
        rootId,
        idSelected: rootId
      })
      return parseExecutionTree(html)
    },
    enabled: shouldFetch && Boolean(processKey),
    staleTime: FIVE_MINUTES,
    gcTime: FIVE_MINUTES,
    retry: false
  })

  // The full subtree, leaves included — this tab mirrors the legacy
  // Executions tree, not a subprocess-only summary. Every node id, leaf or
  // not, is its own process/task instance and opens fine as a
  // symphony-request tab; `hasChildren` only says whether the *tree* goes
  // deeper here, not whether the node itself is a real request.
  const children = data?.children.length ? data.children : node.children

  return (
    <Stack gap={2}>
      <Group gap={6} wrap="nowrap" justify="space-between">
        <Group gap={6} wrap="nowrap" style={{ minWidth: 0 }}>
          {node.hasChildren ? (
            <UnstyledButton onClick={() => setExpanded((v) => !v)} style={{ display: 'flex' }}>
              <IconChevronRight
                size={14}
                style={{
                  transform: expanded ? 'rotate(90deg)' : undefined,
                  transition: 'transform 100ms ease',
                  flexShrink: 0
                }}
              />
            </UnstyledButton>
          ) : (
            <div style={{ width: 14, flexShrink: 0 }} />
          )}
          <Tooltip label={node.name}>
            <Text size="xs" truncate>
              {node.name}
            </Text>
          </Tooltip>
        </Group>
        <Group gap={4} wrap="nowrap" style={{ flexShrink: 0 }}>
          {node.status && (
            <Badge size="xs" color={statusColor(node.status)} variant="light">
              {node.status}
            </Badge>
          )}
          <ActionIcon
            component={Link}
            variant="subtle"
            size="sm"
            to={tabPath({
              kind: 'symphony-request',
              requestId: node.id,
              processId: NO_PROCESS_ID
            })}
          >
            <IconEye size={14} />
          </ActionIcon>
        </Group>
      </Group>

      {expanded && (
        <Stack gap={2} pl={20}>
          {isError && (
            <Text size="xs" c="red">
              Failed to load children
            </Text>
          )}
          {isLoading && (
            <Center py={4}>
              <Loader size="xs" />
            </Center>
          )}
          {!isLoading &&
            !isError &&
            children.map((child) => (
              <SubprocessNode key={child.id} node={child} rootId={rootId} processKey={processKey} />
            ))}
          {!isLoading && !isError && children.length === 0 && (
            <Text size="xs" c="dimmed">
              No steps recorded
            </Text>
          )}
        </Stack>
      )}
    </Stack>
  )
}

export default function SymphonyChildProcesses({
  requestId,
  processKey,
  isActive,
  pending = false
}: Props): React.JSX.Element {
  const { data: root, isLoading, isError, error } = useSymphonyExecutionTree(requestId, isActive)

  const children = root?.children ?? []

  return (
    <Stack gap="xs">
      {!requestId && !pending && (
        <Alert color="gray" icon={<IconInfoCircle size={16} />}>
          No request record for this process — the execution tree needs a request id, which a
          process-instance-only view does not have.
        </Alert>
      )}

      {isError && (
        <Alert color="red" icon={<IconAlertTriangle size={16} />}>
          {(error as Error)?.message ?? 'Failed to load the execution tree'}
        </Alert>
      )}

      {(isLoading || pending) && requestId && (
        <Center py="lg">
          <Loader size="sm" />
        </Center>
      )}

      {!isLoading && !pending && !isError && requestId && (
        <>
          {children.length === 0 ? (
            <Center py="lg">
              <Text size="sm" c="dimmed">
                No executions recorded
              </Text>
            </Center>
          ) : (
            <Stack gap={4}>
              {children.map((node) => (
                <SubprocessNode
                  key={node.id}
                  node={node}
                  rootId={requestId}
                  processKey={processKey}
                />
              ))}
            </Stack>
          )}
        </>
      )}
    </Stack>
  )
}
