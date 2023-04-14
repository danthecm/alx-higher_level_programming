#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char = 'X') {
    for (let i = 0; i < this.height; i++) {
      const rep = char.repeat(this.height);
      console.log(rep);
    }
  }
}
module.exports = Square;
