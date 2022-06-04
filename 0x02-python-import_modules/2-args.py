#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    nArgs = len(argv)
    if nArgs == 1:
        print(f"{nArgs - 1} arguments.")
    elif nArgs == 2:
        print(f"{nArgs - 1} argument:")
    else:
        print(f"{nArgs - 1} arguments:")

    for i in range(1, nArgs):
        print(f"{i}: {argv[i]}")
