#!/usr/bin/node
const args = process.argv.splice(2);
if (args.length <= 1) {
  console.log('0');
} else {
  let max = parseInt(args[0]) < parseInt(args[1]) ? parseInt(args[1]) : parseInt(args[0]);
  let secondMax = parseInt(args[0]) > parseInt(args[1]) ? parseInt(args[1]) : parseInt(args[0]);
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i]) > max) {
      secondMax = max;
      max = parseInt(args[i]);
    } else if (parseInt(args[i]) > secondMax && parseInt(args[i]) < max) {
      secondMax = parseInt(args[i]);
    }
  }
  console.log(secondMax);
}
