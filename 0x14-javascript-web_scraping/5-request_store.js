#!/usr/bin/node

/**
 * A script that gets the contents of a webpage and stores it in a file.
 */
const fs = require('fs');
const request = require('request');
const args = process.argv;

request(args[2]).pipe(fs.createWriteStream(args[3]));
