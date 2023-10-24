#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    throw err;
  }
  const data = JSON.parse(body);
  const dict = {};
  for (const task of data) {
    if (task.completed === true) {
      if (dict[task.userId] === undefined) {
        dict[task.userId] = 1;
      } else {
        dict[task.userId] += 1;
      }
    }
  }
  console.log(dict);
});
