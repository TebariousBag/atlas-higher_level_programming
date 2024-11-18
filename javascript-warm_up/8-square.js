#!/usr/bin/node
// start at first argument of command line
const args = process.argv.slice(2);
// convert arg to int
const num = parseInt(args[0]);
// if NotaNumber, print statement
if (isNaN(num))
{
  console.log('Missing size');
// iterate and print X, repeat num times
} else {
  for (let i = 0; i < num; i++)
  {
	console.log('X'.repeat(num));
  }
}
