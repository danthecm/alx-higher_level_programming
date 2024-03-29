#!/usr/bin/python3
"""
A python module that makes a request to a url and prints the response
"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    data = response.read()

print("Body response:")
print("\t- type: {}".format(type(data)))
print("\t- content: {}".format(data))
print("\t- utf8 content: {}".format(data.decode('utf-8')))
