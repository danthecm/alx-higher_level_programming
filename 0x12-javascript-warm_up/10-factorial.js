#!/usr/bin/node
const input = parseInt(process.argv[2]);
function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(input));
