#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((listItem) => {
    if (listItem === searchElement) {
      count++;
    }
  });
  return count;
};
