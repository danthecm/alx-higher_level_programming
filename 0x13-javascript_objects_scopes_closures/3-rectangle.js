#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rep = '';
      for (let j = 0; j < this.width; j++) {
        rep += 'X';
      }
      console.log(rep);
    }
  }
}
module.exports = Rectangle;
