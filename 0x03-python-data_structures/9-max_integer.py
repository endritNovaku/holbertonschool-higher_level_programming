#!/usr/bin/python3
def max_integer(my_list=[]):
    # return the biggest number from the array
    biggest_num = 0
    for i in range(len(my_list)):
        if my_list[i] > biggest_num:
            biggest_num = my_list[i]
    return(biggest_num)
