from collections import deque

def solution(maps):
    p = [0,0]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append(p)
    check = [[-1 for i in range(len(maps[0]))] for i in range(len(maps))]
    check[p[0]][p[1]] = 0
    while q:
        c = q.popleft()
        dis = check[c[0]][c[1]]
        for i in range(4):
            ny = c[0] + dy[i]
            nx = c[1] + dx[i]
            if 0<=nx<len(check[0]) and 0<=ny<len(check) and check[ny][nx] == -1 and maps[ny][nx] == 1:
                q.append([ny,nx])
                check[ny][nx] = dis + 1
    if check[len(check)-1][len(check[0])-1] != -1:
        return check[len(check)-1][len(check[0])-1] + 1
    
    return -1