// Shared encode/decode for the safeStorage-backed JSON stores.
//
// Why this exists: on Linux, Chromium picks its password-store backend from
// XDG_CURRENT_DESKTOP. Launched from a bare shell (no desktop session exported
// — `npm run dev` from a plain terminal, tmux, ssh, a CI box) that variable is
// missing, Chromium falls back to `basic_text`, and safeStorage.
// isEncryptionAvailable() returns false. The stores then read an
// already-encrypted file as UTF-8 and JSON.parse died on the raw ciphertext with
// "Unexpected token 'v'" — the v10/v11 prefix Chromium's OSCrypt writes.
//
// decodeStore tries both representations instead of trusting
// isEncryptionAvailable(), so a store written in either mode is readable in
// either mode. If the payload really is ciphertext we cannot decrypt, it throws
// something actionable rather than a JSON syntax error, and never rewrites the
// file — the credentials in it are still recoverable once the keyring is back.

import { safeStorage } from 'electron'

/** OSCrypt ciphertext version prefixes. v10 = hardcoded key, v11 = keyring key. */
const CIPHERTEXT_PREFIXES = ['v10', 'v11']

function looksEncrypted(buffer: Buffer): boolean {
  const prefix = buffer.subarray(0, 3).toString('latin1')
  return CIPHERTEXT_PREFIXES.includes(prefix)
}

export class StoreDecryptError extends Error {
  constructor(name: string, cause: unknown) {
    super(
      `Could not decrypt ${name}: the OS keyring is not available to this process, ` +
        `so its encrypted contents cannot be read (backend: ` +
        `${safeStorage.getSelectedStorageBackend?.() ?? 'unknown'}). ` +
        `The file has been left untouched. On Linux this usually means the app was ` +
        `launched without a desktop session — retry with XDG_CURRENT_DESKTOP set ` +
        `(e.g. XDG_CURRENT_DESKTOP=GNOME npm run dev) or pass ` +
        `--password-store=gnome-libsecret. Original error: ${String(cause)}`
    )
    this.name = 'StoreDecryptError'
  }
}

/**
 * Reads a store file, tolerating both encrypted and plaintext payloads
 * regardless of what the current process thinks is available.
 *
 * @param name Human-readable store name, used only in error messages.
 */
export function decodeStore(buffer: Buffer, name: string): unknown {
  const encrypted = looksEncrypted(buffer)

  if (encrypted) {
    try {
      return JSON.parse(safeStorage.decryptString(buffer))
    } catch (err) {
      // Nothing else to try: plaintext parsing of ciphertext is what produced
      // the confusing error this module exists to prevent.
      throw new StoreDecryptError(name, err)
    }
  }

  try {
    return JSON.parse(buffer.toString('utf-8'))
  } catch (plainErr) {
    // Not a recognized prefix and not valid JSON. It may still be ciphertext
    // from a future/different scheme, so try decrypting before giving up.
    try {
      return JSON.parse(safeStorage.decryptString(buffer))
    } catch {
      throw new Error(`Could not read ${name}: not valid JSON. Original error: ${String(plainErr)}`)
    }
  }
}

/** Encrypts when possible; warns once per call site when it cannot. */
export function encodeStore(value: unknown, name: string): Buffer {
  const json = JSON.stringify(value)
  if (!safeStorage.isEncryptionAvailable()) {
    console.warn(
      `safeStorage encryption is unavailable on this system (backend: ` +
        `${safeStorage.getSelectedStorageBackend?.() ?? 'unknown'}) — ${name} will be saved unencrypted.`
    )
    return Buffer.from(json, 'utf-8')
  }
  return safeStorage.encryptString(json)
}
