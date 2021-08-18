import sys

input = sys.stdin.readline

def power(mat, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat
    else:
        if b%2:
            tmp = power(mat, b//2)
            return dot(dot(tmp, tmp),mat)
        else:
            tmp = power(mat, b//2)
            return dot(tmp, tmp)

def dot(m1, m2):
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (m1[i][k] * m2[k][j])
    for i in range(n):
        for j in range(n):
            result[i][j] %= 1000
    return result


n, b = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(n)]
result = power(mat, b)
for i in range(n):
    print(*result[i])
