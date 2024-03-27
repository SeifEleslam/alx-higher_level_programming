#!/usr/bin/node
const { get } = require('request');

const url = process.argv[2];
get(url, null, (_, res) => {
  const movies = JSON.parse(res.body).results;
  console.log(
    movies.filter((movie) =>
      movie.characters.some((char) => char.includes('/18/'))
    ).length
  );
});
