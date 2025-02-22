# You are given an integer array coins representing coins of different denominations and an integer
# amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#Leetcode(322. Coin Change)

coinss = [1]
amountt = 0


def foo(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):

        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])
    print(dp)
    return dp[amount] if (dp[amount] != amount + 1) else -1


print(foo(coinss, amountt))
