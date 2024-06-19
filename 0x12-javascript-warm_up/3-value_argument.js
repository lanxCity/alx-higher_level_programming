#!/usr/bin/node

// process.argv -> [nodeDir, jsFileDir, args...]
const myArgv = process.argv;

if (myArgv.length <= 2) {
  console.log('No argument');
} else {
  console.log(myArgv[2]);
}
