#!/usr/bin/python3
"""status for intranet.hbtn.io/status/"""
import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("UTF-8"))
