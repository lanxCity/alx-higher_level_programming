#!/usr/bin/node

const initDict = require('./101-data').dict;

const initDictValuesList = Object.values(initDict);

const initDictValuesObj = initDictValuesList.reduce((newDic, el) => {
  newDic[el] = [];
  return newDic;
}, {});

// reduce(func, init)

for (const key in initDict) {
  initDictValuesObj[initDict[key]].push(key);
}

console.log(initDictValuesObj);
