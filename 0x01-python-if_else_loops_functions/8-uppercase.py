#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        print("{:c}".format(ord(letter) if letter >= 'A' and letter <= 'Z'
                            else (ord(letter) + ord('A') - ord('a'))), end='')
    print('')
