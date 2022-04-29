$(document).ready(function(){
    fillTime();

    // day selected
    $(".week .day").on("click", function(){
        $(this).toggleClass("selected");
        console.log("toggled");
    });

    // AM vs PM selected
    $(".details .twelve-hour-clock button").on("click", function(){
        $(".details .twelve-hour-clock button").each(function(){
            $(this).toggleClass("selected");
        });
        console.log("toggled");
    });
});

function fillTime(){
    // fill hours selection dropdown
    for(let i = 1; i <= 12; i++){
        var option = "<option>" + i + "</option>";
        $(".details .time .hour").append(option);
    }

    // fill hours selection dropdown
    for(let i = 0; i <= 59; i++){
        if(i < 10){
            var option = "<option>0" + i + "</option>";
        } else{
            var option = "<option>" + i + "</option>";
        }
        $(".details .time .mins").append(option);
    }
}