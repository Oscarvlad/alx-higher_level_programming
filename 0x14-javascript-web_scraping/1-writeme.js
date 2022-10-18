#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
fs.appendFile(args[2], args[3], 'utf8', (err) => {
  if (err) throw err;
});
