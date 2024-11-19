#!/usr/bin/node
// count args already printed
// and prin the current arg
let count = 0;

// function given
exports.logMe = function (item) {
	// print count, print item
	// remember bacckticks, not single quotes
  console.log(`${count}: ${item}`);
  // increment count
  count++;
};
