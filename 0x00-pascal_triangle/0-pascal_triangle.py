#!/usr/bin/python3
"""
function that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """pascal triangle definition"""
    # from math import factorial
    from math import comb
    if n <= 0:
        return []
    triangle = [[0] * (i + 1) for i in range(n)]
    for i in range(n):
        triangle[i][0] = 1
        triangle[i][i] = 1
        for j in range(1, i):
          triangle[i][j] = comb(i, j)
            # triangle[i][j] = int(factorial(i)/(factorial(j) * factorial(i-j)))

    return triangle
