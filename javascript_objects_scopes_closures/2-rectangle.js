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
}
// export class
module.exports = Rectangle;
