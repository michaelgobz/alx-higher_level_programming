#!/usr/bin/node
// script to return the  status code of  response
const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    if (err) console.log(err);
    console.log('code:', res.statusCode);
  });
}

