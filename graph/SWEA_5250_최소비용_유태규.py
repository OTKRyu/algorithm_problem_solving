def bfs():
    global n
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    maximum = n * 1000 * n
    dis = [[maximum for j in range(n)] for i in range(n)]
    dis[0][0] = 0
    q = [[0,0]]
    while q:
        p = q.pop(0)
        for i in range(4):
            np = [p[0] + dy[i], p[1] + dx[i]]
            if 0<= np[0]< n and 0<= np[1] < n:
                diff = 1 + max(0, heights[np[0]][np[1]] - heights[p[0]][p[1]])
                if dis[np[0]][np[1]] > dis[p[0]][p[1]] + diff:
                    dis[np[0]][np[1]] = dis[p[0]][p[1]] + diff
                    q.append(np)
    return dis[n-1][n-1]


for tc in range(int(input())):
    n = int(input())
    heights = [list(map(int, input().split())) for i in range(n)]
    print('#{} {}'.format(tc + 1, bfs()))
