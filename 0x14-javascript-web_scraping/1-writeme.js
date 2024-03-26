#!/usr/bin/node
const { writeFile } = require('fs');

writeFile(process.argv[2], process.argv[3], 'utf8', (err, _) => {
  if (err) console.log(err);
});
