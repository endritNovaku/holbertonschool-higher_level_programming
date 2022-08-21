#!/usr/bin/python3
'fetch https://intranet.hbtn.io/status using requests library'
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
