#!/usr/bin/node

/**
 * A script that prints the title of a Star Wars movie where the episode number
 * matches a given integer.
 */

const request = require('request');
const args = process.argv;

let data = {};
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + args[2], (error, response, body) => {
  if (error) throw error;
  data = JSON.parse(body);
  console.log(data.title);
});
