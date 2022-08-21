#!/usr/bin/python3
"""status for intranet.hbtn.io/status/"""
import urllib.request
import urlib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("UTF-8")
