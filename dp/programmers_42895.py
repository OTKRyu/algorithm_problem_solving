def solution(N, number):
    dp = [[]]
    dp += [[int(str(N)*(i+1))] for i in range(8)]
    for i in range(1,9):
        if dp[i][0] == number:
            return i
    for i in range(2,9):
        for j in range(1,i):
            for k in range(len(dp[j])):
                for l in range(len(dp[i-j])):
                    dp[i].append(dp[j][k]+dp[i-j][l])
                    dp[i].append(dp[j][k]-dp[i-j][l])
                    dp[i].append(dp[j][k]*dp[i-j][l])
                    if dp[i-j][l] != 0:
                        dp[i].append(dp[j][k]//dp[i-j][l])
        for j in range(len(dp[i])):
            if dp[i][j] == number:
                return i
        dp[i] = list(set(dp[i]))
    return -1