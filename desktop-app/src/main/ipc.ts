import { ipcMain } from 'electron'
import * as odoo from './backend/odoo'
import * as devops from './backend/devops'
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

  ipcMain.handle('settings:getStore', () => getStore())
  ipcMain.handle('settings:saveProfile', (_e, profile: Profile) => saveProfile(profile))
  ipcMain.handle('settings:deleteProfile', (_e, id: string) => deleteProfile(id))
  ipcMain.handle('settings:setActiveProfile', (_e, id: string) => {
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

  ipcMain.handle('updater:quitAndInstall', () => quitAndInstall())
}
