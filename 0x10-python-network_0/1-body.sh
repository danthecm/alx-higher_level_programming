#!/bin/bash
# sends a curl request and displays the response if status code is 200
curl -s -w '\n%{http_code}\n' $1 | sed -n '$p' | grep -q '^200$' && curl -s $1
