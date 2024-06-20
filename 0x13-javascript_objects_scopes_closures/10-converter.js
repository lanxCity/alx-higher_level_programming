#!/usr/bin/node

exports.converter = function (base) {
  const hexExceptions = {
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f'
  };

  function convert (value) {
    if (value < base) {
      return value in hexExceptions ? hexExceptions[value] : value;
    }

    let remainder = value % base;
    remainder = remainder in hexExceptions ? hexExceptions[value] : remainder;

    const constant = Math.floor(value / base);

    return String(convert(constant)) + String(remainder);
  }
  return convert;
};
