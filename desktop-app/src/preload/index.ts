import { contextBridge, ipcRenderer } from 'electron'
import { electronAPI } from '@electron-toolkit/preload'

const api = {
  odoo: {
    search: (
      model: string,
      domain: unknown,
      offset?: number,
      limit?: number,
      order?: string
    ): Promise<unknown> => ipcRenderer.invoke('odoo:search', model, domain, offset, limit, order),
    read: (model: string, ids: number[], fields: string[]): Promise<unknown> =>
      ipcRenderer.invoke('odoo:read', model, ids, fields),
    write: (
      model: string,
      ids: number[],
      values: Record<string, unknown>,
      context?: Record<string, unknown>
    ): Promise<unknown> => ipcRenderer.invoke('odoo:write', model, ids, values, context),
    searchRead: (
      model: string,
      domain: unknown,
      fields?: string[],
      offset?: number,
      limit?: number,
      order?: string
    ): Promise<unknown> =>
      ipcRenderer.invoke('odoo:searchRead', model, domain, fields, offset, limit, order),
    fieldsGet: (model: string, fields?: string[], attributes?: string[]): Promise<unknown> =>
      ipcRenderer.invoke('odoo:fieldsGet', model, fields, attributes),
    nameGet: (model: string, ids: number[]): Promise<unknown> =>
      ipcRenderer.invoke('odoo:nameGet', model, ids),
    callMethod: (model: string, ids: number[], method: string): Promise<unknown> =>
      ipcRenderer.invoke('odoo:callMethod', model, ids, method)
  },
  b2w: {
    call: (
      url: string,
      method: 'GET' | 'PUT' | 'POST' | 'PATCH',
      paramTuples?: [string, string][],
      body?: unknown,
      headers?: HeadersInit
    ): Promise<unknown> => ipcRenderer.invoke('b2w:call', url, method, paramTuples, body, headers),
    getAssets: (filters?: Record<string, unknown>): Promise<unknown> =>
      ipcRenderer.invoke('b2w:getAssets', filters)
  },
  devops: {
    getMyWorkItems: (): Promise<unknown> => ipcRenderer.invoke('devops:getMyWorkItems')
  },
  settings: {
    getStore: (): Promise<unknown> => ipcRenderer.invoke('settings:getStore'),
    saveProfile: (profile: unknown): Promise<unknown> =>
      ipcRenderer.invoke('settings:saveProfile', profile),
    deleteProfile: (id: string): Promise<void> => ipcRenderer.invoke('settings:deleteProfile', id),
    setActiveProfile: (id: string): Promise<void> =>
      ipcRenderer.invoke('settings:setActiveProfile', id)
  },
  savedDomains: {
    list: (): Promise<unknown> => ipcRenderer.invoke('savedDomains:list'),
    save: (input: { id?: string; name: string; domain: string }): Promise<unknown> =>
      ipcRenderer.invoke('savedDomains:save', input),
    remove: (id: string): Promise<void> => ipcRenderer.invoke('savedDomains:remove', id)
  },
  updater: {
    onUpdateDownloaded: (callback: () => void): (() => void) => {
      const listener = (): void => callback()
      ipcRenderer.on('updater:update-downloaded', listener)
      return () => ipcRenderer.removeListener('updater:update-downloaded', listener)
    },
    quitAndInstall: (): Promise<void> => ipcRenderer.invoke('updater:quitAndInstall')
  }
}

if (process.contextIsolated) {
  try {
    contextBridge.exposeInMainWorld('electron', electronAPI)
    contextBridge.exposeInMainWorld('api', api)
  } catch (error) {
    console.error(error)
  }
} else {
  // @ts-ignore (define in dts)
  window.electron = electronAPI
  // @ts-ignore (define in dts)
  window.api = api
}

export type Api = typeof api
