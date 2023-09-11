#!/usr/bin/node
const numbers = process.argv.slice(2).map(Number);
numbers.sort((a, b) => b - a);
if (numbers.length < 2) {
  console.log(0);
} else {
  console.log(numbers[1]);
}
