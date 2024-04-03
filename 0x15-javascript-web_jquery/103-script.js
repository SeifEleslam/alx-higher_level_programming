const submit_code = () => {
  const lang = $('input#language_code').val();
  $.ajax({
    type: 'GET',
    url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
    success: (res) => {
      $('div#hello').html(res.hello);
    },
  });
};
$(document).ready(function () {
  $('input#btn_translate').click(submit_code);
  $('input#language_code').keypress(function (e) {
    if (e.which == 13) {
      $('input#btn_translate').trigger('click');
    }
  });
});
