#!/usr/bin/node
const arg = process.argv[2];
const parsed = parseInt(arg);
if (!isNaN(parsed)) {
  if (parsed > 0) {
    for (let i = 0; i < parsed; i++) {
      console.log('X'.repeat(parsed));
    }
  }
} else {
  console.log('Missing size');
}
         #!/usr/bin/node
const arg = process.argv[2];
const parsed = parseInt(arg);
if (!isNaN(parsed)) {
  if (parsed > 0) {
    for (let i = 0; i < parsed; i++) {
      console.log('X'.repeat(parsed));
    }
  }
} else {
  console.log('Missing size');
}
