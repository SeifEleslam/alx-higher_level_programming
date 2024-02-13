#!/usr/bin/node

// prettier-ignore
const ParentSquare = require('./5-square');

// prettier-ignore
class Square extends ParentSquare {

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
