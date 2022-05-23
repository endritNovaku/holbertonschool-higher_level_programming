#!/usr/bin/python3
def matrix_divided(matrix, div):
    divMatrix=[]
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        divMatrix.append([])
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            divMatrix[i].append(round(matrix[i][j] / div, 2))
    return divMatrix
            
