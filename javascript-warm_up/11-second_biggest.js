#!/usr/bin/node
// extract args except first 2
let args = process.argv.slice(2);
// convert args to Number
args = args.map(Number);
// if no args print 0
if (args.length < 2) {
  console.log(0);
} else {
  // sort args ascending
  const sorted = args.sort((a, b) => a - b);
  // print the next to last
  // which is the second biggest
  console.log(sorted[sorted.length - 2]);
}
