#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        numerals = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                    }
        num = 0
        i = 0
        if roman_string[i] == 'I' and len(roman_string) > 1:
            while roman_string[i] == 'I':
                num += numerals['I']
                i += 1
            if roman_string[i] != 'I' and roman_string[i]:
                num *= -1
        for it in range(i, len(roman_string)):
            num += numerals[roman_string[it]]
        return num
    return 0
