#!/usr/bin/node
// import fs built in
const fs = require('fs');
// get arg2 from command line
const filePath = process.argv[2];
// the data to write
const data = process.argv[3];
// write the file, unless error occuers
fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) {
	console.log(err);
  }
});
