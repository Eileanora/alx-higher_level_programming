#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file_path = process.argv[3];
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    fs.writeFile(file_path, body, 'utf8', function (err2) {
      if (err2) {
        throw err2;
      }
    });
  }
});
