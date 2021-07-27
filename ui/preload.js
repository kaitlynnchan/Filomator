// Browser window

const { BADHINTS } = require('dns');

window.addEventListener('DOMContentLoaded', ()=> {
    // Creating anonymous function to replaceText
    const replaceText = (selector, text) => {
        const element = document.getElementById(selector);
        if (element) {
            element.innerText = text;
        }
    }

    // Iterating through each HTML elements and replacing text
    // See: https://www.electronjs.org/docs/tutorial/process-model for process models
    for (const dependency of ['chrome', 'node', 'electron']) {
        replaceText(`${dependency}-version`, process.versions[dependency]);
    }
});


// For IPC communication
const {contextBridge, ipcRenderer} = require("electron");

// Set up communication from renderers to main process
// See: https://www.electronjs.org/docs/tutorial/process-model
// on ipcRenderer methods
contextBridge.exposeInMainWorld(
    "api", {
        send: (channel, data) => {
            // Setup channels to send toMain
            ipcRenderer.send(channel, data);
            
        },
        receive: (channel, receiveFunc) => {
                // Only include event when the receiveFunc needs to return backs
            ipcRenderer.on(channel, (event, ...args) => receiveFunc(...args)); 
        },

        // Try this soon?
        invoke: async (channel, data) => {
            return await ipcRenderer.invoke(channel, data).then(receivedData => {
                console.log("Decoding data");
                const result = new TextDecoder().decode(receivedData);
                console.log("Result of decode = " + result);
                return result;
            });
        },
        // Package input
        packageData: (pythonScript, ...args) => {
            return [pythonScript, ...args]
        }
    }
)


