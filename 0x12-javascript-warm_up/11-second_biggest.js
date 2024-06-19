#!/usr/bin/node

const myArgv = process.argv;

// copy elements from index 2 to the end
const realArgs = myArgv.slice(2);

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
  const biggestIntPosition = 3;
  let highest;

  while (counter < biggestIntPosition) {
    counter++;
    highest = findHighestNumber(realArgs);

    if (counter === biggestIntPosition) break;

    for (const i in realArgs) {
      if (realArgs[i] === highest) {
        realArgs.splice(i, 1);
      }
    }
  }
  console.log(highest);
}
