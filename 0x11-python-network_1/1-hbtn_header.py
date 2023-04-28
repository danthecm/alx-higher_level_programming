#!/usr/bin/python3
"""
A python module that makes a request to the url passed as argument
"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')
    print(header)