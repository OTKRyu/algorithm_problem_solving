import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
house = [list(map(int, input().split())) for i in range(n)]
check = [[0 for i in range(m)] for j in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]
while 1:
    check[r][c] = 1
    for i in range(4):
        nd = (d+3*(i+1))%4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if 0<=nr<n and 0<=nc<m and house[nr][nc] == 0 and check[nr][nc] == 0:
            r = nr
            c = nc
            d = nd
            break
    else:
        nr = r - dr[d]
        nc = c - dc[d]
        if 0<=nr<n and 0<=nc<m and house[nr][nc] == 0:
            r = nr
            c = nc
        else:
            break
result = 0
for i in range(n):
    for j in range(m):
        if check[i][j] != 0:
            result += 1
print(result)