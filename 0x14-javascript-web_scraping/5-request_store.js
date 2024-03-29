#!/usr/bin/node
//script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

if (process.argv.length > 3) {
  request(process.argv[2], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      fs.writeFile(process.argv[3], body, 'utf8', (err) => {
        if (err) console.log(err);
      });
    }
  });
}
