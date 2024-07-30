#!/usr/bin/node

const readFile = (path) => {
  const fs = require('node:fs');

  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
};

if (process.argc < 3) {
  console.log('Usage: ./0-readme /path/to/file');
  process.exit(1);
}

const [path] = process.argv.slice(2);

readFile(path);
