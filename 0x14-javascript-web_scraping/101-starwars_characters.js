#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, function (error, response, body) {
  if (error) {
    throw error;
  } else {
    const chars = JSON.parse(body).characters;
    for (const addr of chars) {
      request(addr, function (error, response, body) {
        if (error) {
          throw error;
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
