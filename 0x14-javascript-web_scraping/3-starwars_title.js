#!/usr/bin/node
const axios = require('axios');
const { argv } = require('process');
const link = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

axios.get(link)
  .then(response => {
    console.log(response.data.title);
  });
