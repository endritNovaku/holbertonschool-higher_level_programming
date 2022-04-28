#!/usr/bin/python3
import sys
def main():
    length = len(sys.argv)
    if length == 1:
        print("0 argument.")
    elif length == 2:
        print("1 argument:", sys.argv[1])
    else:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
