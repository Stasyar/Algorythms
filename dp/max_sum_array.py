# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.
#Leetcode(53. Maximum Subarray)

numss = [-2,1,-3,4,-1,2,1,-5,4]

def foo(nums):
    dp = [0] * (len(nums))

    for i, v in enumerate(nums):
        dp[i] = max(v, dp[i - 1] + v)
    return max(dp)

print(foo(numss))