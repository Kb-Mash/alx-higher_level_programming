#!/usr/bin/node

let arr = process.argv.slice(2).map((x) => {
  return parseInt(x);
});

if (arr.length <= 1) {
  console.log(0);
} else {
  console.log(arr.sort((a, b) => {
    return b - a;
  })[1]);
}
