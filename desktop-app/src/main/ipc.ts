import { ipcMain } from 'electron'
import * as odoo from './backend/odoo'
import * as devops from './backend/devops'
import * as symphony from './backend/symphony/client'
import {
  ensureCatalog,
  getObservedProcessKeys,
  getUsableCachedCatalog,
  searchProcessKeys
} from './backend/symphony/catalog'
import {
  createSweep,
  deleteSweep,
  getSweepSnapshot,
  listSweeps,
  pauseAllForProfileSwitch,
  pauseSweep,
  startSweep,
  updateSweep
} from './backend/symphony/sweepEngine'
import type { UpdateSweepPatch } from './backend/symphony/sweepEngine'
import type { CreateSweepInput } from './backend/symphony/sweepTypes'
import type {
  SymphonyRequestDetailOptions,
  SymphonyRequestTreeQuery
} from './backend/symphony/types'
import { invalidateToken } from './backend/keycloak'
import {
  getStore,
  saveProfile,
  deleteProfile,
  setActiveProfile,
  type Profile
} from './backend/settings'
import { listSavedDomains, saveSavedDomain, removeSavedDomain } from './backend/savedDomains'
import { listSavedTabSets, saveSavedTabSet, removeSavedTabSet } from './backend/savedTabSets'
import { getUiPrefs, setUiPref } from './backend/uiPrefs'
import { quitAndInstall } from './updater'

export function registerIpcHandlers(): void {
  ipcMain.handle('odoo:search', (_e, model, domain, offset, limit, order) =>
    odoo.odooSearch(model, domain, offset, limit, order)
  )
  ipcMain.handle('odoo:read', (_e, model, ids, fields) => odoo.odooRead(model, ids, fields))
  ipcMain.handle('odoo:write', (_e, model, ids, values, context) =>
    odoo.odooWrite(model, ids, values, context)
  )
  ipcMain.handle('odoo:searchRead', (_e, model, domain, fields, offset, limit, order) =>
    odoo.odooSearchRead(model, domain, fields, offset, limit, order)
  )
  ipcMain.handle('odoo:fieldsGet', (_e, model, fields, attributes) =>
    odoo.odooFieldsGet(model, fields, attributes)
  )
  ipcMain.handle('odoo:nameGet', (_e, model, ids) => odoo.odooNameGet(model, ids))
  ipcMain.handle('odoo:callMethod', (_e, model, ids, method) =>
    odoo.odooCallMethod(model, ids, method)
  )

  // params arrives as a plain [key, string][] tuple array — URLSearchParams isn't
  // structured-clone-safe over contextBridge, so it's reconstructed here.
  ipcMain.handle('b2w:call', (_e, url, method, paramTuples, body, headers) =>
    odoo.callBit2win(
      url,
      method,
      paramTuples ? new URLSearchParams(paramTuples) : undefined,
      body,
      headers
    )
  )
  ipcMain.handle('b2w:getAssets', (_e, filters) => odoo.getAssets(filters))

  ipcMain.handle('devops:getMyWorkItems', () => devops.getMyWorkItems())

  ipcMain.handle('symphony:getRequestTree', (_e, query: SymphonyRequestTreeQuery) =>
    symphony.getRequestTree(query)
  )
  ipcMain.handle(
    'symphony:getHistoricVariables',
    (_e, processInstanceId: string, page?: number, size?: number) =>
      symphony.getHistoricVariables(processInstanceId, page, size)
  )
  ipcMain.handle(
    'symphony:getHistoricActivities',
    (_e, processInstanceId: string, page?: number, size?: number) =>
      symphony.getHistoricActivities(processInstanceId, page, size)
  )
  ipcMain.handle(
    'symphony:getRequestDetailHtml',
    (_e, requestId: string, parentId: string | null, opts?: SymphonyRequestDetailOptions) =>
      symphony.getRequestDetailHtml(requestId, parentId, opts)
  )
  ipcMain.handle('symphony:listCachedProcessKeys', (_e, profileId: string) =>
    getUsableCachedCatalog(profileId)
  )
  ipcMain.handle('symphony:listObservedProcessKeys', (_e, profileId: string) =>
    getObservedProcessKeys(profileId)
  )
  ipcMain.handle('symphony:refreshProcessKeys', (_e, force?: boolean) =>
    ensureCatalog({ force: force === true })
  )
  ipcMain.handle('symphony:searchProcessKeys', (_e, nameLike: string) =>
    searchProcessKeys(nameLike)
  )

  ipcMain.handle('symphony:deepSearch:list', () => listSweeps())
  ipcMain.handle('symphony:deepSearch:snapshot', (_e, jobId: string) => getSweepSnapshot(jobId))
  ipcMain.handle('symphony:deepSearch:create', (_e, input: CreateSweepInput) => createSweep(input))
  ipcMain.handle('symphony:deepSearch:update', (_e, jobId: string, patch: UpdateSweepPatch) =>
    updateSweep(jobId, patch)
  )
  ipcMain.handle('symphony:deepSearch:start', (_e, jobId: string) => startSweep(jobId))
  ipcMain.handle('symphony:deepSearch:pause', (_e, jobId: string) => pauseSweep(jobId))
  ipcMain.handle('symphony:deepSearch:delete', (_e, jobId: string) => deleteSweep(jobId))

  ipcMain.handle('settings:getStore', () => getStore())
  ipcMain.handle('settings:saveProfile', (_e, profile: Profile) => saveProfile(profile))
  ipcMain.handle('settings:deleteProfile', (_e, id: string) => deleteProfile(id))
  ipcMain.handle('settings:setActiveProfile', (_e, id: string) => {
    // Pause first: a running sweep resolves its base URL and token from the
    // ACTIVE profile at request time, so it must stop before the switch lands.
    pauseAllForProfileSwitch()
    setActiveProfile(id)
    invalidateToken()
  })

  ipcMain.handle('savedDomains:list', () => listSavedDomains())
  ipcMain.handle('savedDomains:save', (_e, input: { id?: string; name: string; domain: string }) =>
    saveSavedDomain(input)
  )
  ipcMain.handle('savedDomains:remove', (_e, id: string) => removeSavedDomain(id))

  ipcMain.handle('savedTabSets:list', (_e, profileId: string) => listSavedTabSets(profileId))
  ipcMain.handle(
    'savedTabSets:save',
    (_e, input: { id?: string; profileId: string; name: string; tabs: unknown[] }) =>
      saveSavedTabSet(input)
  )
  ipcMain.handle('savedTabSets:remove', (_e, id: string) => removeSavedTabSet(id))

  ipcMain.handle('uiPrefs:getAll', () => getUiPrefs())
  ipcMain.handle('uiPrefs:set', (_e, key: string, value: unknown) => setUiPref(key, value))

  ipcMain.handle('updater:quitAndInstall', () => quitAndInstall())
}
