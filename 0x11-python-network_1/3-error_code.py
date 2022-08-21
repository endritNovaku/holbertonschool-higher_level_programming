#!/usr/bin/python3
"""status for intranet.hbtn.io/status/"""
import urllib.request
from urllib.error import HTTPError
from sys import argv
if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        res = urllib.request.urlopen(req)
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
    else:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("UTF-8"))
