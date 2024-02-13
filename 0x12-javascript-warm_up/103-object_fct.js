#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
};
console.log(myObject);

// prettier-ignore
function addOne() {
  this.value++;
}
myObject.incr = addOne;
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
