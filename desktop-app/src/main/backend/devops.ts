import { getSettings } from './settings'

const TERMINAL_STATES = ['Closed', 'Resolved', 'Removed']
const BATCH_SIZE = 200

export interface DevOpsWorkItem {
  id: number
  title: string
  description: string
  status: string
  assignee: string | null
  createdDate: string
  project: string
  lastCommentDate: string | null
  lastCommentText: string | null
  lastCommentAuthor: string | null
  url: string
}

export class DevOpsError extends Error {
  constructor(response: Response, text: string) {
    const hint =
      response.status === 401
        ? ' — your Azure DevOps PAT is invalid, expired, or missing the Work Items (Read) scope'
        : ''
    super(`Azure DevOps request to ${response.url} failed with ${response.status}${hint}: ${text}`)
  }
}

function stripHtml(html: string): string {
  return html
    .replace(/<[^>]*>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/\s+/g, ' ')
    .trim()
}

function chunk<T>(items: T[], size: number): T[][] {
  const chunks: T[][] = []
  for (let i = 0; i < items.length; i += size) {
    chunks.push(items.slice(i, i + size))
  }
  return chunks
}

async function getDevOpsPat(): Promise<string> {
  const { devopsPat } = getSettings()
  if (!devopsPat) {
    throw new Error('Azure DevOps token not configured. Please configure your settings.')
  }
  return devopsPat
}

async function callDevOps<T>(path: string, pat: string, init?: RequestInit): Promise<T> {
  const { devopsOrg: org } = getSettings()
  const response = await fetch(`https://dev.azure.com/${org}${path}`, {
    ...init,
    headers: {
      ...init?.headers,
      Authorization: `Basic ${Buffer.from(`:${pat}`).toString('base64')}`
    }
  })
  if (response.status !== 200) {
    throw new DevOpsError(response, await response.text())
  }
  return response.json()
}

interface WiqlResult {
  workItems: { id: number }[]
}

interface WorkItemFields {
  'System.Id': number
  'System.Title': string
  'System.Description'?: string
  'System.State': string
  'System.AssignedTo'?: { displayName: string }
  'System.CreatedDate': string
  'System.TeamProject': string
  'System.CommentCount': number
}

interface WorkItemsBatchResult {
  value: { id: number; fields: WorkItemFields }[]
}

interface CommentsResult {
  comments: { text: string; createdDate: string; createdBy: { displayName: string } }[]
}

async function fetchLastComment(
  project: string,
  id: number,
  pat: string
): Promise<{ date: string; text: string; author: string } | null> {
  const result = await callDevOps<CommentsResult>(
    `/${encodeURIComponent(project)}/_apis/wit/workItems/${id}/comments?api-version=7.1-preview.4&$top=1&$order=desc`,
    pat
  )
  const [comment] = result.comments
  if (!comment) {
    return null
  }
  return {
    date: comment.createdDate,
    text: stripHtml(comment.text),
    author: comment.createdBy.displayName
  }
}

export async function getMyWorkItems(): Promise<DevOpsWorkItem[]> {
  const pat = await getDevOpsPat()
  const { devopsOrg: org } = getSettings()

  const wiql = await callDevOps<WiqlResult>('/_apis/wit/wiql?api-version=7.1', pat, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query:
        'SELECT [System.Id] FROM WorkItems WHERE [System.CreatedBy] = @Me ORDER BY [System.CreatedDate] DESC'
    })
  })

  const ids = wiql.workItems.map((w) => w.id)
  if (ids.length === 0) {
    return []
  }

  const fields = [
    'System.Id',
    'System.Title',
    'System.Description',
    'System.State',
    'System.AssignedTo',
    'System.CreatedDate',
    'System.TeamProject',
    'System.CommentCount'
  ].join(',')

  const batches = await Promise.all(
    chunk(ids, BATCH_SIZE).map((batchIds) =>
      callDevOps<WorkItemsBatchResult>(
        `/_apis/wit/workitems?ids=${batchIds.join(',')}&fields=${fields}&api-version=7.1`,
        pat
      )
    )
  )
  const workItems = batches.flatMap((batch) => batch.value)

  const items: DevOpsWorkItem[] = await Promise.all(
    workItems.map(async (wi) => {
      const f = wi.fields
      const lastComment =
        f['System.CommentCount'] > 0
          ? await fetchLastComment(f['System.TeamProject'], wi.id, pat)
          : null

      return {
        id: wi.id,
        title: f['System.Title'],
        description: f['System.Description'] ? stripHtml(f['System.Description']) : '',
        status: f['System.State'],
        assignee: f['System.AssignedTo']?.displayName ?? null,
        createdDate: f['System.CreatedDate'],
        project: f['System.TeamProject'],
        lastCommentDate: lastComment?.date ?? null,
        lastCommentText: lastComment?.text ?? null,
        lastCommentAuthor: lastComment?.author ?? null,
        url: `https://dev.azure.com/${org}/${encodeURIComponent(
          f['System.TeamProject']
        )}/_workitems/edit/${wi.id}`
      }
    })
  )

  return items.sort((a, b) => {
    const aTerminal = TERMINAL_STATES.includes(a.status)
    const bTerminal = TERMINAL_STATES.includes(b.status)
    if (aTerminal !== bTerminal) {
      return aTerminal ? 1 : -1
    }

    const aDate = new Date(a.lastCommentDate ?? a.createdDate).getTime()
    const bDate = new Date(b.lastCommentDate ?? b.createdDate).getTime()
    return bDate - aDate
  })
}
