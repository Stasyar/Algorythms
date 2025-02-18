# You may recall that an array arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if
# there is no mountain subarray.
# Leetcode(845. Longest Mountain in Array)


a = [0,1,2,3,4,5,4,3,2,1,0]


def foo(arr):
    all_mounts = []

    for i in range(1, len(arr)):
        if i + 1 < len(arr) and arr[i - 1] < arr[i] > arr[i + 1]:
            l = i - 1
            r = i + 1

            while l - 1 >= 0 and arr[l] > arr[l - 1]:
                l -= 1
            while r + 1 < len(arr) and arr[r] > arr[r + 1]:
                r += 1

            all_mounts.append(arr[l:r + 1])

    if all_mounts:
        print(all_mounts)
        res = [len(x) for x in all_mounts]
        return max(res)
    else:
        return 0


print(foo(a))