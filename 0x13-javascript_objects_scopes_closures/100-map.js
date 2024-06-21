#!/usr/bin/node

const initArray = require('./100-data').list;

const initArrayMultiple = initArray.map((el, index) => el * index);

console.log(initArray);
console.log(initArrayMultiple);
