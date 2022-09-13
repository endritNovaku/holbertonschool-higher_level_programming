#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2])
  .then(response => {
    const movies = response.data.results;
    const actorAdress = 'https://swapi-api.hbtn.io/api/people/18/';
    let actorShowen = 0;
    for (let i = 0; i < movies.length; i++) {
      for (let j = 0; j < movies[i].characters.length; j++) {
        if (movies[i].characters[j] === actorAdress) {
          actorShowen++;
        }
      }
    }
    console.log(actorShowen);
  })
