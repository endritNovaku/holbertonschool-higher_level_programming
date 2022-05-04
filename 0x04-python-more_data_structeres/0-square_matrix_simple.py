#!/usr/bin/python3
# compute the square value of all integers of a matrix
def square_matrix_simple(matrix=[]):
    # new list to store all results of matrix
    square = []
    # find the square of each element in matrix and store it in square list
    for row in matrix:
        square.append(list(map(lambda a: a*a, row)))
    return(square)
