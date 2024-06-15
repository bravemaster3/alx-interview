#!/usr/bin/python3
"""
Prime game function
"""


def isWinner(x, nums):
    """function def"""
    def sieve(n):
        """helper function to generate all primes to n"""
        primes = [True for _ in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p] is True:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        primes[0] = primes[1] = False
        return [p for p in range(2, n+1) if primes[p]]

    def game(n):
        """actual game"""
        primes = sieve(n)
        return len(primes) % 2 == 1

    maria_wins = sum(game(n) for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
