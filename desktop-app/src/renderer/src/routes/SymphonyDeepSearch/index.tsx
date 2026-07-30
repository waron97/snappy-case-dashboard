import { useState } from 'react'
import { Link } from 'react-router-dom'
import {
  IconAlertTriangle,
  IconEye,
  IconPlayerPause,
  IconPlayerPlay,
  IconTrash
} from '@tabler/icons-react'
import {
  ActionIcon,
  Alert,
  Badge,
  Button,
  Center,
  Collapse,
  Container,
  Group,
  Loader,
  ScrollArea,
  Stack,
  Table,
  Text,
  TextInput,
  Title,
  Tooltip
} from '@mantine/core'
import UiCard from '@/components/UiCard'
import ClauseEditor from '@/routes/SymphonyDeepSearch/ClauseEditor'
import FilterFields from '@/components/SymphonyFilters/FilterFields'
import {
  fromSweepListFilter,
  toSweepListFilter,
  type SymphonyFilterState
} from '@/components/SymphonyFilters/types'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { formatSymphonyTimestamp } from '@/lib/symphonyDates'
import { tabPath } from '@/lib/useCaseTabs'
import {
  isClauseEmpty,
  sweepFilterKey,
  useSweep,
  useSweepActions,
  type SweepJob,
  type SweepListFilter,
  type SweepPredicate
} from '@/lib/symphonyDeepSearch'
import { useResolvedTabName } from '@/lib/symphonyDetail'

type Props = {
  jobId: string
  isActive?: boolean
  onNameResolved?: (name: string) => void
}

const STATUS_COLORS: Record<SweepJob['status'], string> = {
  draft: 'gray',
  queued: 'blue',
  running: 'blue',
  paused: 'yellow',
  done: 'green',
  error: 'red'
}

const PAUSE_REASONS: Record<string, string> = {
  user: 'paused by you',
  'app-quit': 'paused when Snappy closed',
  'profile-switch': 'paused because the profile changed',
  'server-errors': 'paused after repeated server errors',
  'not-configured': 'paused — profile not configured'
}

