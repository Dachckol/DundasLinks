var page = $("#pageID").data("page");
$("#"+page+"Nav").addClass("active");
if ($(window).width() > 768){
    $(".name h1 a").html("<img src='/static/img/logo.png'>");
}
