#!/usr/bin/node
// import request built in
const requesting = require('request');
// get url from command line
const url = process.argv[2];
// make a request to GET url, unless error
requesting(url, (error, response) => {
  if (error) {
    console.error('code:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
