#!/usr/bin/python3
'fetch https://intranet.hbtn.io/status using requests library'
import requests

r = requests.get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(type(r.text)))
print('\t- content: {}'.format(r.text))
