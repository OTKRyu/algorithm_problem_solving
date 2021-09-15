n = int(input())
dp =[[0,0] for i in range(n)]
dp[0] = [0,1]
for i in range(1,n):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-1][0]
print(sum(dp[n-1]))