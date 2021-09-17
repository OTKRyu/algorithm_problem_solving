import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(s)
    check[s] = 0
    while q:
        c = q.popleft()
        step = check[c]
        if c + u <= f and check[c + u] == -1:
            check[c + u] = step + 1
            q.append(c + u)
        if c - d > 0 and check[c - d] == -1:
            check[c - d] = step + 1
            q.append(c - d)
        if check[g] != -1:
            return check[g]
    return 'use the stairs'


f, s, g, u, d = map(int, input().split())
check = [-1 for i in range(f + 1)]
print(bfs())
