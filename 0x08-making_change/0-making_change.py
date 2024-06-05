#!/usr/bin/python3
"""
makeChange function for computing the minimum number of coins to give change
"""

def makeChange(coins, total):
    """function definition"""
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each total
    # from 0 to the given total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
