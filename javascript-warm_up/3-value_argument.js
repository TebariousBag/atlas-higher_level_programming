#!/usr/bin/node
// start at first argument of command line
const args = process.argv.slice(2);
// if no arg
if (args[0] === undefined) {
  console.log('No argument');
// if arg than print arg
} else {
  console.log(args[0]);
}
