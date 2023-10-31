#!/usr/bin/python3
import this
arr = this.__doc__
if arr:
  arr = arr.split('\n\n')
  print(arr[2])
  print(arr[1])
