#!/usr/bin/node
const { get } = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
get(url, null, (_, res) => {
  console.log(JSON.parse(res.body).title);
});
