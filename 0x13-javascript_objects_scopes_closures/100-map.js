#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((item, index) => {
  return item * index;
});
console.log(list);
console.log(newList);
