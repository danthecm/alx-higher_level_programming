#!/usr/bin/node
const MySquare = require('./5-square');

class Square extends MySquare {
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
