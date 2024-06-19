#!/usr/bin/node

// process.argv -> [nodeDir, jsFileDir, args...]
const myArgv = process.argv;

if (isNaN(myArgv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myArgv[2]));
}
