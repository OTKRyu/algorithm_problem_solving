def bfs(queue):
    global n, m, front, rear
    dy = [1, -1, 0, 0, 0, 0]
    dx = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    cnt = 0
    while rear - front != 0:
        front += 1
        l = queue[front]
        d = lands[l[0]][l[1]][l[2]]
        for i in range(6):
            nl = [l[0] + dz[i], l[1] + dy[i], l[2]+dx[i]]
            if 0 <= nl[0] < h and 0 <= nl[1] < n and 0 <= nl[2] < m and lands[nl[0]][nl[1]][nl[2]] == 0:
                lands[nl[0]][nl[1]][nl[2]] = d + 1
                rear += 1
                queue[rear] = nl
                if d + 1 > cnt:
                    cnt = d + 1
    return cnt


m, n, h = map(int, input().split())
lands = []
for k in range(h):
    floor = []
    for i in range(n):
        floor.append(list(map(int, input().split())))
    lands.append(floor)
queue = [[0, 0, 0] for i in range(1000000)]
front = -1
rear = -1
cnt = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if lands[k][i][j] != 0:
                cnt += 1
                if lands[k][i][j] == 1:
                    rear += 1
                    queue[rear] = [k, i, j]
if cnt == m * n * h:
    print(0)
else:
    flag = 1
    result = bfs(queue)
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if lands[k][i][j] == 0:
                    print(-1)
                    flag = 0
                    break
            if not flag:
                break
        if not flag:
            break
    if flag:
        print(result - 1)
