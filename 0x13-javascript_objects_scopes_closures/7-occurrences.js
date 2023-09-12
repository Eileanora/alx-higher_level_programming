#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (const element of list) {
    if (element === searchElement) {
      cnt++;
    }
  }
  return cnt;
};