export default function SymphonyDeepSearch({
  jobId,
  isActive = false,
  onNameResolved
}: Props): React.JSX.Element {
  // -------------------------------------
  // Hooks
  // -------------------------------------

  const { data, isLoading, isError, error } = useSweep(jobId)
  const actions = useSweepActions()
  // Expanded by default: collapsed, the process/status fields read as absent.
  const [showFilter, setShowFilter] = useState(true)
  const [actionError, setActionError] = useState<string | null>(null)

  const job = data?.job ?? null
  const [draft, setDraft] = useState<SweepPredicate | null>(null)
  const [name, setName] = useState('')
  // null = "in sync with the persisted job"; set only once the user edits.
  const [filterDraft, setFilterDraft] = useState<SymphonyFilterState | null>(null)

  // Seed the form the first time this job's snapshot arrives. Keyed on job.id,
  // not on the predicate: progress pushes update the job object roughly twice a
  // second, and re-seeding on those would wipe out whatever the user is typing.
  // Render-phase adjustment rather than an effect — React's documented pattern
  // for props-derived state, and it avoids a frame of empty inputs.
  const [seededJobId, setSeededJobId] = useState<string | null>(null)
  if (job && seededJobId !== job.id) {
    setSeededJobId(job.id)
    setDraft(job.predicate)
    setName(job.name)
    setFilterDraft(null)
  }

  useDocumentTitle(job ? `${job.name} — Deep search` : 'Deep search', isActive)
  // Retitles the tab from the persisted job name, so a tab restored from a URL
  // or a saved tab set shows "voltura search" rather than a generic label.
  useResolvedTabName(job?.name, onNameResolved)

  // -------------------------------------
  // Functions
  // -------------------------------------

  async function run(fn: () => Promise<unknown>): Promise<void> {
    setActionError(null)
    try {
      await fn()
    } catch (err) {
      setActionError(err instanceof Error ? err.message : String(err))
    }
  }

  // -------------------------------------
  // Local Variables
  // -------------------------------------

  const hits = data?.hits ?? []
  const isRunning = job?.status === 'running' || job?.status === 'queued'
  const canEdit = job != null && !isRunning
  const predicateEmpty = draft == null || draft.clauses.every(isClauseEmpty)
  const multiClause =
    job != null && job.predicate.clauses.filter((c) => !isClauseEmpty(c)).length > 1
  const predicateDirty =
    job != null && draft != null && JSON.stringify(draft) !== JSON.stringify(job.predicate)
  // Tracked separately: gating the save on predicateDirty alone meant editing
  // only the name silently discarded it — the button never even appeared.
  const nameDirty = job != null && name.trim().length > 0 && name.trim() !== job.name
  const queryDirty = predicateDirty || nameDirty
  const filterDirty =
    job != null &&
    filterDraft != null &&
    sweepFilterKey(toSweepListFilter(filterDraft)) !== sweepFilterKey(job.filter)

  if (isLoading) {
    return (
      <Center py="xl">
        <Loader />
      </Center>
    )
  }

  // A tab can outlive its job — restored from a saved tab set after the job was
  // deleted, or after a profile switch.
  if (!job) {
    return (
      <Container size="xl" py="md">
        <Alert color="gray" icon={<IconAlertTriangle size={16} />} title="Sweep not found">
          {isError
            ? ((error as Error)?.message ?? 'This sweep could not be loaded.')
            : 'This sweep no longer exists — it may have been deleted, or it belongs to another profile. You can close this tab.'}
        </Alert>
      </Container>
    )
  }

  return (
    <Container size="xl" py="md">
      <Stack gap="md">
        <Group justify="space-between" align="start">
          <div>
            <Title fz={24}>{job.name}</Title>
            <Group gap="xs" mt={4}>
              <Badge color={STATUS_COLORS[job.status]} variant="light">
                {job.status}
              </Badge>
              {job.pauseReason && job.status === 'paused' && (
                <Text size="xs" c="dimmed">
                  {PAUSE_REASONS[job.pauseReason] ?? job.pauseReason}
                </Text>
              )}
              <Text size="xs" c="dimmed">
                created {formatSymphonyTimestamp(job.createdAt, 'D/M/YY HH:mm')}
              </Text>
            </Group>
          </div>
          <Group gap="xs">
            {isRunning ? (
              <Button
                variant="light"
                color="yellow"
                leftSection={<IconPlayerPause size={14} />}
                onClick={() => run(() => actions.pause(job.id))}
              >
                Pause
              </Button>
            ) : (
              <Tooltip label={predicateEmpty ? 'Add a variable condition first' : 'Start scanning'}>
                <Button
                  leftSection={<IconPlayerPlay size={14} />}
                  disabled={predicateEmpty}
                  onClick={() =>
                    run(async () => {
                      if (queryDirty && draft) {
                        await actions.update({ jobId: job.id, name, predicate: draft })
                      }
                      await actions.start(job.id)
                    })
                  }
                >
                  {job.status === 'done'
                    ? 'Run again'
                    : job.counters.scanned > 0
                      ? 'Resume'
                      : 'Start'}
                </Button>
              </Tooltip>
            )}
            <Tooltip label="Delete this sweep and its stored results">
              <ActionIcon
                variant="subtle"
                color="red"
                size="lg"
                onClick={() => {
                  if (window.confirm(`Delete sweep "${job.name}" and its results?`)) {
                    run(() => actions.remove(job.id))
                  }
                }}
              >
                <IconTrash size={16} />
              </ActionIcon>
            </Tooltip>
          </Group>
        </Group>

        {actionError && (
          <Alert color="red" icon={<IconAlertTriangle size={16} />}>
            {actionError}
          </Alert>
        )}
        {job.error && (
          <Alert color="red" icon={<IconAlertTriangle size={16} />} title="Sweep error">
            {job.error}
          </Alert>
        )}
        {!job.filter.startTimeInitStr && job.status === 'draft' && (
          <Alert color="yellow" icon={<IconAlertTriangle size={16} />} title="No start date">
            Without a start date this sweeps all history up to now, as a single query — and Symphony
            stops enumerating at about 10,000 results per query, so anything older than that is
            silently missed. Setting a start date also lets the sweep split into per-day windows,
            which avoids the cap entirely.
          </Alert>
        )}

        {job.truncated && (
          <Alert color="yellow" icon={<IconAlertTriangle size={16} />}>
            The server would not enumerate every result in one of this sweep&apos;s time windows.
            Narrow the date range for complete coverage.
          </Alert>
        )}
        {job.hitsTruncated && (
          <Alert color="yellow" icon={<IconAlertTriangle size={16} />}>
            Stopped recording after {job.options.maxHits.toLocaleString()} matches. Scanning
            continued, so the match count below is still the true total.
          </Alert>
        )}
        {job.driftDetected && (
          <Alert color="yellow" icon={<IconAlertTriangle size={16} />}>
            New requests appeared inside this sweep&apos;s window while it was running, so a segment
            was restarted. Already-scanned requests were skipped, not re-fetched.
          </Alert>
        )}

        <UiCard
          title="Which requests to sweep"
          rightElement={
            <Button
              size="xs"
              variant="subtle"
              color="gray"
              onClick={() => setShowFilter((v) => !v)}
            >
              {showFilter ? 'Hide' : 'Edit'}
            </Button>
          }
        >
          <Stack gap="xs">
            <Text size="sm">{filterSummary(job.filter)}</Text>
            <Collapse in={showFilter}>
              <Stack gap="sm" pt="xs">
                <FilterFields
                  value={filterDraft ?? fromSweepListFilter(job.filter)}
                  onChange={setFilterDraft}
                  disabled={isRunning}
                  showIdentityFields={false}
                />
                {filterDirty && job.counters.scanned > 0 && (
                  <Alert color="yellow" icon={<IconAlertTriangle size={16} />}>
                    Changing which requests to sweep discards this sweep&apos;s{' '}
                    {job.counters.scanned.toLocaleString()} scanned request
                    {job.counters.scanned === 1 ? '' : 's'} and {job.counters.hits.toLocaleString()}{' '}
                    match
                    {job.counters.hits === 1 ? '' : 'es'} — the old results describe the old query,
                    so it restarts from scratch.
                  </Alert>
                )}
                <Group justify="end" gap="sm">
                  <Button
                    size="xs"
                    variant="subtle"
                    color="gray"
                    disabled={!filterDirty}
                    onClick={() => setFilterDraft(fromSweepListFilter(job.filter))}
                  >
                    Discard changes
                  </Button>
                  <Button
                    size="xs"
                    disabled={!filterDirty || isRunning}
                    onClick={() =>
                      run(async () => {
                        if (
                          job.counters.scanned > 0 &&
                          !window.confirm(
                            `Restart "${job.name}"? Its ${job.counters.scanned.toLocaleString()} scanned requests and ${job.counters.hits.toLocaleString()} matches will be discarded.`
                          )
                        ) {
                          return
                        }
                        await actions.update({
                          jobId: job.id,
                          filter: toSweepListFilter(filterDraft as SymphonyFilterState)
                        })
                        setFilterDraft(null)
                      })
                    }
                  >
                    Save filter
                  </Button>
                </Group>
                {isRunning && (
                  <Text size="xs" c="dimmed">
                    Pause the sweep to change which requests it covers.
                  </Text>
                )}
              </Stack>
            </Collapse>
          </Stack>
        </UiCard>

        <UiCard title="What to look for in the variables">
          <Stack gap="sm">
            <TextInput
              label="Sweep name"
              description="Label only — names this sweep in its tab and in the saved-sweep list. It does not affect what is searched."
              value={name}
              disabled={!canEdit}
              onChange={(e) => setName(e.currentTarget.value)}
            />
            {draft && <ClauseEditor value={draft} onChange={setDraft} disabled={!canEdit} />}
            <Group justify="end">
              {queryDirty && canEdit && (
                <Button
                  size="xs"
                  variant="light"
                  onClick={() =>
                    run(() =>
                      actions.update({ jobId: job.id, name, predicate: draft as SweepPredicate })
                    )
                  }
                >
                  {predicateDirty ? 'Save conditions' : 'Save name'}
                </Button>
              )}
            </Group>
            {isRunning && (
              <Text size="xs" c="dimmed">
                Pause the sweep to change its conditions.
              </Text>
            )}
          </Stack>
        </UiCard>

        <UiCard title="Progress">
          <Stack gap="xs">
            <Group gap="lg">
              <Counter label="scanned" value={job.counters.scanned} />
              <Counter label="matches" value={job.counters.hits} />
              <Counter label="already seen" value={job.counters.skipped} />
              <Counter label="errors" value={job.counters.requestErrors} />
              <Counter
                label="time window"
                value={`${job.segmentIndex + 1}/${job.segments.length}`}
                hint={
                  job.segments.length > 1
                    ? `A wide date range is swept one day at a time, because Symphony stops enumerating at about 10,000 results per query. This sweep is on window ${job.segmentIndex + 1} of ${job.segments.length}.`
                    : 'The whole date range fits in one query. Ranges longer than 3 days are split into per-day windows, because Symphony stops enumerating at about 10,000 results per query.'
                }
              />
            </Group>
            <Text size="xs" c="dimmed">
              Closing Snappy pauses a running sweep; reopen this tab and press Resume to continue
              where it left off.
            </Text>
          </Stack>
        </UiCard>

        <UiCard
          title="Matches"
          rightElement={
            <Text size="xs" c="dimmed">
              {hits.length.toLocaleString()} shown
            </Text>
          }
        >
          <ScrollArea.Autosize mah={700}>
            <Table striped highlightOnHover stickyHeader>
              <Table.Thead>
                <Table.Tr>
                  <Table.Th w={140}>Process Key</Table.Th>
                  <Table.Th w={90}>Status</Table.Th>
                  {multiClause && <Table.Th w={50}>Cond</Table.Th>}
                  <Table.Th w={140}>Variable</Table.Th>
                  <Table.Th>Excerpt</Table.Th>
                  <Table.Th w={120}>Received</Table.Th>
                  <Table.Th w={40} />
                </Table.Tr>
              </Table.Thead>
              <Table.Tbody>
                {hits.map((hit) => (
                  <Table.Tr key={`${hit.seq}`}>
                    <Table.Td>
                      <Text size="xs">{hit.processKey ?? '—'}</Text>
                    </Table.Td>
                    <Table.Td>
                      {/* Plain text rather than a Badge — the wide excerpt
                          column squeezes this one and a Badge ellipsises to
                          "COMP…". */}
                      <Text size="xs" c="dimmed">
                        {hit.status ?? '—'}
                      </Text>
                    </Table.Td>
                    {multiClause && (
                      <Table.Td>
                        <Text size="xs" c="dimmed">
                          {(hit.clauseIndex ?? 0) + 1}
                        </Text>
                      </Table.Td>
                    )}
                    <Table.Td>
                      <Text size="xs" ff="monospace">
                        {hit.varName}
                      </Text>
                    </Table.Td>
                    <Table.Td>
                      <Tooltip label={`match at ${hit.matchOffset} of ${hit.valueLength}`}>
                        <Text size="xs" ff="monospace" lineClamp={2}>
                          {hit.excerpt}
                        </Text>
                      </Tooltip>
                    </Table.Td>
                    <Table.Td>
                      <Text size="xs" c="dimmed">
                        {formatSymphonyTimestamp(hit.createdDate, 'D/M/YY HH:mm')}
                      </Text>
                    </Table.Td>
                    <Table.Td>
                      <ActionIcon
                        component={Link}
                        variant="subtle"
                        size="sm"
                        to={tabPath({
                          kind: 'symphony-request',
                          requestId: hit.requestId,
                          processId: hit.processId,
                          label: hit.processKey ?? hit.requestId
                        })}
                      >
                        <IconEye size={14} />
                      </ActionIcon>
                    </Table.Td>
                  </Table.Tr>
                ))}
              </Table.Tbody>
            </Table>

            {hits.length === 0 && (
              <Center py="lg">
                <Text size="sm" c="dimmed">
                  {job.counters.scanned === 0 ? 'Nothing scanned yet.' : 'No matches so far.'}
                </Text>
              </Center>
            )}
          </ScrollArea.Autosize>
        </UiCard>
      </Stack>
    </Container>
  )
}

