#!/usr/bin/node
// star at first argument of command line
const args = process.argv.slice(2);
// convert a and b to int
// index 0 and 1 since we slice 2
const a = parseInt(args[0]);
const b = parseInt(args[1]);

// function asked for
function add (a, b) {
	  return a + b;
}

// if a or b is NaN, print NaN
if (isNaN(a) || isNaN(b)) {
	  console.log('NaN');
} else {
	  console.log(add(a, b));
}
