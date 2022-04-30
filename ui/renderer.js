const windowApi = window.api;

document.querySelector("#srcBtn").addEventListener('click', async ()=> {
    await windowApi.invoke("openExplorer").then(receivedData => {
        console.log("received info");
        document.querySelector("#srcInput").value = receivedData;
    });
});

document.querySelector("#destBtn").addEventListener('click', async ()=> {
    await windowApi.invoke("openExplorer").then(receivedData => {
        console.log("received info");
        document.querySelector("#destInput").value = receivedData;
    });
});

window.addEventListener('load', (event) => {
    console.log('page is fully loaded');

    // adding new task
    document.querySelector("#newTaskBtn").addEventListener('click', async ()=> {
        var name = getName();
        var startTime = getStartTime();
        var srcPath = getSrcPath();
        var destPath = getDestPath();
        var daysOfWeekArray = getDaysOfWeek();
        var desiredFiles = getFileTypes();
        var newFileName = getNewFileName();

        let data = windowApi.packageData("../data_storage.py", name, startTime, daysOfWeekArray, srcPath, destPath, desiredFiles, newFileName);
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

function getStartTime() {
    var startTime = [];
    startTime.push(document.querySelector("#hour").value);
    startTime.push(document.querySelector("#mins").value);

    var val = document.querySelector(".twelve-hour-clock button.selected");
    if(val.innerText == 'PM'){
        startTime.push(true);
    } else{
        startTime.push(false);
    }
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
    console.log(selectedDaysArr);
    return selectedDaysArr;
}

function getFileTypes() {
    const fileTypes = [];
    var keywords = document.querySelector(".keywords").getElementsByClassName("labelBtn");
    for(let i = 0; i < keywords.length; i++){
        var inner = keywords[i].innerHTML;
        inner = inner.split("&nbsp;");
        if(inner[0] === 'all'){
            fileTypes.push("*");
        } else{
            fileTypes.push(inner[0]);
        }
    }

    var extensions = document.querySelector(".extensions").getElementsByClassName("labelBtn");
    for(let i = 0; i < extensions.length; i++){
        var inner = extensions[i].innerHTML;
        inner = inner.split("&nbsp;");
        if(inner[0] === 'all'){
            fileTypes.push(".*");
        } else if(inner[0].charAt(0) != '.'){
            fileTypes.push('.' + inner[0]);
        } else{
            fileTypes.push(inner[0]);
        }
    }
    console.log(fileTypes);
    return fileTypes;
}