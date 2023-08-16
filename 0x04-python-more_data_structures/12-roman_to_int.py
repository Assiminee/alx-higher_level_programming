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
        rev = roman_string[::-1]
        num = numerals[rev[0]]
        for i in range(1, len(rev)):
            prev = numerals[rev[i - 1]]
            if prev > numerals[rev[i]]:
                num -= numerals[rev[i]]
            else:
                num += numerals[rev[i]]
        return num
    return 0
