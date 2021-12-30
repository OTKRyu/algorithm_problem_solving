from collections import deque

def bfs(start, end,n):
    check = [[-1 for i in range(n)] for j in range(n)]
    q = deque()
    q.append(start)
    check[start[0]][start[1]] = 0
    dr = [-2,-2,0,0,2,2]
    dc = [-1,1,-2,2,-1,1]
    while q:
        r,c = q.popleft()
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n and check[nr][nc] == -1:
                check[nr][nc] = check[r][c] + 1
                q.append([nr,nc])
    return check[end[0]][end[1]]


n =  int(input())
r1, c1, r2, c2 = map(int, input().split())
print(bfs([r1,c1], [r2,c2],n))