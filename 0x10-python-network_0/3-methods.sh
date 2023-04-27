#!/bin/bash
# a shell script that displays the allowed methods of a request
curl -Is "$1" | grep Allow | cut -c 8-
