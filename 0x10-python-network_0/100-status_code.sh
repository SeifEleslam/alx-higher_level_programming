#!/bin/bash
# Using curl to get response size of provided url
curl -so /dev/null -w "%{http_code}\n" $1
