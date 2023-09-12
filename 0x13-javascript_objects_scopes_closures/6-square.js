#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
