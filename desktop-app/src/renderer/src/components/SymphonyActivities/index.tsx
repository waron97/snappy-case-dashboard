import { useMemo, useState } from 'react'
import { IconAlertTriangle } from '@tabler/icons-react'
import {
  Alert,
  Badge,
  Box,
  Center,
  Group,
  Loader,
  ScrollArea,
  Stack,
  Switch,
  Tabs,
  Text,
  Tooltip
} from '@mantine/core'
import UiCard from '@/components/UiCard'
import SymphonyChildProcesses from '@/components/SymphonyChildProcesses'
import { useSymphonyActivities } from '@/lib/symphonyDetail'
import {
  formatDuration,
  formatSymphonyTimestamp,
  symphonyTimestampValue
} from '@/lib/symphonyDates'
import type { SymphonyActivity } from '@/lib/symphony-api'

type Props = {
  processInstanceId: string | null
  /** The tree root's request id, for the Child processes tab — null when
   *  there's no request row to walk a tree from. */
  requestId: string | null
  processKey: string | null
  isActive: boolean
  /** The caller is still resolving which process instance to ask about, so an
   *  empty result here means "not known yet", not "none exist". */
  pending?: boolean
}

/** Anything slow, anything that failed, and the structural milestones. */
const NOTABLE_TYPES = new Set([
  'startEvent',
  'endEvent',
  'callActivity',
  'userTask',
  'serviceTask',
  'boundaryEvent',
  'intermediateCatchEvent',
  'intermediateThrowEvent',
  'errorEndEvent'
])
const SLOW_MS = 1000

type ActivityRun = {
  key: string
  activity: SymphonyActivity
  count: number
  totalMs: number
  notable: boolean
}

function isNotable(activity: SymphonyActivity): boolean {
  if (Number(activity.durationInMillis) > SLOW_MS) return true
  if (activity.deleteReason) return true
  return NOTABLE_TYPES.has(activity.activityType)
}

/**
 * Symphony flows are loop-heavy — the legacy screenshot shows eight consecutive
 * BSP_ManageTask rows — so consecutive repeats of the same activity collapse
 * into one row with a xN badge. Typically takes ~95 rows down to ~35.
 */
function collapseRuns(activities: SymphonyActivity[]): ActivityRun[] {
  const runs: ActivityRun[] = []
  for (const activity of activities) {
    const previous = runs[runs.length - 1]
    const ms = Number(activity.durationInMillis) || 0
    if (previous && previous.activity.activityName === activity.activityName) {
      previous.count++
      previous.totalMs += ms
      previous.notable = previous.notable || isNotable(activity)
      continue
    }
    runs.push({
      key: `${activity.activityId}:${activity.startTime}:${runs.length}`,
      activity,
      count: 1,
      totalMs: ms,
      notable: isNotable(activity)
    })
  }
  return runs
}

