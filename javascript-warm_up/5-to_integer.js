#!/usr/bin/node
// start at first argument of command line
const args = process.argv.slice(2);
// convert arg to int
const int = parseInt(args[0]);
// if NotaNumber, print Not a number
// else print the number
if (isNaN(int)) {
  console.log('Not a number');
} else {
	  console.log(`My number: ${int}`);
}
