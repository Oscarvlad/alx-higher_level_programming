#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
const { argv } = require('process');
const link = argv[2];
const path = argv[3];

axios.get(link)
  .then(res => {
    fs.appendFile(path, res.data, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }).catch(error => {
    if (error.response) {
      console.log(error.response.status);
    }
  });
