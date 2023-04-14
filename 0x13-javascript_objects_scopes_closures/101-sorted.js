#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  if (!Object.hasOwnProperty.call(newDict, dict[key])) {
    newDict[dict[key]] = [];
  }

  newDict[dict[key]].push(key);
}
console.log(dict);
console.log(newDict);
