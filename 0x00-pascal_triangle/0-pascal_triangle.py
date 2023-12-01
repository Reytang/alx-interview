#!/usr/bin/python3
'''A module for working with a Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates the list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for p in range(n):
        line = []
        for j in range(p + 1):
            if j == 0 or j == p:
                line.append(1)
            elif p > 0 and j > 0:
                line.append(triangle[p - 1][j - 1] + triangle[p - 1][j])
        triangle.append(line)
    return triangle
