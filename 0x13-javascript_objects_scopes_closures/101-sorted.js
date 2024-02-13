#!/usr/bin/node
// prettier-ignore
const dict = require('./101-data').dict;

const newDict = {};
Object.keys(dict).forEach((key) => {
  if (newDict[dict[key]]) newDict[dict[key]].push(key);
  else newDict[dict[key]] = [key];
});
console.log(newDict);
