#!/usr/bin/node
let result = 1
for (let i = parseInt(process.argv[2]); i > 0; i--) {
	result *= i;
}

console.log(result);
