#!/usr/bin/node

const { error, log } = require('console');

const movieCountCharacter = (url) => {
  const req = require('request');

  req(url, (err, resp, body) => {
    if (err) { error(err); return; }

    const movieArr = JSON.parse(body).results;
    let count = 0;

    for (const movie of movieArr) {
      for (const character of movie.characters) {
        count = character.includes(18) ? count + 1 : count;
      }
    }

    log(count);
  });
};

if (process.argv.length < 3) {
  log('Usage: ./4-starwars_count url');
  process.exit(1);
}

const url = process.argv[2];

movieCountCharacter(url);
