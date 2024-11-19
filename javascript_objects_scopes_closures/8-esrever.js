#!/usr/bin/node
// function returns list reversed
exports.esrever = function (list) {
	  // variable to hold reversed list
  const reversed = [];
  // start at end of the list
  const listy = list.length - 1;
  // iterate backwards through the list
  for (let i = listy; i >= 0; i--) {
	// each time push the element to reversed
	reversed.push(list[i]);
  }
  // return backwards list
  return reversed;
};
