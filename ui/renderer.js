const windowApi = window.api;

// source button clicked
document.querySelector("#srcBtn").addEventListener('click', async ()=> {
    // send to ipcMain.("openExplorer")
    await windowApi.invoke("openExplorer").then(receivedData => {
        // promise was returned
        console.log("received info");
        // fill source input with selected folder
        document.querySelector("#srcInput").value = receivedData;
    });
});

// destination button clicked
document.querySelector("#destBtn").addEventListener('click', async ()=> {
    // send to ipcMain.("openExplorer")
    await windowApi.invoke("openExplorer").then(receivedData => {
        // promise was returned
        console.log("received info");
        // fill destination input with selected folder
        document.querySelector("#destInput").value = receivedData;
    });
});

window.addEventListener('load', (event) => {
    console.log('page is fully loaded');

    // new task button clicked
    document.querySelector("#newTaskBtn").addEventListener('click', async ()=> {
        var name = getName();
        var startTime = getStartTime();
        var daysOfWeekArray = getDaysOfWeek();
        var srcPath = getSrcPath();
        var destPath = getDestPath();
        var desiredFiles = getFileTypes();
        var newFileName = getNewFileName();

        // package arguments for data_storage main
        let data = windowApi.packageData("../model/data_storage.py", name, startTime, daysOfWeekArray, srcPath, destPath, desiredFiles, newFileName);
        // send data to ipcMain.("runDataStorage")
        await windowApi.invoke("runDataStorage", data).then(receivedData => {
            if(receivedData.includes("All fields must be filled")){
                alert(receivedData);
            } else{
                alert("Successfully added task")
            }
        });
    });
});

function getName() {
    return document.querySelector("#nameInput").value;
}
function getSrcPath() {
    return document.querySelector("#srcInput").value;
}
function getDestPath() {
    return document.querySelector("#destInput").value;
}
function getNewFileName() {
    return document.querySelector("#newFileNameInput").value;
}

/**
 * returns array of start time info
 * startTime[0]: hour
 * startTime[1]: min
 * startTime[2]: AM or PM
 */
function getStartTime() {
    var startTime = [];
    startTime.push(document.querySelector("#hour").value);
    startTime.push(document.querySelector("#mins").value);
    startTime.push(document.querySelector(".twelve-hour-clock button.selected").innerText);
    return startTime;
}

/**
 * returns array of selected days in text
 * monday = 0, ..., sunday = 6
 */
function getDaysOfWeek() {
    var week = document.querySelector(".week");
    var days = week.getElementsByClassName("day");

    const selectedDaysArr = [];

    // find selected days
    for(let i = 0; i < days.length; i++){
        if(days[i].classList.contains("selected")){
            selectedDaysArr.push(i);
        }
    }
    return selectedDaysArr;
}

// returns array of file types
function getFileTypes() {
    const fileTypes = [];

    // get all label buttons for keywords
    var keywords = document.querySelector(".keywords").getElementsByClassName("labelBtn");
    for(let i = 0; i < keywords.length; i++){
        // extract text from label button
        var inner = keywords[i].innerHTML;
        inner = inner.split("&nbsp;");
        if(inner[0] === 'all'){
            fileTypes.push("*");
        } else{
            fileTypes.push(inner[0]);
        }
    }

    // get all label buttons for extensions
    var extensions = document.querySelector(".extensions").getElementsByClassName("labelBtn");
    for(let i = 0; i < extensions.length; i++){
        // extract text from label button
        var inner = extensions[i].innerHTML;
        inner = inner.split("&nbsp;");
        if(inner[0] === 'all'){
            fileTypes.push(".*");
        } else if(inner[0].charAt(0) != '.'){
            // prepend . to extension if not there
            fileTypes.push('.' + inner[0]);
        } else{
            fileTypes.push(inner[0]);
        }
    }
    return fileTypes;
}