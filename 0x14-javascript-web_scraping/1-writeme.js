#!/usr/env/node
const fs = require('fs');
const filepath = process.argv[1];
const data = process.argv[2];

fs.writeFile(filepath, data, 'utf8', function (err) {
  if (err) {
    throw err;
  }
});
