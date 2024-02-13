#!/usr/bin/node
let res = -Infinity;
let largest = 0;
if (process.argv.length > 3) {
  for (let i = 2; i < process.argv.length; i++) {
    if (+process.argv[i] > largest) {
      res = largest;
      largest = +process.argv[i];
    } else if (process.argv[i] > res) {
      res = +process.argv[i];
    }
  }
} else res = 0;
console.log(res);
