#!/bin/bash
# a shell script that displays the allowed methods of a request
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
