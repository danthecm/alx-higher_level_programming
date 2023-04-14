#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const score = dict[key];
  if (!Object.hasOwnProperty.call(newDict, score)) {
    newDict[score] = [];
  }
  newDict[score].push(key);
}

console.log(newDict);
