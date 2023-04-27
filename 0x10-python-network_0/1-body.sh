#!/bin/bash
# sends a curl request and displays the response if status code is 200
output=$(curl -s -w '%{http_code}' $1) && echo "$output" | grep -q '200$' && echo "$output" | sed '$d'
