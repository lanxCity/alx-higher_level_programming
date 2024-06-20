#!/usr/bin/node

exports.logMe = function (item) {
  console.log(`${exports.logMe.counter++}: ${item}`);
};

exports.logMe.counter = 0;
