#!/usr/bin/node
const { get } = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function callbackPerson(people, idx) {
  if (idx < people.length)
    get(people[idx], null, (_, personRes) => {
      const person = JSON.parse(personRes.body);
      console.log(person.name);
      callbackPerson(people, idx + 1);
    });
}

get(url, null, (_, res) => {
  const people = JSON.parse(res.body).characters;
  callbackPerson(people, 0);
});
