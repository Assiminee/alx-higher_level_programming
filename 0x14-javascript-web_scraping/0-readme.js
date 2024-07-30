#!/usr/bin/node

const readFile = () => {
  if (process.argc < 3) {
    console.log('Usage: ./0-readme /path/to/file');
    return;
  }

  const [path] = process.argv.slice(2);
  const fs = require('node:fs');

  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
};

readFile();
