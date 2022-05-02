#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # create an array to add tuples
    tuple_sum = [0, 0, 0, 0]
    # check if the tuple exist and add them to tuple_sum array
    # if tuple does not exist the element of array will remain 0
    for i in range(2):
        if len(tuple_a) == 2:
            tuple_sum[i] = tuple_a[i]
        elif len(tuple_a) == 1:
            tuple_sum[0] = tuple_a[0]
    for j in range(2):
        if len(tuple_b) == 2:
            tuple_sum[j + 2] = tuple_b[j]
        elif len(tuple_b) == 1:
            tuple_sum[2] = tuple_b[0]
    # find the sum of all elements in the tupple_sum array
    result = tuple_sum[0] + tuple_sum[2], tuple_sum[1] + tuple_sum[3]
    # return the sum of all elements in the tupple_sum array
    return(result)
