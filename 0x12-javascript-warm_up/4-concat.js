#!/usr/bin/node

// process.argv -> [nodeDir, jsFileDir, args...]
const myArgv = process.argv;

console.log(myArgv[2] + ' is ' + myArgv[3]);
