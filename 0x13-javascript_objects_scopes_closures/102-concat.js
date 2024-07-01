#!/usr/bin/node

const myArgv = process.argv;

if (myArgv.length > 3) {
  const fs = require('fs');
  // File A
  const fileAPath = myArgv[2];
  let fileA = '';

  fs.readFile(fileAPath, 'utf8', (err, data) => {
    if (err) {
      console.log("Error: FileA");
      return;
    }
    fileA = data;
    return;
  });
  // file B
  const fileBPath = myArgv[3];
  let fileB = ''; 

  fs.readFile(fileBPath, 'utf8', (err, data) => {
    if (err) {
      console.log("Error: FileB");
      return;
    }
    fileB = data;
    return;
  });
  
  console.log(fileA, fileB);
  // file C
  const fileCPath = myArgv[4];
  const content = `${fileA}\n${fileB}`;

  fs.writeFile(fileCPath, content, 'utf8', (err, data) => {
    if (err) {
      console.log("Error: FileC");
      return;
    }
    console.log("Concatenation Successful...");
  });
}
