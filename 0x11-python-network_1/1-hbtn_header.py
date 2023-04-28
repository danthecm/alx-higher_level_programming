#!/usr/bin/python3
"""
A python module that makes a request to the url passed as argument
"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    header = response.getheader('X-Request-Id')
    print(header)
