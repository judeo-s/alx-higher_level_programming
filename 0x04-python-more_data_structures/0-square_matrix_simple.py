#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''
    A function that computes the square values of all integers of a matrix

    Args:
        matrix : list
    Returns:
        new_matrix : list
    '''
    new_matrix = []
    for i in matrix:
        squared = list(map(lambda x: x ** 2, i))
        new_matrix.append(squared)
    return new_matrix
