#!/usr/bin/python3
def text_indentation(text):
    check_space = True
    for char in text:
        if check_space == True and char == " ":
            continue
        check_space = False
        print(char, end="")
        if char in ["?", ".", ":"]:
            check_space = True
            print("\n")
