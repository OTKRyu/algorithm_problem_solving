import sys
from collections import deque


def bfs(cl, id):
    dr = [0,0,1,1,1,-1,-1,-1]
    dc = [1,-1,1,0,-1,1,0,-1]
    q = deque()
    q.append(cl)
    check[cl[0]][cl[1]] = id
    while q:
        r, c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < h and 0<= nc< w and islands[nr][nc] == 1 and check[nr][nc] == 0:
                check[nr][nc] = id
                q.append([nr,nc])

while 1:
    w, h = map(int, input().split())
    if (w,h) == (0,0):
        break
    else:
        islands = [list(map(int, input().split())) for i in range(h)]
        id = 0
        check = [[0 for i in range(w)] for j in range(h)]
        for i in range(h):
            for j in range(w):
                if islands[i][j] == 1 and check[i][j] == 0:
                    id += 1
                    bfs([i,j],id)
        print(id)