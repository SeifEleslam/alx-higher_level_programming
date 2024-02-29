#!/bin/bash
# Using curl to get response size of provided url

url=$1
if [ -z "$url" ] ; then
  echo "Usage: $0 <URL>"
  exit 1
else
  curl -s -o /dev/null  -w "%{size_download}\n" "$url"
fi
