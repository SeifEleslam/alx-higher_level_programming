#!/usr/bin/python3
import this

if this.__doc__ is not None:
  arr = this.__doc__.split('\n\n')
  print(arr[2])
  print(arr[1])
