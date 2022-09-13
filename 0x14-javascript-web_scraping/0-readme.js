#!/usr/bin/node

const { readFileSync } = require('fs');

console.log(readFileSync(process.argv[2], 'utf-8'));
