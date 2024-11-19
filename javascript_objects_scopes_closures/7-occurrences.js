#!/usr/bin/node
// number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
	// variable to hold occurence
  let occur = 0;
  // iterate through list
  // if i is the element we are looking for
  // then increment occur
  for (const i of list) {
	if (i === searchElement) {
	  occur++;
	}
  }
  // return the number of occurrences
  return occur;
};
