$(document).ready(function () {
  $('input#btn_translate').click(function (e) {
    const lang = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      success: (res) => {
        $('div#hello').html(res.hello);
      },
    });
  });
});
