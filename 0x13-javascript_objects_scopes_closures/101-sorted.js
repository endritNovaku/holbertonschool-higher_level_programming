#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  if (!newDict.hasOwnProperty(dict[key])) {
    newDict[dict[key]] = [];
  }
}

for (const key in dict) {
  if (newDict.hasOwnProperty(dict[key])) {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
