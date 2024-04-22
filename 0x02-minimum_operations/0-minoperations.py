#!/usr/bin/python3
"""
Minimum number of operations for achieving an exact number of H
"""


def minOperations(n: int) -> int:
    """Function definition"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
