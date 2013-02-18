#!/usr/bin/env python

import sys, time
import json
import requests


# Read arugments
try:
    filename = sys.argv[1]
except IndexError:
    print 'looking for: \'python compile.py example.tex\''
    quit()

# Load contents of .tex file
fid = open(filename, 'rb')
text = fid.read()
fid.close()

# Post contents to writeLaTeX
payload = {'snip': text, 'spash': 'none'}
r = requests.post('https://www.writelatex.com/docs', data=payload)

# Recieve response
print 'Uploaded: %s' % r.url
doc_id = r.url.split('/')[3]

# Get address of PDF
time.sleep(4)
r = requests.post('https://www.writelatex.com/docs/%s/pdf' % doc_id)
pdf_url = 'http://%s' % r.text.split('\'')[1]
r = requests.get(pdf_url)
print 'PDF size: %s bytes' % len(r.content)

# Write PDF to file
pdf_filename = '%s.pdf' % filename.split('.tex')[0]
fid = open(pdf_filename, 'wb')
fid.write(r.content)
fid.close()
print 'PDF saved: \'%s\'' % pdf_filename
