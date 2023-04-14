#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const score = parseInt(dict[key]);
  console.log(typeof score);
  if (!Object.hasOwnProperty.call(newDict, score)) {
    Object.assign(newDict, { [score]: [] });
  }
  newDict[score].push(parseInt(key));
}
