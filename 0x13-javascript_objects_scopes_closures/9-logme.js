#!/usr/bin/node
let exec = 0;
exports.logMe = function (item) {
  console.log(`${exec}: ${item}`);
  exec++;
};
