#!/usr/bin/node
const { get } = require('request');

get(process.argv[2], null, (err, res) => {
  console.log(`code: ${res.statusCode}`);
});
