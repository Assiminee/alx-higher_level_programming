#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args = process.argv.splice(2);
const sum = add(parseInt(args[0]), parseInt(args[1]));
if (!isNaN(sum)) {
  console.log(sum);
} else {
  console.log('NaN');
}
