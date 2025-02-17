# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
# Leetcode(15. 3Sum)

nums = [0,0,0,0]


def foo(lst):
    lst.sort()

    final_lst = []
    for i, p in enumerate(lst):

        if i > 0 and p == lst[i - 1]:
            continue

        l = i + 1
        r = len(lst) - 1

        while l < r:
            sm = p + lst[l] + lst[r]

            if sm > 0:
                r -= 1
            elif sm < 0:
                l += 1
            else:
                final_lst.append([p, lst[r], lst[l]])
                l += 1
                while l < r and lst[l] == lst[l + 1]:
                    l += 1
                while l < r and lst[r] == lst[r - 1]:
                    r -= 1


    return final_lst


print(foo(nums))
