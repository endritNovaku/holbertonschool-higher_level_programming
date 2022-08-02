#!/usr/bin/node

let i = 0;
function increment (n) {
  n++;
  return n;
}
exports.logMe = function (item) {
  console.log(i + ':', item);
  i = increment(i);
};
