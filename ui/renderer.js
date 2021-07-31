
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

// returns array of selected days in text
function getDaysOfWeek() {
    var week = document.getElementsByClassName("week");
    var selectedDays = week[0].getElementsByClassName("selected");
    var selectedDaysArr = Array.from(selectedDays).map((day) => day.innerText);
    console.log(selectedDaysArr);
    return selectedDaysArr;
}

window.addEventListener('load', (event) => {
    console.log('page is fully loaded');

    // adding new task
    var newTask = document.querySelector("newTask");
    newTask.addEventListener('click', async ()=> {
       var daysOfWeekArray = getDaysOfWeek();
    });
});