function Counter({
  label,
  value,
  hint
}: {
  label: string
  value: number | string
  hint?: string
}): React.JSX.Element {
  const body = (
    <div>
      <Text size="lg" fw={600}>
        {typeof value === 'number' ? value.toLocaleString() : value}
      </Text>
      <Text size="xs" c="dimmed" style={hint ? { textDecoration: 'underline dotted' } : undefined}>
        {label}
      </Text>
    </div>
  )
  return hint ? (
    <Tooltip label={hint} multiline w={320}>
      {body}
    </Tooltip>
  ) : (
    body
  )
}

/** One-line description of the request set a sweep covers. */
function filterSummary(filter: SweepListFilter): string {
  const parts: string[] = [filter.processKey ? filter.processKey : 'All processes']
  if (filter.startTimeInitStr || filter.startTimeEndStr) {
    parts.push(`${filter.startTimeInitStr ?? 'any time'} → ${filter.startTimeEndStr ?? 'now'}`)
  }
  parts.push(
    filter.statuses.length === 0 || filter.statuses.length === 5
      ? 'any status'
      : filter.statuses.join(', ')
  )
  // Only surfaced for jobs created before these were dropped from new sweeps.
  for (const [label, value] of [
    ['request', filter.requestId],
    ['instance', filter.processId],
    ['reference', filter.referenceId],
    ['external key', filter.externalKey]
  ] as const) {
    if (value) parts.push(`${label} ${value}`)
  }
  if (filter.deadJob) parts.push('including dead jobs')
  return parts.join(' · ')
}
