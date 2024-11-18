#!/usr/bin/node
// start at first argument of command line
const args = process.argv.slice(2);
// convert arg to int
const num = parseInt(args[0]);
// if NotaNumber, print statement
if (isNaN(num))
	{
  console.log('Missing number of occurrences');
// iterate and print line num times
// use let so its used just  in the block
} else {
  for (let i = 0; i < num; i++)
		{
	console.log('C is fun');
  }
}
