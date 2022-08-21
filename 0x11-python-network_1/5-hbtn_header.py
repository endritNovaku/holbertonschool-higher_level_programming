#!/usr/bin/python3
"""fetch https://intranet.hbtn.io/status"""
import requests
from sys import argv

r = requests.get(argv[1])
print(r.headers['X-Request-Id'])
