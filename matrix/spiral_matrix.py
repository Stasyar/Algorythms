# Leetcode 54: Given an m x n matrix, return all elements of the matrix in spiral order.

data = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]


def foo(mat):
    m = len(mat)

    res = []

    while mat:
        m -= 1
        res.extend(mat.pop(0))
        for i in range(m):
            if mat[i]:
                res.append(mat[i].pop(-1))

        if mat:
            r = mat.pop(-1)
            res.extend(r[::-1])
        m -= 1
        for i in range(m):
            if mat[i]:
                res.append(mat[i].pop(0))

    return res


print(foo(data))
