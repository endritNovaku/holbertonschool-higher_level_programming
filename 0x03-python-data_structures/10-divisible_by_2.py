#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # check if elements in my_list array are divisible by 2
    bool_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            bool_list[i] = True
        else:
            bool_list[i] = False
    # return a new list with True or False
    return(bool_list)
