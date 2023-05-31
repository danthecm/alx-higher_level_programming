$.get(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    data.results.forEach((result) => {
      $('UL#list_movies').append($('<li></li>').text(result.title));
    });
  }
);
