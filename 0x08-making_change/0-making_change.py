#!/usr/bin/python3
"""Make change module"""


def makeChange(coins, total):
    """
        Make change function

        Args:
            coins - number of coins
            total - total coins

        Return:
            the fewest number of coins needed to meet a given amount
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
