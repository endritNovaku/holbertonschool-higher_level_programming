#!/usr/bin/python3
def roman_to_int(roman_string):
    count = 0
    new_list = []
    rom = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    for i in range(len(roman_string)):
        for k, v in rom.items():
            if roman_string[i] == k:
                new_list.append(v)

    for c in range(len(new_list)):
        if c != len(new_list) -1:
            if new_list[c] >= new_list[c + 1]:
                count += new_list[c]
            else:
                count -= new_list[c]
        else:
            count += new_list[c]
    return count
