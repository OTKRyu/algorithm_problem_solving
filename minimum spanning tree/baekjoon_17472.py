import sys
from collections import deque

input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(s, cnt):
    q = deque()
    q.append(s)
    lands[s[0]][s[1]] = cnt
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and lands[nr][nc] == 1:
                lands[nr][nc] = cnt
                q.append([nr, nc])


def get_edges(r, c):
    for i in range(4):
        cnt = 1
        while 1:
            nr = r + dr[i] * cnt
            nc = c + dc[i] * cnt
            if 0 <= nr < n and 0 <= nc < m:
                if lands[nr][nc] == 0:
                    cnt += 1
                elif lands[nr][nc] != lands[r][c]:
                    if cnt-1 >= 2:
                        edges.append([cnt-1, lands[r][c], lands[nr][nc]])
                        break
                    else:
                        break
                else:
                    break
            else:
                break


def find(x):
    while x != check[x]:
        x = check[x]
    return x


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return 0
    else:
        check[root_y] = root_x
        return 1


def kruskal():
    cnt = 0
    idx = 0
    total = 0
    while idx < len(edges) and cnt != land_cnt - 3:
        if union(edges[idx][1], edges[idx][2]):
            idx += 1
            cnt += 1
            total += edges[idx][0]
        else:
            idx += 1
    if cnt == land_cnt - 3:
        return total
    else:
        return -1

n, m = map(int, input().split())
lands = [list(map(int, input().split())) for i in range(n)]
land_cnt = 2
edges = []
for i in range(n):
    for j in range(m):
        if lands[i][j] == 1:
            bfs([i, j], land_cnt)
            land_cnt += 1
check = list(range(land_cnt + 1))
for i in range(n):
    for j in range(m):
        if lands[i][j] != 0:
            get_edges(i, j)
edges.sort()
print(kruskal())
