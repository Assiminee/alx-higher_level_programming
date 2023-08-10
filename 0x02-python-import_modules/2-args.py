#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ster = "arguments"
    num_args = len(sys.argv)
    if num_args == 1:
        ster += "."
    else:
        if num_args == 2:
            ster = "argument"
        ster += ":"
    print("{:d} {:s}".format(num_args - 1, ster))
    i = 1
    while i < num_args:
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
