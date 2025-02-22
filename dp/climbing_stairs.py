nn = 0


def foo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 1:
        return 2
    else:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
           dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(foo(nn))