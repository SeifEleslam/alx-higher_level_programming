#!/bin/bash
# Using curl to get response size of provided url
curl -sX POST $1 -H "Content-Type: application/json" -d @$2
