#!/usr/bin/node
/**
 * A script that display the status code of a GET request.
 */

const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (error) throw error;
  console.log('code: ' + response.statusCode);
});
