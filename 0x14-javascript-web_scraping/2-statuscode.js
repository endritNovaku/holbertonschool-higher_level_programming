#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(res => {
    console.log('code:', res.status);
  });
  .catch(function (error) {
    console.log('code:', error.response.status);
  });
