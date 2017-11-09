$(document).ready(function(){
  var research = document.getElementsByClassName('research-areas');

$(".info-btn").click(function () {

  var id = this.getAttribute("id");
  var num = parseInt(id.substring(4))-1;
   $(research[num]).removeClass("hidden");
   $(research[num]).addClass("animated slideInRight");
  // $(research[num]).modal('toggle');
});

});
