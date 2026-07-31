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
  symphony: {
    getRequestTree: (query: unknown): Promise<unknown> =>
      ipcRenderer.invoke('symphony:getRequestTree', query),
    getHistoricVariables: (
      processInstanceId: string,
      page?: number,
      size?: number
    ): Promise<unknown> =>
      ipcRenderer.invoke('symphony:getHistoricVariables', processInstanceId, page, size),
    getHistoricActivities: (
      processInstanceId: string,
      page?: number,
      size?: number
    ): Promise<unknown> =>
      ipcRenderer.invoke('symphony:getHistoricActivities', processInstanceId, page, size),
    getRequestDetailHtml: (
      requestId: string,
      parentId: string | null,
      opts?: unknown
    ): Promise<string> =>
      ipcRenderer.invoke('symphony:getRequestDetailHtml', requestId, parentId, opts),
    getExecutionTreeNode: (nodeId: string, query: unknown): Promise<string> =>
      ipcRenderer.invoke('symphony:getExecutionTreeNode', nodeId, query),
    processKeys: {
      listCached: (profileId: string): Promise<unknown> =>
        ipcRenderer.invoke('symphony:listCachedProcessKeys', profileId),
      listObserved: (profileId: string): Promise<unknown> =>
        ipcRenderer.invoke('symphony:listObservedProcessKeys', profileId),
      refresh: (force?: boolean): Promise<unknown> =>
        ipcRenderer.invoke('symphony:refreshProcessKeys', force),
      search: (nameLike: string): Promise<unknown> =>
        ipcRenderer.invoke('symphony:searchProcessKeys', nameLike)
    },
    deepSearch: {
      list: (): Promise<unknown> => ipcRenderer.invoke('symphony:deepSearch:list'),
      snapshot: (jobId: string): Promise<unknown> =>
        ipcRenderer.invoke('symphony:deepSearch:snapshot', jobId),
      create: (input: unknown): Promise<unknown> =>
        ipcRenderer.invoke('symphony:deepSearch:create', input),
      update: (jobId: string, patch: unknown): Promise<unknown> =>
        ipcRenderer.invoke('symphony:deepSearch:update', jobId, patch),
      start: (jobId: string): Promise<unknown> =>
        ipcRenderer.invoke('symphony:deepSearch:start', jobId),
      pause: (jobId: string): Promise<unknown> =>
        ipcRenderer.invoke('symphony:deepSearch:pause', jobId),
      remove: (jobId: string): Promise<void> =>
        ipcRenderer.invoke('symphony:deepSearch:delete', jobId),
      onProgress: (callback: (payload: unknown) => void): (() => void) => {
        const listener = (_e: unknown, payload: unknown): void => callback(payload)
        ipcRenderer.on('symphony:deepSearch:progress', listener)
        return () => ipcRenderer.removeListener('symphony:deepSearch:progress', listener)
      }
    }
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
  savedTabSets: {
    list: (profileId: string): Promise<unknown> =>
      ipcRenderer.invoke('savedTabSets:list', profileId),
    save: (input: {
      id?: string
      profileId: string
      name: string
      tabs: unknown[]
    }): Promise<unknown> => ipcRenderer.invoke('savedTabSets:save', input),
    remove: (id: string): Promise<void> => ipcRenderer.invoke('savedTabSets:remove', id)
  },
  uiPrefs: {
    getAll: (): Promise<Record<string, unknown>> => ipcRenderer.invoke('uiPrefs:getAll'),
    set: (key: string, value: unknown): Promise<void> =>
      ipcRenderer.invoke('uiPrefs:set', key, value)
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
