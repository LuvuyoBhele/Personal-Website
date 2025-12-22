$(document).ready(function(){
    console.log('App.js loaded');
});

$('.card').hover(
  function(){
  $(this).addClass('onHover')
    console.log('hovered');
},
  function(){
    $(this).removeClass('onHover')}
);