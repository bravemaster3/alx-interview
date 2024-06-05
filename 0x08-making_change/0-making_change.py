#!/usr/bin/python3

"""
makeChange function for computing the minimum number of coins to give change
"""


def makeChange(coins, total):
    """function definition"""

    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0
    remaining_total = total

    for coin in coins:
        if coin <= remaining_total:
            num_coins = remaining_total // coin
            coin_count += num_coins
            remaining_total -= num_coins * coin
        if remaining_total == 0:
            return coin_count

    return -1
