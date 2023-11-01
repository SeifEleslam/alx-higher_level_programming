#!/usr/bin/python3
for letter in reversed(range(ord('a'), ord('z')+1)):
    print("{:c}".format(letter if letter %
          2 == 0 else letter + ord('A') - ord('a')), end='')
