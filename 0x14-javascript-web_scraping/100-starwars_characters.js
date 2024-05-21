#!/usr/bin/node

/**
 * A script that prints all characters of a Star Wars movie.
 */

const request = require('request');
const args = process.argv;

const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + args[2], (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    request.get(i, function (error, response, body1) {
      if (error) throw error;
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
