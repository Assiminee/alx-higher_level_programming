#!/usr/bin/node

const { error, log } = require('console');
const req = require('request');

const movieCharacters = (url) => {
  req(url, (err, resp, body) => {
    if (err) { error(err); return; }

    const movie = JSON.parse(body);

    for (const character of movie.characters) {
      req(character, (err, resp, body) => {
        if (err) { error(err); return; }
        log(JSON.parse(body).name);
      });
    }
  });
};

if (process.argv.length < 3) {
  log('Usage: ./100-starwars_characters id');
  process.exit(1);
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

movieCharacters(url);
