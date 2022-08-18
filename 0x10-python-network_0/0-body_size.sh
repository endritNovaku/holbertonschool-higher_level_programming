#!/bin/bash
# use curl command and display the size
curl -s "$1" | wc -c
