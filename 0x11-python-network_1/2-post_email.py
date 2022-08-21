#!/usr/bin/python3
"""status for intranet.hbtn.io/status/"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email' : sys.argv[2] }
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    the_page = the_page.decode("UTF-8")
    print(the_page)
