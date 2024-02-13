#!/usr/bin/node

// prettier-ignore
const ParentSquare = require('./5-square');

// prettier-ignore
class Square extends ParentSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
