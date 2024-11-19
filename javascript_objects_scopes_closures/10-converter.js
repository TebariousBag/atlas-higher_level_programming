#!/usr/bin/node
// convert number from base 10 to another base
// function given
exports.converter = function (base) {
  // inner function to convert number
  return function (number) {
    // toString(base) nconverts it to base
    return number.toString(base);
  };
};
