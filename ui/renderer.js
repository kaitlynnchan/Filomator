
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

window.addEventListener('load', (event) => {
    console.log('page is fully loaded');

    // adding new task
    var newTask = document.querySelector(".newTask");
    newTask.addEventListener('click', async ()=> {
       var daysOfWeekArray = getDaysOfWeek();
    });
});