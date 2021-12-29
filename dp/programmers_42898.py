def solution(m, n, puddles):
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = 1
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
    for i in range(1,n):
        if dp[i][0] == -1:
            continue
        else:
            if dp[i-1][0] == -1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
    for i in range(1,m):
        if dp[0][i] == -1:
            continue
        else:
            if dp[0][i-1] == -1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == -1:
                continue
            else:
                if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                    dp[i][j] = 0
                elif dp[i-1][j] == -1:
                    dp[i][j] = dp[i][j-1]
                elif dp[i][j-1] == -1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
    answer = dp[n-1][m-1]
    print(dp)
    return answer