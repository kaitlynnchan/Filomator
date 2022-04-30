// https://www.electronjs.org/docs/tutorial/quick-start


const path = require('path');
const { app, browser, BrowserWindow, ipcMain, ipcRenderer } = require('electron');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            contextIsolation: true,
            nodeIntegration: false,
            enableRemoteModule: false,
            // Loading the preloader
            // - __dirname = path of the script
            preload: path.join(__dirname, 'preload.js')
        }
    })

    // Loading html file
    win.loadFile('index.html');
}

app.whenReady().then(() => {
    createWindow();

    // Open a window if none are open (macOS)
    app.on('activate', function() {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    })
})

// Closing the app in Windows / Linux when all windows are closed
app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit();
})

ipcMain.on("openExplorer", (event, args) => {
    const { dialog } = require('electron');

    // open dialog box
    dialog.showOpenDialog({ properties: ['openDirectory'] }).then(result => {
        console.log(result.canceled);
        console.log(result.filePaths);

        // convert result to Buffer object
        let val = [];
        val.push(Buffer.from(result.filePaths[0]));

        // return value
        event.reply('openExplorer', Buffer.concat(val));
    }).catch(err => {
        console.log(err)
    });
});

ipcMain.handle("openExplorer", async (event, args) => {
    return new Promise(resolve => {
        const { dialog } = require('electron');

        // open dialog box
        dialog.showOpenDialog({ properties: ['openDirectory'] }).then(result => {
            console.log(result.canceled)
            console.log(result.filePaths)

            // convert result to Buffer object
            let val = [];
            val.push(Buffer.from(result.filePaths[0]));

            // return value
            resolve(Buffer.concat(val));
        }).catch(err => {
            console.log(err)
        });
    });
});


ipcMain.on("runDataStorage", (event, args) => {
    // create arguments to execute
    var python = require('child_process').spawn('python', args.slice());
    let result = [];

    // For receiving data (receives as a readable stream)
    // - can be decoded into a string.
    python.stdout.on('data', function (data) {
        console.log("Python response: ", data);
        result.push(Buffer.from(data));
    });
    python.stdout.on('end', function() {
        event.reply('runDataStorage', Buffer.concat(result));
    });

    // Error handling
    python.stderr.on('data', (data) => {
        console.error(result);
        event.reply('runDataStorage', data);
    });

    python.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });
});

ipcMain.handle("runDataStorage", async (event, args) => {
    return new Promise(resolve => {
        var python = require('child_process').spawn('python', args.slice());
        let result = [];

        // For receiving data (receives as a readable stream)
        // - can be decoded into a string.
        python.stdout.on('data', function (data) {
            console.log("Python response: ", data);
            result.push(Buffer.from(data));
        });
        python.stdout.on('end', function() {
            resolve(Buffer.concat(result));
        });

        // Error handling
        python.stderr.on('data', (data) => {
            console.error(result);
            return data;
        });

        python.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
        });
    });
});