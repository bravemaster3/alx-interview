#!/usr/bin/python3
"""Rotates a matrix 90° clockwise"""


def rotate_2d_matrix(matrix):
    """function definition"""
    matrix[:] = [list(i) for i in zip(*matrix)]
    for row in matrix:
        row.reverse()
