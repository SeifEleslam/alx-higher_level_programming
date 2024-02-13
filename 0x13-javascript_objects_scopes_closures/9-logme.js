#!/usr/bin/node

let test = 0;
// prettier-ignore
exports.logMe = function (item) {
  console.log(`${test}: ${item}`);
  test++;
}
