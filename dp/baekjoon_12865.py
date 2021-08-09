import sys

input = sys.stdin.readline

n, k = map(int, input().split())
things = [list(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(k+1)] for j in range(n)]
for i in range(n):
    for j in range(k+1):
        if i == 0:
            if j >= things[i][0]:
                dp[i][j] = things[i][1]
        else:
            if j >= things[i][0]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-things[i][0]]+things[i][1])
            else:
                dp[i][j] = dp[i-1][j]
print(dp[n-1][k])