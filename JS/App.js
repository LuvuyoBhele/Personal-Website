$(document).ready(function(){
    console.log('App.js loaded');
    if (window.jQuery) console.log('jQuery OK', $.fn.jquery);
    else console.log('jQuery NOT FOUND');

    $(".card").hover(
      function(){ $(this).css("background-color", "yellow"); },
      function(){ $(this).css("background-color", "pink"); }
    );
});