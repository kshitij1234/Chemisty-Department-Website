$(document).ready(function () {

    var loc = window.location.href;
    //alert(loc);
    $("#home").addClass("active");

    if(loc.contains("people")){
        PeopleClicked();
    }
    
});

function PeopleClicked() {

    RemoveActive();
    $("#people").addClass("active");

}

function RemoveActive() {
    $(".navigator").removeClass("active");
}