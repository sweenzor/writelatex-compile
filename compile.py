#!/usr/bin/env python

import requests
import json

fid = open('example.tex', 'rb')
text = fid.read()

payload = {'snip': text, 'spash': 'none'}
r = requests.post('https://www.writelatex.com/docs', data=payload)

print json.dumps(payload)
print r.url


