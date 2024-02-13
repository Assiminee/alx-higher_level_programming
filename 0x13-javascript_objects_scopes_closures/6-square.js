#!/usr/bin/node

const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
