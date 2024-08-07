window.onload = () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';

  $('INPUT#btn_translate').click(() => {
    $.ajax({
      url: url + $('INPUT#language_code').val(),
      type: 'GET',
      dataType: 'json'
    }).done((json) => {
      $('DIV#hello').text(json.hello);
    });
  });
};
