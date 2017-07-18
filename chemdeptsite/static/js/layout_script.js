$(document).ready(function () {
    var loc = window.location.href;
    var str = loc.split("/")[3];
    if(str.localeCompare("") == 0)
      $("#home").addClass("active");
    else
      $("#" + str).addClass("active");
    $('.carousel').carousel({
          dist:0,
          shift:0,
          padding:100,

    });
    $('.carousel').carousel('next');
});
