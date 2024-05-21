#!/usr/bin/node
/**
 * A script that prints the number of movies where the character “Wedge
 * Antilles” is present.
 */

const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (error) throw error;

  const films = JSON.parse(body).results;
  let count = 0;

  for (const filmIndex in films) {
    const filmChars = films[filmIndex].characters;
    for (const charIndex in filmChars) {
      if (filmChars[charIndex].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
