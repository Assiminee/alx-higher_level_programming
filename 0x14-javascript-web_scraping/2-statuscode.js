#!/usr/bin/node

const { log } = require('console');

const displayStatusCode = (url) => {
  const req = require('request');

  req.get(url).on('response', (resp) => {
	  log(`code: ${resp.statusCode}`);
  });
};

if (process.argv.length < 3) {
  log('Usage: ./2-statuscode.js url');
  process.exit(1);
}

const [url] = process.argv.slice(2);

displayStatusCode(url);
