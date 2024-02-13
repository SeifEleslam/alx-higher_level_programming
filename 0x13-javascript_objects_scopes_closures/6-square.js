#!/usr/bin/node

// prettier-ignore
const Rectangle = require('./4-rectangle');

// prettier-ignore
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
