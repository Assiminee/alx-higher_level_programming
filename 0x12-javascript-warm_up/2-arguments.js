#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
#!/usr/bin/node
const args = process.argv;
if (args.length < 3) {
  console.log('No argument');
} else {
  if (args.length === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}
