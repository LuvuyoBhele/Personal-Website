$(document).ready(function(){
    console.log('App.js loaded');
});

$('.card').mouseover(
  function(){
  $(this).addClass('onHover')
    console.log('hovered');
})

$('.card').click(
  function(){
  $(this).addClass('onHover')
    console.log('hovered');
})

$('.card').mouseout(
  function(){
    $(this).removeClass('onHover')}
);

document.getElementById('card-1').addEventListener('click', function() {
  window.location.href = 'https://github.com/LuvuyoBhele/bill-please';
});

document.getElementById('card-2').addEventListener('click', function() {
  window.location.href = 'https://github.com/LuvuyoBhele/Breaking-an-encryption';
});