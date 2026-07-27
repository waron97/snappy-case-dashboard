import { ipcMain } from 'electron'
import * as odoo from './backend/odoo'
import * as devops from './backend/devops'
import { getSettings, saveSettings, type Settings } from './backend/settings'

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

  ipcMain.handle('settings:get', () => getSettings())
  ipcMain.handle('settings:save', (_e, settings: Settings) => saveSettings(settings))
}
