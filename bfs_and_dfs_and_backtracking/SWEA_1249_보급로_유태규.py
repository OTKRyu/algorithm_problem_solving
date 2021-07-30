def bfs():
    global n
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    dis = [[n*n*10 for j in range(n)] for i in range(n)]
    dis[0][0] = 0
    q = [[0, 0]]
    while q:
        p = q.pop(0)
        for i in range(4):
            np = [p[0] + dy[i], p[1] + dx[i]]
            if 0 <= np[0] < n and 0 <= np[1] < n:
                if dis[np[0]][np[1]] > dis[p[0]][p[1]] + depth[np[0]][np[1]]:
                    dis[np[0]][np[1]] = dis[p[0]][p[1]] + depth[np[0]][np[1]]
                    q.append(np)
    return dis[n - 1][n - 1]


for tc in range(int(input())):
    n = int(input())
    depth = [list(map(int, list(input()))) for i in range(n)]
    print('#{} {}'.format(tc + 1, bfs()))
