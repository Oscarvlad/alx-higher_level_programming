/*
  fetches and lists all movies title by using this URL:
  https://swapi-api.hbtn.io/api/films/?format=json
*/
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data, textStatus) {
  data.results.map((movie) => $('UL#list_movies').append('<li>' + movie.title + '</li>'));
});
