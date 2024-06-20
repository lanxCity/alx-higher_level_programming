#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  /**
   * prints the rectangle using the character c
   * If c is undefined, use the character X
   */
  charPrint (c) {
    !c ? super.print() : super.print(c);
  }
}

module.exports = Square;
