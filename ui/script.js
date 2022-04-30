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

    // add new values from input to keywords list
    $("#keyWInput").on("keydown", function(event){
        if(event.keyCode == 13) {
            var val = $(this).val();
            var labelBtn = "<button class='labelBtn' onclick='removeLabel(this)'>" + val + "&nbsp;<i class='fas fa-xmark'></i></button>";
            $(".keywords").append(labelBtn);
        }
    });

    // add new values from input to extensions list
    $("#extnInput").on("keydown", function(event){
        if(event.keyCode == 13) {
            var val = $(this).val();
            var labelBtn = "<button class='labelBtn' onclick='removeLabel(this)'>" + val + "&nbsp;<i class='fas fa-xmark'></i></button>";
            $(".extensions").append(labelBtn);
        }
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

// remove label from list
function removeLabel(element){
    element.remove();
}