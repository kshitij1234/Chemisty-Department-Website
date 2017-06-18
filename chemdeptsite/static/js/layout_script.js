$(document).ready(function () {

    var loc = window.location.href;
    //alert(loc);
    $("#home").addClass("active");

    if(loc.indexOf("people")!=-1){
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