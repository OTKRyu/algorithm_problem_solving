import sys
from collections import deque

input = sys.stdin.readline


def bfs(s):
    global n
    q = deque()
    q.append(s)
    check[s[0]][s[1]] = 1
    dr = [2, 2, 1, 1, -2, -2, -1, -1]
    dc = [1, -1, 2, -2, 1, -1, 2, -2]
    while q:
        r, c = q.popleft()
        if [r, c] == target:
            print(check[r][c] - 1)
            break
        else:
            dis = check[r][c]
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and check[nr][nc] == 0:
                    q.append([nr, nc])
                    check[nr][nc] = dis + 1


for tc in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    check = [[0 for i in range(n)] for j in range(n)]
    bfs(start)
