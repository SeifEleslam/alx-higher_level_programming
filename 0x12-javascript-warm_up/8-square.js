#!/usr/bin/node

for (let i = 0; i < +process.argv[2]; i++) {
  let x = '';
  for (let i = 0; i < +process.argv[2]; i++) x += 'X';
  console.log(x);
}
if (isNaN(process.argv[2])) console.log('Missing size');
