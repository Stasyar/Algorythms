# Given an integer array nums and an integer k, return true if there are two distinct indices i and j
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Leetcode(219. Contains Duplicate II)


n = [1,2,3,4,1]
kk = 3


def foo(nums, k):
    seen = []

    for i, v in enumerate(nums):
        if v in seen:
            return True

        seen.append(v)

        if len(seen) > k:
            seen.remove(nums[i - k])

    return False


def better_foo(nums, k):
    h = {}

    for i, val in enumerate(nums):
        if val in h and abs(i - h[val]) <= k:
            return True
        else:
            h[val] = i

    return False


print(foo(n, kk))