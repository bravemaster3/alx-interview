#!/usr/bin/python3
"""
Prime game function
"""


def is_prime(n):
    """
    This function checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def remove_multiples(nums, prime):
    """
    This function removes the prime number and its multiples from the list.
    """
    new_nums = []
    for num in nums:
        if num % prime != 0 or num == prime:
            new_nums.append(num)
    return new_nums


def isWinner(x, nums):
    """
    This function determines the winner of the game for a single round.
    """
    maria_wins = 0
    ben_wins = 0
    player = "Maria"  # Start with Maria
    for _ in range(x):
        if not nums:
            break
        if player == "Maria":
            # Maria can't choose anymore, Ben wins the round
            ben_wins += 1
            player = "Ben"
        else:
            # Ben removes the first element (not a prime)
            nums.pop(0)
            player = "Maria"
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
