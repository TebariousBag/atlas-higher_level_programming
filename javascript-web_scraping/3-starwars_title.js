#!/usr/bin/node
// import request built in
const requesting = require('request');
// get movie id
const movie = process.argv[2];
// the url we are accessing
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;
// make request to url, unless error
requesting(url, (error, response, body) => {
  if (error) {
	console.error(error);
  } else {
	console.log(JSON.parse(body).title);
  }
});
