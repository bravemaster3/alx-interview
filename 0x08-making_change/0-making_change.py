#!/usr/bin/python3

"""
makeChange function for computing the minimum number of coins to give change
"""


def makeChange(coins, total):
    """function definition"""

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return (dp[total] if dp[total] != float('inf') else -1)