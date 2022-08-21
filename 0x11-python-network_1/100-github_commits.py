#!/usr/bin/python3
"""list 10 recent commits from a github repo"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    res = requests.get(url)
    lastCom = res.json()
    for i in range(0, 10):
        print("{} {}".format(lastCom[i]['sha'],
                             lastCom[i]['commit']['author']['name']))
