$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
}).done((json) => {
  const ul = $('UL#list_movies');
  const res = json.results;

  $.each(res, (index, entry) => {
    ul.append(`<li>${entry.title}</li>`);
  });
});
