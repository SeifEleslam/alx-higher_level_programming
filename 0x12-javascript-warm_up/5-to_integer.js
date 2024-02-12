#!/usr/bin/node
console.log(
  !isNaN(process.argv[2]) ? parseInt(process.argv[2]) : 'Not a number'
);
