$(document).ready(function(){

    // day selected
    $(".week .day").on("click", function(){
        $(this).toggleClass("selected");
        console.log("toggled");
    });

});
