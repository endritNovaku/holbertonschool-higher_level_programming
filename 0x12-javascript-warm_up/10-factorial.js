#!/usr/bin/node
function factorial(){
	let result = 1;
	for (let i = parseInt(process.argv[2]); i > 0; i--) {
  	result *= i;
	}
	return result
}
console.log(factorial());
