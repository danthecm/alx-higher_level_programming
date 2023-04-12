#!/usr/bin/node

const argvLength = process.argv.length;

if (argvLength < 4) {
  console.log(0);
} else {
  const numbers = [];
  for (let i = 2; i < argvLength; i++) {
    numbers.push(parseInt(process.argv[i]));
  }
  numbers.sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
}
