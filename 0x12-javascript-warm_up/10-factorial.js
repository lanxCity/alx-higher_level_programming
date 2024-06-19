#!/usr/bin/node

const myArgv = process.argv;
const n = myArgv[2];

function factorial (n) {
  if (n === 0 || isNaN(n)) return 1;

  return n * factorial(n - 1);
}

console.log(factorial(n));
