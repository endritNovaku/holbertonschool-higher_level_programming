#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2])
  .then(res => {
    const idObj = {};
    for (let i = 0; i < res.data.length; i++) {
      if (res.data[i].userId in idObj) {
        if (res.data[i].completed === true) {
          idObj[res.data[i].userId]++;
        }
      } else {
        if (res.data[i].completed === true) {
          idObj[res.data[i].userId] = 1;
        } else {
          idObj[res.data[i].userId] = 0;
        }
      }
    }
    console.log(idObj);
  })
  .catch(error => {
    console.log(error);
  });
