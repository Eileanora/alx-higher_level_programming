#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const charId = 18;
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (const result of results) {
      for (const character of result.characters) {
        if (character.includes(charId)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
