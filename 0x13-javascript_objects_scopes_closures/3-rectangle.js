#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let width = '';
    let i = 0;
    while (i < this.width) {
      width += 'X';
      i++;
    }
    for (i = 0; i < this.height; i++) {
      console.log(width);
    }
  }
};
