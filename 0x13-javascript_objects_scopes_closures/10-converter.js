#!/usr/bin/node
exports.converter = function (base) {
  return function getNum (num) {
    return parseInt(num, 10).toString(base);
  };
};
