
//const windowApi = window.api;
//
//button.addEventListener('click', async ()=> {
//    let data = windowApi.packageData("python/calc.py", input.value);
//    // window.api.send("toMain", data);
//    await windowApi.invoke("toMain", data).then(receivedData => {
//        result.textContent = receivedData;
//    });
//});
//
//button.dispatchEvent(new Event('click'));

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
        // name, start_time, end_time, days_of_week, source_path, dest_path, desired_files, new_file_name
        // write_to_json(argv[0], start_time, end_time, argv[2], argv[3], argv[4], argv[5], argv[6])
        var name = getName();
        var startTime = getStartTime();
        var srcPath = getSrcPath();
        var destPath = getDestPath();
//        var endTime = getEndTime();
        var daysOfWeekArray = getDaysOfWeek();
//        var desiredFiles = getFileTypes();
        var newFileName = getNewFileName();
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
    startTime.append(document.querySelector("#hour").value);
    startTime.append(document.querySelector("#mins").value);

    var val = document.querySelector(".twelve-hour-clock .selected");
    if(val[0].textContent == 'PM'){
        startTime.append(true);
    } else{
        startTime.append(false);
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
    var keywords = document.querySelector(".keywords").children();
    for(let i = 0; i < keywords.length; i++){
//    check if its all
//        strip html, space and icon
//        if(keywords[i].innerHTML ){
//            fileTypes.push(i);
//        }
    }

    var extensions = document.querySelector(".extensions").children();
    for(let i = 0; i < extensions.length; i++){
//    check if its all
//        strip html, space and icon
//        if(extensions[i].innerHTML ){
//            fileTypes.push(i);
//        }
    }
    console.log(fileTypes);
    return fileTypes;
}