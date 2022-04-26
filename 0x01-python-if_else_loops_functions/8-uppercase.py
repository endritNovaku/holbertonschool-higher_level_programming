#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            string = string + chr(ord(i) - 32)
        else:
            string = string + i

    print(string)
    return str
