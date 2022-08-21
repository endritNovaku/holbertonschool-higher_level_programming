#!/usr/bin/python3
'fetch https://intranet.hbtn.io/status using requests library'
import requests

r = requests.get('https://intranet.hbtn.io/status')
print(r.headers['X-Request-Id'])
