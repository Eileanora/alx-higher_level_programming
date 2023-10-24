#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    fs.writeFile(filePath, body, 'utf8', function (err2) {
      if (err2) {
        throw err2;
      }
    });
  }
});
