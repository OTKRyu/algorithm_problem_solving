n = int(input())
pays = [0]
pays += list(map(int, input().split()))
dp = pays[:]
for i in range(1,n+1):
    for j in range(1,i):
        dp[i] = min(dp[i], dp[i-j]+pays[j])
print(dp[n])
