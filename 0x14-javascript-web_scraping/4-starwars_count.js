#!/usr/bin/node
const axios = require('axios');
const { argv } = require('process');
const link = argv[2];
const character = '/18/';

axios.get(link)
  .then(res => {
    let movieCount = 0;

    for (let i = 0; i < res.data.results.length; i++) {
      for (let j = 0; j < res.data.results[i].characters.length; j++) {
        if (res.data.results[i].characters[j].endsWith(character)) {
          movieCount++;
        }
      }
    }
    console.log(movieCount);
  }).catch(error => {
    if (error.response) {
      console.log(error.response.headers);
    }
  });
