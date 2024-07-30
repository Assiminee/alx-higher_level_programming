#!/usr/bin/node

const { log, error } = require('console');

const fetchStarWars = (id) => {
  const req = require('request');
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

  req(url, (err, resp, body) => {
    if (err) {
      error(err);
      return;
    }

    const json = JSON.parse(body);

    log(json.title);
  });
};

if (process.argv.length < 3) {
  log('Usage: ./3-starwars_title id');
  process.exit(1);
}

const id = process.argv[2];

fetchStarWars(id);
