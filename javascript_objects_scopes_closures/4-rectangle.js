#!/usr/bin/node
// class rectangle, if w or h is = 0
// than create empty object
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // iterat through height
  // print X width times then repeate height times
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // rotate width and height
  // just swap values
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // double width and height
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
// export class
module.exports = Rectangle;
