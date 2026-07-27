import { getSettings } from './settings'

export class ConnectError extends Error {
  constructor(response: Response, text: string) {
    super(`Failed to load resource at ${response.url}: status code ${response.status} : ${text}`)
  }
}

function encodeQs(body: { [key: string]: string }): string {
  const searchParams = new URLSearchParams()
  Object.entries(body).forEach(([key, value]) => {
    searchParams.append(key, value)
  })
  return searchParams.toString()
}

async function getToken(): Promise<string> {
  const {
    keycloakUrl,
    keycloakServiceUsername,
    keycloakServicePassword,
    keycloakClientId,
    keycloakClientSecret
  } = getSettings()

  const response = await fetch(keycloakUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: encodeQs({
      username: keycloakServiceUsername,
      password: keycloakServicePassword,
      client_id: keycloakClientId,
      client_secret: keycloakClientSecret,
      grant_type: 'password'
    })
  })
  if (response.status === 200) {
    const json = await response.json()
    return json.access_token
  }
  throw new ConnectError(response, await response.text())
}

let tokenPromise: Promise<string> | null = null

export async function getCachedToken(): Promise<string> {
  if (!tokenPromise) {
    tokenPromise = getToken().catch((e) => {
      tokenPromise = null
      throw e
    })
  }
  return tokenPromise
}

export function invalidateToken(): void {
  tokenPromise = null
}
