#!/usr/bin/node
let biggestNum = 0;
let secondNum = 0;
for (let i = 2; process.argv[i] !== undefined; i++) {
  if (parseInt(process.argv[i]) > biggestNum) {
    biggestNum = parseInt(process.argv[i]);
  }
}
for (let i = 2; process.argv[i] !== undefined; i++) {
  if (parseInt(process.argv[i]) < biggestNum && secondNum < parseInt(process.argv[i])) {
    secondNum = parseInt(process.argv[i]);
  }
}
console.log(secondNum);
