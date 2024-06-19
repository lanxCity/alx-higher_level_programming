#!/usr/bin/node

// process.argv -> [nodeDir, jsFileDir, args...]
const myArgv = process.argv;

if (isNaN(myArgv[2])) {
  console.log('Missing number of occurences');
} else {
  const x = parseInt(myArgv[2]);

  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
