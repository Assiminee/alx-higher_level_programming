const fetchHello = () => {
  const lang = $('INPUT#language_code').val();

  $.ajax({
    url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
    type: 'GET',
    dataType: 'json',
    success: (json) => {
      $('DIV#hello').text(json.hello);
    }
  });
};

$(document).ready(() => {
  $('INPUT#btn_translate').on('click', fetchHello);

  $('INPUT#language_code').on('keypress', (e) => {
    if (e.key === 'Enter') {
      fetchHello();
    }
  });
});
