/*
  adds, removes and clears LI elements from a list when the user clicks
*/
$(document).ready(() => {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list LI').slice(-1).remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list LI').remove();
  });
});
