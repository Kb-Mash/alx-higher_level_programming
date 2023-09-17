#!/usr/bin/node

const SquareModel = require('./5-square');

module.exports = class Square extends SquareModel {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
