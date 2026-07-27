export type { OneToMany, OdooDomain, Asset } from '../../../main/backend/odoo'

export async function odooSearch(
  model: string,
  domain: unknown,
  offset: number = 0,
  limit?: number,
  order?: string
): Promise<any> {
  return window.api.odoo.search(model, domain, offset, limit, order)
}

export async function odooRead(model: string, ids: number[], fields: string[]): Promise<any> {
  return window.api.odoo.read(model, ids, fields)
}

export async function odooWrite(
  model: string,
  ids: number[],
  values: Record<string, unknown>,
  context?: Record<string, unknown>
): Promise<any> {
  return window.api.odoo.write(model, ids, values, context)
}

export async function odooSearchRead(
  model: string,
  domain: unknown,
  fields?: string[],
  offset: number = 0,
  limit?: number,
  order?: string
): Promise<any> {
  return window.api.odoo.searchRead(model, domain, fields, offset, limit, order)
}

export async function odooFieldsGet(
  model: string,
  fields?: string[],
  attributes?: string[]
): Promise<any> {
  return window.api.odoo.fieldsGet(model, fields, attributes)
}

export async function odooNameGet(model: string, ids: number[]): Promise<[number, string][]> {
  return window.api.odoo.nameGet(model, ids) as Promise<[number, string][]>
}

export async function odooCallMethod(model: string, ids: number[], method: string): Promise<any> {
  return window.api.odoo.callMethod(model, ids, method)
}

export async function callBit2win(
  url: string,
  method: 'GET' | 'PUT' | 'POST' | 'PATCH',
  params?: URLSearchParams,
  body?: unknown,
  headers?: HeadersInit
): Promise<any> {
  const paramTuples = params ? Array.from(params.entries()) : undefined
  return window.api.b2w.call(url, method, paramTuples, body, headers)
}

export async function getAssets(filters?: Record<string, unknown>): Promise<any> {
  return window.api.b2w.getAssets(filters)
}
