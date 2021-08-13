import sys

input = sys.stdin.readline


def power(mat, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000000007
        return mat
    else:
        if b % 2:
            tmp = power(mat, b // 2)
            return dot(dot(tmp, tmp), mat)
        else:
            tmp = power(mat, b // 2)
            return dot(tmp, tmp)


def dot(m1, m2):
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (m1[i][k] * m2[k][j])
    for i in range(n):
        for j in range(n):
            result[i][j] %= 1000000007
    return result


n = 2
b = int(input())
if b == 0:
    print(0)
elif b == 1:
    print(1)
elif b == 2:
    print(1)
else:
    b -= 1
    mat = [[0, 1], [1, 1]]
    result = power(mat, b)
    print(result[1][1])
