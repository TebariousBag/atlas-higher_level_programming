#!/usr/bin/node
// start at first argument of command line
const args = process.argv.slice(2);
// print 2 arguments
// since we slice at 2, we use args[0] and args[1]
console.log(`${args[0]} is ${args[1]}`);
