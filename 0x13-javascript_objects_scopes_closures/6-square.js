#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let charToPrint = c;
    let width = '';
    let i = 0;
    if (c === undefined) {
      charToPrint = 'X';
    }
    while (i < this.width) {
      width += charToPrint;
      i++;
    }
    for (i = 0; i < this.height; i++) {
      console.log(width);
    }
  }
};
