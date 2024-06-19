#!/usr/bin/node

const myArgv = process.argv;

// copy elements from index 2 to the end
const realArgs = myArgv.slice(2);
let realArgsCopy = realArgs.slice(0);

if (realArgs <= 1) {
  console.log(0);
} else {
  function findHighestNumber (arr) {
    let i = 0;
    let highest = arr[i];

    while (arr[i]) {
      if (arr[i] > highest) {
        highest = arr[i];
      }
      i++;
    }
    return highest;
  }

  // To keep track biggest integer needed, either first, second, etc.
  let counter = 0;
  const biggestIntPosition = 2;
  let highest;

  while (counter < biggestIntPosition) {
    counter++;
    highest = findHighestNumber(realArgsCopy);

    if (counter === biggestIntPosition) break;

    realArgsCopy = realArgsCopy.filter(el => el !== highest);
  }
  console.log(highest);
}
