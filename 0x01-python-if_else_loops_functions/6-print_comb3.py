#!/usr/bin/python3
for num in range(0, 100):
    if (num % 10 > int(num/10)):
        print("{:02d}".format(num, num),
              end='\n' if num % 10 + int(num/10) == 17 else ', ')
