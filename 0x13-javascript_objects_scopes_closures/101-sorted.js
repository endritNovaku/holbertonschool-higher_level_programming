#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  if (!dict.hasOwnProperty(dict[key])) {
    newDict[dict[key]] = [];
  }
}

for (const key in dict) {
  if (dict.hasOwnProperty.call(dict[key])) {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
