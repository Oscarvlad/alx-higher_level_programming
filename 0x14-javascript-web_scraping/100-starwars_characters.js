#!/usr/bin/node
const axios = require('axios');
const { argv } = require('process');
const link = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

axios.get(link)
  .then(res => {
    const characters = res.data.characters;
    for (let i = 0; i < characters.length; i++) {
      axios.get(characters[i])
        .then(response => {
          console.log(response.data.name);
        });
    }
  }).catch(error => {
    if (error.response) console.log(error.response);
  });
