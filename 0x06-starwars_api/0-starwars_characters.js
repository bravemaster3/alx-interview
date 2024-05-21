#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/';
const filmUrl = baseUrl + 'films/' + movieId;

function getCharacterName(charUrl) {
  return new Promise((resolve, reject) => {
    request({ url: charUrl, json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body.name);
      }
    });
  });
}

request({ url: filmUrl, json: true }, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  for (const character of body.characters) {
    try {
      const name = await getCharacterName(character);
      console.log(name);
    } catch (error) {
      console.error('Error:', error);
    }
  }
});
