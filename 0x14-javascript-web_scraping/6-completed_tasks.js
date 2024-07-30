#!/usr/bin/node

const { error, log } = require('console');
const req = require('request');

const displayCompleted = (url) => {
  req(url, (err, resp, body) => {
    if (err) { error(err); return; }
    const obj = {};
    const json = JSON.parse(body);

    for (const entry of json) {
      const userId = entry.userId;

      if (!entry.completed) {
        continue;
      }

      obj[userId] = userId in obj ? obj[userId] + 1 : 1;
    }
    log(obj);
  });
};

if (process.argv.length < 3) {
  log('Usage: ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos');
  process.exit(1);
}

const url = process.argv[2];

displayCompleted(url);
