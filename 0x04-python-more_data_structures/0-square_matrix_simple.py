#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda i: i**2, i)))
    return (new_matrix)
