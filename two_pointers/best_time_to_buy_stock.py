# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
# in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Leetcode (121. Best Time to Buy and Sell Stock)


prices = [7,1,5,3,6,4]


def foo(lst):
    max_p = 0

    l, r = 0, 1

    while r != len(lst):
        if lst[l] < lst[r]:
            max_p = max(max_p, lst[r] - lst[l])
        else:
            l = r

        r += 1

    return max_p

print(foo(prices))