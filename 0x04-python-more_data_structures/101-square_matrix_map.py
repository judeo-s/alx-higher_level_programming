#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    '''
    A function that computes the square value of all integers
    of a matrix using map

    Args:
        matrix : list
    Returns:
        list
    '''
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