export default function SymphonyActivities({
  processInstanceId,
  requestId,
  processKey,
  isActive,
  pending = false
}: Props): React.JSX.Element {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const [showAll, setShowAll] = useState(false)

  // -------------------------------------
  // Queries
  // -------------------------------------

  const {
    data: activities,
    isLoading,
    isError,
    error
  } = useSymphonyActivities(processInstanceId, isActive)

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  // Memoized so the empty-array fallback doesn't churn the run-collapsing memo.
  const all = useMemo(() => activities ?? [], [activities])

  const { runs, hidden, spanMs, maxMs } = useMemo(() => {
    // The API sorts startTime desc; read the flow forwards.
    const chronological = [...all].sort(
      (a, b) => symphonyTimestampValue(a.startTime) - symphonyTimestampValue(b.startTime)
    )
    const allRuns = collapseRuns(chronological)
    const visible = showAll ? allRuns : allRuns.filter((r) => r.notable)

    const times = chronological
      .flatMap((a) => [symphonyTimestampValue(a.startTime), symphonyTimestampValue(a.endTime)])
      .filter((t) => Number.isFinite(t))
    const span = times.length ? Math.max(...times) - Math.min(...times) : 0

    return {
      runs: visible,
      hidden: allRuns.length - visible.length,
      spanMs: span,
      maxMs: Math.max(1, ...allRuns.map((r) => r.totalMs))
    }
  }, [all, showAll])

  return (
    <UiCard>
      <Tabs defaultValue="history" keepMounted={false}>
        <Tabs.List>
          <Tabs.Tab value="history">Activity history</Tabs.Tab>
          <Tabs.Tab value="children">Child processes</Tabs.Tab>
        </Tabs.List>

        <Tabs.Panel value="history" pt="xs">
          <Stack gap="xs">
            <Group justify="space-between">
              <Switch
                size="xs"
                label="Show all"
                checked={showAll}
                onChange={(e) => setShowAll(e.currentTarget.checked)}
              />
              <Group gap="xs">
                {!showAll && hidden > 0 && (
                  <Text size="xs" c="dimmed">
                    {hidden} routine hidden
                  </Text>
                )}
                <Text size="xs" c="dimmed">
                  {all.length} steps · {formatDuration(spanMs)}
                </Text>
              </Group>
            </Group>

            {isError && (
              <Alert color="red" icon={<IconAlertTriangle size={16} />}>
                {(error as Error)?.message ?? 'Failed to load activities'}
              </Alert>
            )}

            {(isLoading || pending) && (
              <Center py="lg">
                <Loader size="sm" />
              </Center>
            )}

            {!isLoading && !pending && !isError && (
              <ScrollArea.Autosize mah={640}>
                <Stack gap={2}>
                  {runs.map((run) => (
                    <Box
                      key={run.key}
                      px={6}
                      py={4}
                      style={{
                        borderRadius: 4,
                        borderLeft: `2px solid var(--mantine-color-${run.activity.deleteReason ? 'red' : run.totalMs > SLOW_MS ? 'yellow' : 'dark'}-5)`
                      }}
                    >
                      <Group gap={6} wrap="nowrap" justify="space-between">
                        <Group gap={6} wrap="nowrap" style={{ minWidth: 0 }}>
                          <Text size="xs" c="dimmed" ff="monospace" style={{ flexShrink: 0 }}>
                            {formatSymphonyTimestamp(run.activity.startTime, 'HH:mm:ss')}
                          </Text>
                          <Tooltip label={run.activity.activityName || run.activity.activityId}>
                            <Text size="xs" truncate>
                              {run.activity.activityName || run.activity.activityId}
                            </Text>
                          </Tooltip>
                          {run.count > 1 && (
                            <Badge size="xs" variant="light" style={{ flexShrink: 0 }}>
                              ×{run.count}
                            </Badge>
                          )}
                        </Group>
                        <Text size="xs" c="dimmed" style={{ flexShrink: 0 }}>
                          {formatDuration(run.totalMs)}
                        </Text>
                      </Group>
                      <Group gap={6} wrap="nowrap">
                        <Text size="xs" c="dimmed" truncate>
                          {run.activity.activityType}
                        </Text>
                        {run.activity.deleteReason && (
                          <Tooltip label={run.activity.deleteReason}>
                            <Badge size="xs" color="red" variant="light">
                              deleted
                            </Badge>
                          </Tooltip>
                        )}
                      </Group>
                      {/* Duration bar — makes "where did the time go" immediate. */}
                      <Box
                        mt={2}
                        h={2}
                        w={`${Math.max(1, (run.totalMs / maxMs) * 100)}%`}
                        bg={run.totalMs > SLOW_MS ? 'yellow.6' : 'gray.6'}
                      />
                    </Box>
                  ))}
                </Stack>

                {runs.length === 0 && (
                  <Center py="lg">
                    <Text size="sm" c="dimmed">
                      {all.length === 0
                        ? 'No activities recorded'
                        : 'Nothing notable — enable Show all'}
                    </Text>
                  </Center>
                )}
              </ScrollArea.Autosize>
            )}
          </Stack>
        </Tabs.Panel>

        <Tabs.Panel value="children" pt="xs">
          <SymphonyChildProcesses
            requestId={requestId}
            processKey={processKey}
            isActive={isActive}
            pending={pending}
          />
        </Tabs.Panel>
      </Tabs>
    </UiCard>
  )
}
