$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: (res) => {
    $('div#character').html(res.name);
  },
});
