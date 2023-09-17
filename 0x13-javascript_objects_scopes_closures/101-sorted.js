#!/usr/bin/node

const list = require('./101-data').dict;
const sorted_dict = {};

Object.keys(list).forEach(key => {
  if (sorted_dict[list[key]] === undefined) sorted_dict[list[key]] = [];

  sorted_dict[list[key]].push(key);
});

console.log(sorted_dict);
