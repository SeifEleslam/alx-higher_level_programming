#!/usr/bin/node
const { get } = require('request');
const { writeFile } = require('fs');

const url = process.argv[2];
get(url, null, (_, res) => {
  writeFile(process.argv[3], res.body, 'utf8', () => {});
});
