#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
fs.readFile(args[2], 'utf8', (data, err) => {
  if (err) {
    console.log(err);
    return;
  }
  if (data === null) {
    console.log('');
    return;
  }
  console.log(data);
});
