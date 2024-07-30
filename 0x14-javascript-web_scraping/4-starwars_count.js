#!/usr/bin/node

const { error, log } = require('console');

const movieCountCharacter = (url) => {
  const req = require('request');

  req(url, (err, resp, body) => {
    if (err) {
      error(err);
      return;
    }

    const movieArr = JSON.parse(body).results;
    const character = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;

    for (movie of movieArr) {
      const characters = movie.characters;
      
      if (characters.includes(character)) {
        count++;
	  }
    }

    log(count);
  });
}

if (process.argv.length < 3) {
  log('Usage: ./4-starwars_count url');
  process.exit(1);
}

const url = process.argv[2];

if (url !== 'https://swapi-api.alx-tools.com/api/films') {
  log('Incorrect url');
  process.exit(1);
}

movieCountCharacter(url);
