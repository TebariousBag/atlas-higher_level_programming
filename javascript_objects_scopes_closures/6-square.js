#!/usr/bin/node
// class inherits Square from 5-square.js
// require from 5-square.js
const five_square = require('./5-square');

// create and inherit from five_square
class Square extends five_square {
  // print c in a square
  charPrint (c) {
	// if no c, then use X
	if (c === undefined) {
	  c = 'X';
	}
	// iterate through height, and print width times
	for (let i = 0; i < this.height; i++) {
		// printing c, if it was not defined then X
	  console.log(c.repeat(this.width));
	}
  }
}

// export class
module.exports = Square;
