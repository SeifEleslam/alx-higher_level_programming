#!/bin/bash
# Using curl to get response size of provided url
curl -s -o /dev/null  -w "%{size_download}\n" "$1"

