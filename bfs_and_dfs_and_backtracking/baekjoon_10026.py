from collections import deque
import sys

input = sys.stdin.readline

def bfs1(start, cnt):
    q = deque()
    q.append(start)
    check1[start[0]][start[1]] = cnt
    color = RGB[start[0]][start[1]]
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n and check1[nr][nc] == 0 and RGB[nr][nc] == color:
                check1[nr][nc] = cnt
                q.append([nr,nc])

def bfs2(start, cnt):
    q = deque()
    q.append(start)
    check2[start[0]][start[1]] = cnt
    color = RGB[start[0]][start[1]]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and check2[nr][nc] == 0:
                if color == 'R' or color == 'G':
                    if RGB[nr][nc] == 'R' or RGB[nr][nc] == 'G':
                        check2[nr][nc] = cnt
                        q.append([nr, nc])
                else:
                    if RGB[nr][nc] == 'B':
                        check2[nr][nc] = cnt
                        q.append([nr, nc])


n = int(input())
RGB = [list(input()) for i in range(n)]
check1 = [[0 for i in range(n)] for j in range(n)]
check2 = [[0 for i in range(n)] for j in range(n)]
cnt1 = 0
cnt2 = 0
dr = [1,-1,0,0]
dc = [0,0,1,-1]
for i in range(n):
    for j in range(n):
        if check1[i][j] == 0:
            cnt1 += 1
            bfs1([i,j], cnt1)
        if check2[i][j] == 0:
            cnt2 += 1
            bfs2([i,j], cnt2)
print(f'{cnt1} {cnt2}')