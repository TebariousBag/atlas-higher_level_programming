#!/usr/bin/node
// import request built in
const request = require('request');
// get url from command line
const url = process.argv[2];
// id to count
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
  // for each film, count character
  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes(`/api/people/${id}/`)) {
        count++;
      }
    });
  });

  console.log(count);
});
