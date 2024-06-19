#!/usr/bin/node

// process.argv -> [nodeDir, jsFileDir, args...]
const myArgv = process.argv;

const a = parseInt(myArgv[2]);
const b = parseInt(myArgv[3]);

const add = (a, b) => a + b;
console.log(add(a, b));
