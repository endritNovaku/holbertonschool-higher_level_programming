#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # delete an element at a given index and return the new list
    # if idx is out of range return the original list
    if idx < 0 or idx >= len(my_list):
        return(my_list)
    del my_list[idx]
    return(my_list)
