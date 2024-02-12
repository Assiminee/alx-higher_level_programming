#!/usr/bin/node
const arg = process.argv[2];
const parsed = parseInt(arg);
if (!isNaN(parsed)) {
  if (parsed > 0) {
    for (let i = 0; i < parsed; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
