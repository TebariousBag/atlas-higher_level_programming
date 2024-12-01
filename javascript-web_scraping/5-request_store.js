#!/usr/bin/node
// import request built in
const requesting = require('request');
// import fs built in
const fs = require('fs');
// get url from command line
const url = process.argv[2];
// get file path from command line
const file = process.argv[3];
// make a request to GET url, unless error
requesting(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // write file, unless error
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
