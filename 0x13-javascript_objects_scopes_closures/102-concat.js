#!/usr/bin/node
const { readFileSync, writeFileSync } = require('fs');

const contents1 = readFileSync('./' + process.argv[2], 'utf-8');
const contents2 = readFileSync('./' + process.argv[3], 'utf-8');
writeFileSync('./' + process.argv[4], contents1 + contents2);
