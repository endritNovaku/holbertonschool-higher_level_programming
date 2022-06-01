#!/usr/bin/python3
"""pascal fun"""


def pascal_triangle(n):
    """create a pascal num"""
    newArr = []
    result = []
    newN = 1
    if n <= 0:
        return newArr

    for i in range(n):
        num = newN
        newArr.append([])
        if num > 9:
            while num > 9:
                newArr[i].append(int(num % 10))
                num = num / 10
        newArr[i].append(int(num))
        newN = newN * 11
    return newArr
