#!/usr/bin/node

const { error, log } = require('console');
const fs = require('node:fs');
const req = require('request');

const writeIntoFile = (url, path) => {
  req(url, (err, resp, body) => {
    if (err) { error(err); return; }
    fs.writeFile(path, body, 'utf8', err => {
      if (err) { error(err); }
    });
  });
};

if (process.argv.length < 4) {
  log('Usage: ./5-request_store.js url /path/to/file');
  process.exit(1);
}

const [url, path] = process.argv.slice(2);

writeIntoFile(url, path);
