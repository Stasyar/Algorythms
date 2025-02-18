# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Leetcode(209. Minimum Size Subarray Sum)


target1 = 7
nums1 = [1,1,1,1,7]


def foo(target, nums):
    l, total = 0, 0
    result = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            result = min(r - l + 1, result)
            total -= nums[l]
            l += 1
    return 0 if result == float("inf") else result


print(foo(target1, nums1))