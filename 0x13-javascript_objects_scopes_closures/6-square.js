#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  /**
   * prints the rectangle using the character c
   * If c is undefined, use the character X
   */
  charPrint (c) {
    const line = !c ? 'X' : c;

    for (let i = 0; i < this.width; i++) {
      console.log(line.repeat(this.width));
    }
  }
}

module.exports = Square;
