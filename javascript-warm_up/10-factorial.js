#!/usr/bin/node
// start at first argument of command line
const args = process.argv.slice(2);
// convert arg to int
const num = parseInt(args[0]);
// function factorial(num)
function factorial (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
// print result
console.log(factorial(num));
