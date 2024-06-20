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
  print () {
    Rectangle.drawPlaneShape(this.width, this.height);
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

  /**
   * It draws any plane shape with two side
   */
  
  static drawPlaneShape (w, h) {
    for (let i = 0; i < h; i++) {
      let line = '';
      for (let j = 0; j < w; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}

module.exports = Rectangle;
