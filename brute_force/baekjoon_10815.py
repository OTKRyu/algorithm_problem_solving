import sys

input = sys.stdin.readline

n = int(input())
ns = list(map(int, input().split()))
max = -10000001
min = 10000001
for i in range(n):
    if ns[i] > max:
        max = ns[i]
    if ns[i] < min:
        min = ns[i]
check = [0 for i in range(max - min + 1)]
for i in range(n):
    check[ns[i] - min] = 1
m = int(input())
ms = list(map(int, input().split()))
result = [0 for i in range(m)]
for i in range(m):
    if 0 <= ms[i] - min < len(check):
        result[i] = check[ms[i] - min]
    else:
        result[i] = 0
print(*result)
