#!/usr/bin/node
const axios = require('axios');
const { argv } = require('process');
const link = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

axios.get(link)
  .then(async res => {
    const characters = res.data.characters;

    for (let i = 0; i < characters.length; i++) {
      const resp = await axios.get(characters[i]);
      console.log(resp.data.name);
    }
  }).catch(error => {
    if (error.response) console.log(error.response);
  });
