from collections import deque
def bfs(p, cnt):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append(p)
    paper[p[0]][p[1]] = cnt
    tmpcnt = 1
    while q:
        c = q.popleft()
        for i in range(4):
            ny = c[0] + dy[i]
            nx = c[1] + dx[i]
            if 0<=nx<m and 0<=ny<n and paper[ny][nx] == 0:
                q.append([ny,nx])
                paper[ny][nx] = cnt
                tmpcnt += 1
    return tmpcnt

n, m, k = map(int, input().split())
paper = [[0 for i in range(m)] for j in range(n)]
for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1,x2):
            paper[i][j] = -1
cnt = 0
result = []
for i in range(n):
    for j in range(m):
        if paper[i][j] == 0:
            cnt += 1
            result.append(bfs([i,j], cnt))
result.sort()
print(cnt)
print(*result)
