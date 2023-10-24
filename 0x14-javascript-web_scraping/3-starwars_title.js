#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    console.log(JSON.parse(body).title);
  }
});
