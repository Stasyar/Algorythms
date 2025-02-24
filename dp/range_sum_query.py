from typing import List


# Given an integer array nums, handle multiple queries of the following type:
#
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left
# and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
# Leetcode(303. Range Sum Query - Immutable)

class NumArray:

    def __init__(self, nums: List[int]):
        self.array = [0]

        for i in nums:
            self.array.append(self.array[-1] + i)

    def sumRange(self, left: int, right: int) -> int:
        return self.array[right + 1] - self.array[left]


a = NumArray([-2, 0, 3, -5, 2, -1])
print(a.sumRange(0, 2))