#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = ["+", "-", "*", "/"]
    op = argv[2]
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    function_list = [add, sub, mul, div]
    for i in range(len(ops)):
        if op == ops[i]:
            res = function_list[i](a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, res))
