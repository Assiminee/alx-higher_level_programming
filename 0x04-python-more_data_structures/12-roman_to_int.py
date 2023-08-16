#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        numerals = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        first_char = roman_string[0]
        if (first_char == 'I' and len(roman_string) > 1):
            num = -numerals['I']
        else:
            num = numerals[first_char]
        for i in range(1, len(roman_string)):
            num += numerals[roman_string[i]]
        return num
    return 0

