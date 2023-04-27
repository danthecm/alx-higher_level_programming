#!/usr/bin/env bash
url=$1
response=$(curl -s -w '%{size_download}' -o /dev/null $url)
echo "$response"
