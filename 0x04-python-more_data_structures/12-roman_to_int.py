#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a roman numeral to an integer"""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    a_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    num = 0
    for i in reversed(roman_string):
        roman = a_dict[i]
        num += roman if num < roman * 5 else -roman
    return (num)
