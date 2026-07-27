import { getSettings } from './settings'
import { ConnectError, getCachedToken, invalidateToken } from './keycloak'

export type OneToMany = [number, string]

export class AuthError extends Error {
  constructor() {
    super('Authentication failed (401)')
  }
}

export class OdooError extends Error {
  constructor(error: { code: number; message: string; data: { message: string } }) {
    super(`Odoo error: ${error.data?.message ?? error.message}`)
  }
}

type OdooParams = {
  service: string
  method: string
  args: unknown[]
}

async function odooJsonRpc(params: OdooParams, token: string): Promise<any> {
  const { odooUrl } = getSettings()
  const response = await fetch(`${odooUrl}/jsonrpc`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({
      id: 1,
      jsonrpc: '2.0',
      method: 'call',
      params
    })
  })
  if (response.status === 401) {
    throw new AuthError()
  }
  if (response.status !== 200) {
    throw new ConnectError(response, await response.text())
  }
  const json = await response.json()
  if (json.error) {
    throw new OdooError(json.error)
  }
  return json.result
}

async function odooExecuteKw(
  model: string,
  method: string,
  args: unknown[],
  kwargs?: Record<string, unknown>
): Promise<any> {
  const { odooDb: db, odooUid, odooApiKey } = getSettings()
  if (!odooUid || !odooApiKey) {
    throw new Error('Credentials not configured. Please configure your settings.')
  }

  const uid = parseInt(odooUid, 10)
  const token = await getCachedToken()

  const executeKwArgs: unknown[] = [db, uid, odooApiKey, model, method, args]
  if (kwargs !== undefined) {
    executeKwArgs.push(kwargs)
  }

  const params: OdooParams = {
    service: 'object',
    method: 'execute_kw',
    args: executeKwArgs
  }

  try {
    return await odooJsonRpc(params, token)
  } catch (e) {
    if (e instanceof AuthError) {
      invalidateToken()
      const freshToken = await getCachedToken()
      return odooJsonRpc(params, freshToken)
    }
    throw e
  }
}

export type OdooDomain = Array<string | number | boolean | null | OdooDomain>

export async function odooSearch(
  model: string,
  domain: OdooDomain,
  offset: number = 0,
  limit?: number,
  order?: string
): Promise<any> {
  const kwargs: Record<string, unknown> = { offset }
  if (limit !== undefined) {
    kwargs.limit = limit
  }
  if (order !== undefined) {
    kwargs.order = order
  }

  return odooExecuteKw(model, 'search', [domain], kwargs)
}

export async function odooRead(model: string, ids: number[], fields: string[]): Promise<any> {
  return odooExecuteKw(model, 'read', [ids, fields])
}

export async function odooWrite(
  model: string,
  ids: number[],
  values: Record<string, unknown>,
  context?: Record<string, unknown>
): Promise<any> {
  const kwargs = context ? { context } : undefined
  return odooExecuteKw(model, 'write', [ids, values], kwargs)
}

export async function odooSearchRead(
  model: string,
  domain: OdooDomain,
  fields?: string[],
  offset: number = 0,
  limit?: number,
  order?: string
): Promise<any> {
  const kwargs: Record<string, unknown> = { offset }
  if (limit !== undefined) {
    kwargs.limit = limit
  }
  if (order !== undefined) {
    kwargs.order = order
  }

  const args: unknown[] = [domain]
  if (fields !== undefined) {
    args.push(fields)
  }

  return odooExecuteKw(model, 'search_read', args, kwargs)
}

export async function odooFieldsGet(
  model: string,
  fields?: string[],
  attributes?: string[]
): Promise<any> {
  const kwargs: Record<string, unknown> = {}
  if (attributes !== undefined) {
    kwargs.attributes = attributes
  }
  const args: unknown[] = [fields ?? []]
  return odooExecuteKw(model, 'fields_get', args, kwargs)
}

export async function odooNameGet(model: string, ids: number[]): Promise<[number, string][]> {
  return odooExecuteKw(model, 'name_get', [ids])
}

export async function odooCallMethod(model: string, ids: number[], method: string): Promise<any> {
  return odooExecuteKw(model, method, [ids])
}

export async function callBit2win(
  url: string,
  method: 'GET' | 'PUT' | 'POST' | 'PATCH',
  params?: URLSearchParams,
  body?: unknown,
  headers?: HeadersInit
): Promise<any> {
  const token = await getCachedToken()
  const op = async (token: string): Promise<any> => {
    const { b2wUrl } = getSettings()
    let parsedUrl = url

    if (!url.startsWith(b2wUrl)) {
      parsedUrl = `${b2wUrl}${url}`
    }

    if (params) {
      parsedUrl = `${parsedUrl}?${params.toString()}`
    }

    const parsedHeaders = new Headers(headers || {})
    parsedHeaders.set('Authorization', `Bearer ${token}`)
    parsedHeaders.set('output', `all`)

    const response = await fetch(parsedUrl, {
      method,
      headers: parsedHeaders,
      body: body ? JSON.stringify(body) : undefined
    })

    if (response.status === 401) {
      throw new AuthError()
    }

    if (response.status !== 200) {
      throw new ConnectError(response, await response.text())
    }

    const json = await response.json()

    return json
  }

  try {
    return await op(token)
  } catch (err) {
    if (err instanceof AuthError) {
      invalidateToken()
      const freshToken = await getCachedToken()
      return op(freshToken)
    }
    throw err
  }
}

export type Asset = {
  _id: string
  prcode: string
  crm_accountcode: string
  accountcode: string
  createdate: string
  activationdate: string
  podcode: string
  assetstatus: string
  sm_state: string
  contract_id: string
}

type SuggestedAssetFilters = {
  type?: 'product' | 'childproduct'
  prcode?: string
  podcode?: string
  accountcode?: string
  crm_accountcode?: string
  [key: string]: string | undefined
}

export async function getAssets(filters: SuggestedAssetFilters = {}): Promise<Asset[]> {
  const params = new URLSearchParams({
    query: new URLSearchParams(filters as Record<string, string>).toString()
  })
  const headers = { limit: '100' }
  return callBit2win('/api/ordermanagement/v1/asset', 'GET', params, undefined, headers).then(
    (res) => res.results
  )
}
