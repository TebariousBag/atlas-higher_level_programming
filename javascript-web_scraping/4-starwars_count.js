#!/usr/bin/node
// import request built in
const request = require('request');
// get url from command line
const url = process.argv[2];
// id we are looking for
const id = '18';
// make a request to GET url, unless error
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  // parse body
  const films = JSON.parse(body).results;
  let count = 0;
  // count goes up for each time id is found
  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${id}/`)) {
      count++;
    }
  });

  console.log(count);
});
