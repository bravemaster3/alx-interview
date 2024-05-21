#!/usr/bin/node
const request = require('request');
const movie_id = process.argv[2];
const base_url = 'https://swapi-api.alx-tools.com/api/';
const film_url = base_url + 'films/' + movie_id;

request({ url: film_url, json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  for (const character of body.characters) {
    request({ url: character, json: true }, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      console.log(body.name);
    });
  }
});
