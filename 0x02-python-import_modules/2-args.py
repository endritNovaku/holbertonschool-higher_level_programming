#!/usr/bin/python3
import sys
def main():
    length = len(sys.argv)
    if length == 1:
        print("0 argument.")
    else:
        print("{} argument:".format(length - 1))
        for i in range(1, length):
            print(i, sys.argv[i])
