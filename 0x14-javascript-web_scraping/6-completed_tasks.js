#!/usr/bin/node
const axios = require('axios');
const { argv } = require('process');
const link = argv[2];

axios.get(link)
  .then(res => {
    const newDict = {};
    const data = res.data;

    for (let i = 0; i < data.length; i++) {
      if (!(data[i].userId in newDict) && data[i].completed) {
        newDict[data[i].userId] = 1;
      } else if (data[i].userId in newDict && data[i].completed) {
        newDict[data[i].userId] = newDict[data[i].userId] + 1;
      }
    }

    console.log(newDict);
  }).catch(error => {
    if (error.response) {
      console.log(error.response);
    }
  });
