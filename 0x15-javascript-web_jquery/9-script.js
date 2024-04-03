$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (res) => {
      $('div#hello').html(res.hello);
    },
  });
});
