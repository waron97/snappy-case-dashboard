import { app, type BrowserWindow } from 'electron'
import { autoUpdater } from 'electron-updater'

const CHECK_INTERVAL_MS = 4 * 60 * 60 * 1000

export function initAutoUpdater(getWindow: () => BrowserWindow | null): void {
  // electron-updater throws when the app isn't a packaged build (no
  // app-update.yml), which is always the case under `npm run dev`.
  if (!app.isPackaged) return

  autoUpdater.autoDownload = true
  autoUpdater.autoInstallOnAppQuit = false

  autoUpdater.on('update-downloaded', () => {
    getWindow()?.webContents.send('updater:update-downloaded')
  })
  autoUpdater.on('error', (err) => {
    console.error('[autoUpdater]', err)
  })

  const check = (): void => {
    autoUpdater.checkForUpdates().catch((err) => console.error('[autoUpdater] check failed', err))
  }

  check()
  setInterval(check, CHECK_INTERVAL_MS)
}

export function quitAndInstall(): void {
  autoUpdater.quitAndInstall()
}
