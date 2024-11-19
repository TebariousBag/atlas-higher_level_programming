#!/usr/bin/node
// class square inherit from Rectangle
// require module 4-rectangle.js
const Rectangle = require('./4-rectangle');

// class Sqare extends all properties of Rectangle
class Square extends Rectangle {
  constructor (size) {
    // super calls the parent
    super(size, size);
  }
}
// export class
module.exports = Square;
