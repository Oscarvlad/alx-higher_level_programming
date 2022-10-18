#!/usr/bin/node
const args = process.argv;
const axios = require('axios');

async function printStatusCode (url) {
  await axios(url)
    .then(res => {
      console.log('code: ' + res.status);
    }).catch(function (error) {
      if (error.response) {
        console.log('code: ' + error.response.status);
      }
    });
}

printStatusCode(args[2]);
