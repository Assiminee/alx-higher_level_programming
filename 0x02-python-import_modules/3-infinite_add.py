#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0")
    else:
        x = 0
        for i in range(1, len(argv)):
            x += int(argv[i])
        print("{:d}".format(x))
