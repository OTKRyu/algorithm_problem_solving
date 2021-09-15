n = int(input())
dp = [[0,0,0,0,0,0,0,0,0,0] for i in range(n)]
dp[0] = [1,1,1,1,1,1,1,1,1,1]
for i in range(1,n):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
print(sum(dp[n-1])%10007)