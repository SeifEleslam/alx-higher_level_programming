#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
    sum, prv_val, curr_set = 0, 0, 0
    for letter in roman_string:
        value = roman_dictionary[letter]
        if value > prv_val:
            curr_set = value - curr_set
        elif prv_val > value:
            sum += curr_set
            curr_set = value
        else:
            curr_set += value
        prv_val = value
    sum += curr_set
    return sum
