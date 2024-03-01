#!/bin/bash
# Using curl to get response size of provided url
curl -so /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
