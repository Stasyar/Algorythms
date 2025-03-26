# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Leetcode (78. Subsets)

from typing import List

n = [1,2,3]


def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result


print(subsets(n))