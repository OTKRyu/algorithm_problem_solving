import sys
from collections import deque

input = sys.stdin.readline


def bfs(c):
    q = deque()
    q.append(c)
    check[c] = 0
    while q:
        h = q.popleft()
        time = check[h]
        for adj in adjs[h]:
            if check[adj[0]] > time + adj[1]:
                check[adj[0]] = time + adj[1]
                q.append(adj[0])


for tc in range(int(input())):
    n, d, c = map(int, input().split())
    adjs = [[] for i in range(n + 1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        adjs[b].append([a, s])
    check = [10000000 for i in range(n + 1)]
    bfs(c)
    cnt = 0
    maxima = 0
    for i in range(n + 1):
        if check[i] != 10000000:
            cnt += 1
            if check[i] > maxima:
                maxima = check[i]
    print('{} {}'.format(cnt, maxima))
