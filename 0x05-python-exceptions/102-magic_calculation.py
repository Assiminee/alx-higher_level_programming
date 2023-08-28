#!/usr/bin/python3
from dis import dis
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        if i > a:
            raise Exception("Too far")
            break
        else:
            result += (a ** b) / i
        result = a + b
    return result
dis(magic_calculation)
