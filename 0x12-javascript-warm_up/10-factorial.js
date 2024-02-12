#!/usr/bin/node
console.log('C is fun\nPython is cool\nJavaScript is amazing');
#!/usr/bin/node
function fact (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  }
  return a * fact(a - 1);
}
const firstArg = process.argv[2];
const parsedNum = parseInt(firstArg);
console.log(fact(parsedNum));
