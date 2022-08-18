#!/bin/bash
# sent a get request to the url and display the body of the response
curl -sX POST -F "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
