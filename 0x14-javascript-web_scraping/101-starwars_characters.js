#!/usr/bin/node

const { error, log } = require('console');

if (process.argv.length < 3) {
  log('Usage: ./100-starwars_characters id');
  process.exit(1);
}

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, async (err, resp, body) => {
  if (err) { error(err); return; }

  const movie = JSON.parse(body);

  for (const character of movie.characters) {
    await new Promise((resolve, reject) => {
      req(character, (err, resp, body) => {
        if (err) { reject(err); }
        log(JSON.parse(body).name);
      });
      resolve();
    }).catch(err => { error(err); });
  }
});
