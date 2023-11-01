#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        print("{:c}".format((ord(letter) + ord('A') - ord('a')))
              if (letter >= 'a' and letter <= 'z') else letter, end='')
    print('')
