import sys
from collections import deque

input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs():
    global k
    q = deque()
    q.append([0, 0, k])
    check[0][0][k] = 1
    while q:
        c = q.popleft()
        if c[0] == n-1 and c[1] == m-1:
            return check[c[0]][c[1]][c[2]]
        else:
            d = check[c[0]][c[1]][c[2]]
            for i in range(4):
                nr = c[0] + dr[i]
                nc = c[1] + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if maze[nr][nc] == 0 and check[nr][nc][c[2]] == -1:
                        q.append([nr, nc, c[2]])
                        check[nr][nc][c[2]] = d + 1
                    else:
                        if c[2] > 0 and check[nr][nc][c[2]-1] == -1:
                            q.append([nr, nc, c[2]-1])
                            check[nr][nc][c[2] - 1] = d + 1
    return -1


n, m, k = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for i in range(n)]
check = [[[-1 for i in range(k+1)] for j in range(m)] for l in range(n)]
print(bfs())

