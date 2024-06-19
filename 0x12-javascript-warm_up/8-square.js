#!/usr/bin/node

// process.argv -> [nodeDir, jsFileDir, args...]
const myArgv = process.argv;

if (isNaN(myArgv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(myArgv[2]);

  let i = 0;
  while (i < x) {
    // Draw a line for each loop
    let line = '';

    let j = 0;
    while (j < x) {
      line += 'X';
      j++;
    }
    console.log(line);
    i++;
  }
}
