#!/bin/bash
# sends a curl request and displays the response if status code is 200
curl -sfL "$1" -X DELETE
