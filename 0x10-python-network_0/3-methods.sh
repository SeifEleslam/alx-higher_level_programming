#!/bin/bash
# Using curl to get response size of provided url
curl -sI $1 | grep -i 'Allow:' | cut -d ' ' -f2-