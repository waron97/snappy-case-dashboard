'use server';

export type OneToMany = [number, string];

class ConnectError extends Error {
  constructor(response: Response, text: string) {
    super(`Failed to load resource at ${response.url}: status code ${response.status} : ${text}`);
  }
}

class AuthError extends Error {
  constructor() {
    super('Authentication failed (401)');
  }
}

class OdooError extends Error {
  constructor(error: { code: number; message: string; data: { message: string } }) {
    super(`Odoo error: ${error.data?.message ?? error.message}`);
  }
}

function encodeQs(body: { [key: string]: string }): string {
  const searchParams = new URLSearchParams();
  Object.entries(body).forEach(([key, value]) => {
    searchParams.append(key, value);
  });
  return searchParams.toString();
}

async function getToken() {
  const {
    KEYCLOAK_PASSWORD: keycloakPassword,
    KEYCLOAK_USER: keycloakUser,
    KEYCLOAK_URL: keycloakUrl,
    KEYCLOAK_CLIENT_ID: keycloakClientId,
    KEYCLOAK_CLIENT_SECRET: keycloakClientSecret,
  } = process.env;
  const response = await fetch(keycloakUrl!, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: encodeQs({
      username: keycloakUser!,
      password: keycloakPassword!,
      client_id: keycloakClientId!,
      client_secret: keycloakClientSecret!,
      grant_type: 'password',
    }),
  });
  if (response.status === 200) {
    const json = await response.json();
    return json.access_token;
  }
  throw new ConnectError(response, await response.text());
}

let tokenPromise: Promise<string> | null = null;

async function getCachedToken(): Promise<string> {
  if (!tokenPromise) {
    tokenPromise = getToken().catch((e) => {
      tokenPromise = null;
      throw e;
    });
  }
  return tokenPromise;
}

function invalidateToken() {
  tokenPromise = null;
}

type OdooParams = {
  service: string;
  method: string;
  args: unknown[];
};

async function odooJsonRpc(params: OdooParams, token: string) {
  const { ODOO_URL: odooUrl } = process.env;
  const response = await fetch(`${odooUrl}/jsonrpc`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      id: 1,
      jsonrpc: '2.0',
      method: 'call',
      params,
    }),
  });
  if (response.status === 401) {
    throw new AuthError();
  }
  if (response.status !== 200) {
    throw new ConnectError(response, await response.text());
  }
  const json = await response.json();
  if (json.error) {
    throw new OdooError(json.error);
  }
  return json.result;
}

async function odooExecuteKw(
  model: string,
  method: string,
  args: unknown[],
  kwargs?: Record<string, unknown>
) {
  const { ODOO_API_KEY: apiKey, ODOO_DB: db, ODOO_UID: uidStr } = process.env;
  const uid = parseInt(uidStr!, 10);
  const token = await getCachedToken();

  const executeKwArgs: unknown[] = [db, uid, apiKey, model, method, args];
  if (kwargs !== undefined) {
    executeKwArgs.push(kwargs);
  }

  const params: OdooParams = {
    service: 'object',
    method: 'execute_kw',
    args: executeKwArgs,
  };

  try {
    return await odooJsonRpc(params, token);
  } catch (e) {
    if (e instanceof AuthError) {
      invalidateToken();
      const freshToken = await getCachedToken();
      return odooJsonRpc(params, freshToken);
    }
    throw e;
  }
}

export type OdooDomain = Array<string | number | boolean | null | OdooDomain>;

export async function odooSearch(
  model: string,
  domain: OdooDomain,
  offset: number = 0,
  limit?: number,
  order?: string
) {
  const kwargs: Record<string, unknown> = { offset };
  if (limit !== undefined) {
    kwargs.limit = limit;
  }
  if (order !== undefined) {
    kwargs.order = order;
  }

  return odooExecuteKw(model, 'search', [domain], kwargs);
}

export async function odooRead(model: string, ids: number[], fields: string[]) {
  return odooExecuteKw(model, 'read', [ids, fields]);
}

export async function odooWrite(
  model: string,
  ids: number[],
  values: Record<string, unknown>,
  context?: Record<string, unknown>
) {
  const kwargs = context ? { context } : undefined;
  return odooExecuteKw(model, 'write', [ids, values], kwargs);
}

export async function odooSearchRead(
  model: string,
  domain: OdooDomain,
  fields?: string[],
  offset: number = 0,
  limit?: number,
  order?: string
) {
  const kwargs: Record<string, unknown> = { offset };
  if (limit !== undefined) {
    kwargs.limit = limit;
  }
  if (order !== undefined) {
    kwargs.order = order;
  }

  const args: unknown[] = [domain];
  if (fields !== undefined) {
    args.push(fields);
  }

  return odooExecuteKw(model, 'search_read', args, kwargs);
}

export async function odooFieldsGet(model: string, fields?: string[], attributes?: string[]) {
  const kwargs: Record<string, unknown> = {};
  if (attributes !== undefined) {
    kwargs.attributes = attributes;
  }
  const args: unknown[] = [fields ?? []];
  return odooExecuteKw(model, 'fields_get', args, kwargs);
}

export async function odooNameGet(
  model: string,
  ids: number[]
): Promise<[number, string][]> {
  return odooExecuteKw(model, 'name_get', [ids]);
}

export async function odooCallMethod(
  model: string,
  ids: number[],
  method: string
) {
  return odooExecuteKw(model, method, [ids]);
}
