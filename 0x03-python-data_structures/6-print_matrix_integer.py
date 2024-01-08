#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''
    A function that prints a matrix of integers

    Args:
        matrix : [[]]
    Returns:
        None
    '''
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print("{:d}".format(matrix[i][j]), end="")
                if j != len(matrix[0]) - 1:
                    print('', end=" ")
            print()
