#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2])
  .then(res => {
    console.log('code: %s', res.status);
  })
  .catch(error => {
    console.log('code: %s', error.response.status);
  });
