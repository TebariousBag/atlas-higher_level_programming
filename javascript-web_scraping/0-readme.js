#!/usr/bin/node
// import fs builtt in
const fs = require('fs');
// get arg2 from command line
const file = process.argv[2];
// read the file, unless error occuers
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
