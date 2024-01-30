#!/usr/bin/python3

"""A module that uses Numpy to multiply 2 matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
    Args:
        m_a: matrix
        m_b: matrix
    Returns:
        matrix
    """
    return np.matmul(m_a, m_b)
