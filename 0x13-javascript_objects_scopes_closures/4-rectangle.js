#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * Prints the rectangle using the character X
   */
  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
    }
  }

  /**
   * Swaps the values of width and height of the rectangle
   */
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  /**
   * Multiples the width and the height of the rectangle by 2
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
