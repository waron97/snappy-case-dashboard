import { app, shell, BrowserWindow, Menu, type MenuItemConstructorOptions } from 'electron'
import { join } from 'path'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import icon from '../../resources/icon.png?asset'
import { registerIpcHandlers } from './ipc'
import { initAutoUpdater } from './updater'
import { initDeepSearch } from './backend/symphony/sweepEngine'
import { demoteInterruptedJobs } from './backend/symphony/sweepStore'

// Chromium picks its Linux password-store backend from XDG_CURRENT_DESKTOP.
// Launched without a desktop session exported — `npm run dev` from a plain
// terminal, tmux, ssh — that variable is missing, Chromium falls back to
// `basic_text`, and safeStorage.isEncryptionAvailable() goes false: settings
// written earlier with a keyring key then become unreadable, and anything saved
// afterwards would land on disk unencrypted. Naming the backend explicitly in
// that case keeps dev runs consistent with packaged ones. Must happen before
// the first password-store access, hence module scope.
if (process.platform === 'linux' && !process.env.XDG_CURRENT_DESKTOP) {
  app.commandLine.appendSwitch('password-store', 'gnome-libsecret')
}

let mainWindow: BrowserWindow | null = null

// Electron's implicit default menu (installed whenever setApplicationMenu is
// never called) binds CmdOrCtrl+W to the 'close' role, which closes the sole
// BrowserWindow and, via window-all-closed, quits the whole app. Rebuilding
// the same menu minus that item lets the renderer's own Ctrl+W handler (see
// lib/caseWorkspace.tsx) close just the active tab instead. Everything else
// here mirrors Electron's default template so Edit/View shortcuts (copy,
// paste, reload, devtools, zoom, mac Cmd+Q/Cmd+H) keep working.
function buildAppMenu(): void {
  const isMac = process.platform === 'darwin'

  const template: MenuItemConstructorOptions[] = [
    ...(isMac
      ? ([
          {
            label: app.name,
            submenu: [
              { role: 'about' },
              { type: 'separator' },
              { role: 'services' },
              { type: 'separator' },
              { role: 'hide' },
              { role: 'hideOthers' },
              { role: 'unhide' },
              { type: 'separator' },
              { role: 'quit' }
            ]
          }
        ] as MenuItemConstructorOptions[])
      : []),
    {
      label: 'Edit',
      submenu: [
        { role: 'undo' },
        { role: 'redo' },
        { type: 'separator' },
        { role: 'cut' },
        { role: 'copy' },
        { role: 'paste' },
        { role: 'selectAll' }
      ]
    },
    {
      label: 'View',
      submenu: [
        { role: 'reload' },
        { role: 'forceReload' },
        { role: 'toggleDevTools' },
        { type: 'separator' },
        { role: 'resetZoom' },
        { role: 'zoomIn' },
        { role: 'zoomOut' },
        { type: 'separator' },
        { role: 'togglefullscreen' }
      ]
    },
    {
      label: 'Window',
      submenu: [
        { role: 'minimize' },
        { role: 'zoom' },
        ...(isMac
          ? ([{ type: 'separator' }, { role: 'front' }] as MenuItemConstructorOptions[])
          : [])
      ]
    }
  ]

  Menu.setApplicationMenu(Menu.buildFromTemplate(template))
}

function createWindow(): void {
  // Create the browser window.
  const win = new BrowserWindow({
    width: 1440,
    height: 940,
    minWidth: 900,
    minHeight: 600,
    show: false,
    backgroundColor: '#242424',
    autoHideMenuBar: true,
    ...(process.platform === 'linux' ? { icon } : {}),
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })
  mainWindow = win

  win.on('ready-to-show', () => {
    win.show()
  })

  win.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url)
    return { action: 'deny' }
  })

  // HMR for renderer base on electron-vite cli.
  // Load the remote URL for development or the local html file for production.
  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    win.loadURL(process.env['ELECTRON_RENDERER_URL'])
  } else {
    win.loadFile(join(__dirname, '../renderer/index.html'))
  }
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  // Set app user model id for windows
  electronApp.setAppUserModelId('com.electron')

  buildAppMenu()

  // Default open or close DevTools by F12 in development
  // and ignore CommandOrControl + R in production.
  // see https://github.com/alex8088/electron-toolkit/tree/master/packages/utils
  app.on('browser-window-created', (_, window) => {
    optimizer.watchWindowShortcuts(window)
  })

  registerIpcHandlers()

  // Before the window exists: a sweep header left `running` by a crash or a
  // quit would otherwise render as a phantom job with a frozen progress bar.
  // A directory scan plus a few small reads — no network.
  demoteInterruptedJobs()

  createWindow()

  initAutoUpdater(() => mainWindow)
  initDeepSearch(() => mainWindow)

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
