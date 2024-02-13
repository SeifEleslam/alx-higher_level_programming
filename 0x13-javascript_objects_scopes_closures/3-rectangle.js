#!/usr/bin/node

// prettier-ignore
class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) return;
    this.width = w;
    this.height = h;
  }
  print () {
    if (!this.width || !this.height) return;
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
