#!/usr/bin/node

/**
 * A script that writes a string to a file.
 */
const fs = require('fs');
const args = process.argv;

fs.writeFile(args[2], args[3], (err) => {
  if (err) throw err;
});
