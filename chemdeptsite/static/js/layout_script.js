$(document).ready(function () {

    var loc = window.location.href;
    //alert(loc);
    $("#home").addClass("active");
<<<<<<< HEAD
    if(loc.contains("people")){
        PeopleClicked();
    }
=======

    if(loc.indexOf("people")!=-1){
        PeopleClicked();
    }

>>>>>>> c13e0148caacb8fff4034b3b2d0d1befb0d0a278
});

function PeopleClicked() {

    RemoveActive();
    $("#people").addClass("active");

}

function RemoveActive() {
    $(".navigator").removeClass("active");
}
