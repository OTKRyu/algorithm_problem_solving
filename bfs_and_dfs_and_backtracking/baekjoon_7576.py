def bfs(queue):
    global n, m, front, rear
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    cnt = 0
    while rear-front != 0:
        front += 1
        l = queue[front]
        d = lands[l[0]][l[1]]
        for i in range(4):
            nl = [l[0] + dy[i], l[1] + dx[i]]
            if 0 <= nl[0] < n and 0 <= nl[1] < m and lands[nl[0]][nl[1]] == 0:
                lands[nl[0]][nl[1]] = d+1
                rear += 1
                queue[rear] = nl
                if d + 1 > cnt:
                    cnt = d + 1
    return cnt

m, n = map(int, input().split())
lands = []
for i in range(n):
    lands.append(list(map(int, input().split())))
queue = [[0,0] for i in range(1000000)]
front = -1
rear = -1
cnt = 0
for i in range(n):
    for j in range(m):
        if lands[i][j] != 0:
            cnt += 1
            if lands[i][j] == 1:
                rear += 1
                queue[rear] = [i,j]
if cnt == m * n:
    print(0)
else:
    flag = 1
    result = bfs(queue)
    for i in range(n):
        for j in range(m):
            if lands[i][j] == 0:
                print(-1)
                flag = 0
                break
        if lands[i][j] == 0:
            break
    if flag:
        print(result-1)