import sys
input = sys.stdin.readline

dp = [[0,0,0,0] for j in range(1000001)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]
for j in range(4,1000001):
    dp[j][1] = dp[j-1][2]%1000000009 + dp[j-1][3]%1000000009
    dp[j][2] = dp[j-2][1]%1000000009 + dp[j-2][3]%1000000009
    dp[j][3] = dp[j-3][1]%1000000009 + dp[j-3][2]%1000000009
for i in range(int(input())):
    n = int(input())
    print(sum(dp[n])%1000000009)