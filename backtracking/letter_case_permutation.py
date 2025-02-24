# Given a string s, you can transform every letter individually to be lowercase or
# uppercase to create another string.
#
# Return a list of all possible strings we could create. Return the output in any order.
# Leetcode(784. Letter Case Permutation)


from typing import List

ss = "a1b2"


def foo(s: List[str]):
    o = ['']

    for c in s:
        tmp = []
        if c.isalpha():
            for i in o:
                tmp.append(i + c.lower())
                tmp.append(i + c.upper())
        else:
            for i in o:
                tmp.append(i + c)


        o = tmp

    return o

print(foo(ss))