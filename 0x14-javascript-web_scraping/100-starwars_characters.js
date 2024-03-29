#!/usr/bin/node
const { get } = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
get(url, null, (_, res) => {
  const people = JSON.parse(res.body).characters;
  people.forEach((personUrl) => {
    get(personUrl, null, (_, personRes) => {
      const person = JSON.parse(personRes.body);
      console.log(person.name);
    });
  });
});
