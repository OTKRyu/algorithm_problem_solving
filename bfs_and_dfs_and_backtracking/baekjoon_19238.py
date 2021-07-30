import sys
from collections import deque

input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def find_customer(start):
    for i in range(m):
        if start == customers[i] and walls[customers[i][0]][customers[i][1]] == 2:
            walls[start[0]][start[1]] = 0
            return i, 0
    q = deque()
    q.append(start)
    dis = [[-1 for i in range(n)] for j in range(n)]
    dis[start[0]][start[1]] = 0
    flag = n * n
    tr = n
    tc = n
    while q:
        r, c = q.popleft()
        d = dis[r][c]
        if d < flag:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and dis[nr][nc] == -1 and (walls[nr][nc] == 0 or walls[nr][nc] == 2):
                    dis[nr][nc] = d + 1
                    q.append([nr, nc])
                    if walls[nr][nc] == 2:
                        flag = d + 1
                        if tr > nr:
                            tr = nr
                            tc = nc
                        elif tr == nr:
                            if tc > nc:
                                tr = nr
                                tc = nc
        else:
            break
    for i in range(m):
        if tr == customers[i][0] and tc == customers[i][1]:
            walls[tr][tc] = 0
            return i, dis[tr][tc]
    else:
        return -1, -1


def go_destination(idx):
    q = deque()
    q.append(customers[idx])
    dis = [[-1 for i in range(n)] for j in range(n)]
    dis[customers[idx][0]][customers[idx][1]] = 0
    while q:
        r, c = q.popleft()
        d = dis[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and dis[nr][nc] == -1 and (walls[nr][nc] == 0 or walls[nr][nc] == 2):
                dis[nr][nc] = d + 1
                q.append([nr, nc])
                if nr == destinations[idx][0] and nc == destinations[idx][1]:
                    return dis[nr][nc]
    return -1


n, m, fuel = map(int, input().split())
walls = [list(map(int, input().split())) for i in range(n)]
start = list(map(int, input().split()))
start = [start[0] - 1, start[1] - 1]
customers = []
destinations = []
for i in range(m):
    tmp = list(map(int, input().split()))
    customers.append([tmp[0] - 1, tmp[1] - 1])
    walls[tmp[0] - 1][tmp[1] - 1] = 2
    destinations.append([tmp[2] - 1, tmp[3] - 1])
for i in range(m):
    idx, cost = find_customer(start)
    if cost == -1:
        print(-1)
        break
    else:
        if cost >= fuel:
            print(-1)
            break
        else:
            fuel -= cost
            cost = go_destination(idx)
            if cost == -1:
                print(-1)
                break
            else:
                if cost > fuel:
                    print(-1)
                    break
                else:
                    fuel += cost
                    start = destinations[idx]
else:
    print(fuel)
