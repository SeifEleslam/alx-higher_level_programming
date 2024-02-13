#!/usr/bin/node

// prettier-ignore
const Rectangle = require('./4-rectangle');

// prettier-ignore
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
