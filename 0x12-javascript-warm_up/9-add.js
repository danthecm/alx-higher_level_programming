#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

const addition = add(num1, num2);
console.log(addition);
