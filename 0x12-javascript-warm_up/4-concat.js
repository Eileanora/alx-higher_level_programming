#!/usr/bin/node
let s = "undefined";
let t = "undefined";
if (process.argv[2])
  s = process.argv[2];
if (process.argv[3])
  t = process.argv[3];
console.log(s + " is " + t);
