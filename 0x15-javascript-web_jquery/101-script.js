$(document).ready(function () {
  $('div#add_item').click(function (e) {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(function (e) {
    $('ul.my_list').children().last().remove();
  });
  $('div#clear_list').click(function (e) {
    $('ul.my_list').html('');
  });
});
