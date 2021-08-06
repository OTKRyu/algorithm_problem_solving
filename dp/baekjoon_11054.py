import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp1 = [1 for i in range(n)]
dp2 = [1 for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)
for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if nums[j] < nums[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
result = [0 for i in range(n)]
for i in range(n):
    result[i] = dp1[i] + dp2[i] -1
print(max(result))
