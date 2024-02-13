#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
};
console.log(myObject);
const addOne = function () {
  this.value++;
}.bind(myObject);
myObject.incr = addOne;
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
