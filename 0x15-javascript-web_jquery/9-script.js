$(document).ready(() => {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json'
  }).done((json) => {
    $('DIV#hello').text(json.hello);
  });
});
