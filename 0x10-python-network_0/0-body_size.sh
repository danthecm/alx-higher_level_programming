#!/usr/bin/env bash
# a shell script that makes a request to a url and returns the size
echo "$(curl -s -w '%{size_download}' -o /dev/null $1)"
