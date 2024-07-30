#!/usr/bin/node

const { log } = require('node:console');

const writeIntoFile = (path, data) => {
  const fs = require('node:fs');
  const { error } = require('node:console');

  fs.writeFile(path, data, 'utf8', err => {
    if (err)
      error(err);
  });
};

if (process.argv.length < 4) {
  log('Usage: ./1-writeme.js /path/to/file "content"');
  process.exit(1);
}

const [path, data] = process.argv.slice(2);

writeIntoFile(path, data);
