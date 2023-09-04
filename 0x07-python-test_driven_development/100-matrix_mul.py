#!/usr/bin/python3
"""Module to mutiply two matrices
"""


def matrix_mul(m_a, m_b):
    """returns a matrix that's the product
    of m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(ele, list) for ele in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")

    if not len(m_a) or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if not len(m_b) or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    len_ma = len(m_a[0])
    if any(len(row) != len_ma for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    len_mb = len(m_b[0])
    if any(len(row) != len_mb for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len_ma != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(ma_num * mb_num for ma_num, mb_num in zip(ma_row, mb_col)) \
            for mb_col in zip(*m_b)] for ma_row in m_a]
