#!/usr/bin/node
const files = process.argv.slice(2, 4);
const dest = process.argv[4];

const fs = require('fs');

files.forEach((file) => {
  fs.readFile(`./${file}`, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.appendFile(dest, data, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
