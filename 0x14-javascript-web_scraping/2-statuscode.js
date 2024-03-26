#!/usr/bin/node
const { get } = require('request');

get(process.argv[2], null, (_, res) => {
  console.log(`code: ${res.statusCode}`);
});
