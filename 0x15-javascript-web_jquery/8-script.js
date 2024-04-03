$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (res) => {
    res.results.forEach((movie) => {
      $('ul#list_movies').append(`<li>${movie.title}</li>`);
    });
  },
});
