from collections import deque

def bfs(r,c):
    dr = [0,0,1,1,1,-1,-1,-1]
    dc = [1,-1,1,0,-1,1,0,-1]
    q = deque()
    q.append([r,c])
    check[r][c] = 0
    while q:
        cr, cc = q.popleft()
        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<n and 0<=nc<m and (check[nr][nc] == -1 or check[nr][nc] > check[cr][cc]+1):
                q.append([nr,nc])
                check[nr][nc] = check[cr][cc] + 1

n, m = map(int, (input().split()))
table = [list(map(int, input().split())) for i in range(n)]
check = [[-1 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if table[i][j] == 1:
            bfs(i,j)
maximum = 0
for i in range(n):
    for j in range(m):
        if check[i][j] > maximum:
            maximum = check[i][j]
print(maximum)