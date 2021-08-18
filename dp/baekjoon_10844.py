import sys

input = sys.stdin.readline

n = int(input())
stair = [[0]*10 for i in range(n)]
stair[0] = [0,1,1,1,1,1,1,1,1,1]
for i in range(1,n):
    for j in range(10):
        if j == 0:
            stair[i][j] = stair[i-1][j+1]
        elif j == 9:
            stair[i][j] = stair[i-1][j-1]
        else:
            stair[i][j] = (stair[i-1][j-1] + stair[i-1][j+1])
print(sum(stair[n-1])%1000000000)