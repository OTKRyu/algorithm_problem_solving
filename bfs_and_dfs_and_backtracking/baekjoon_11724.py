import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, id):
    q = deque()
    check[start] = id
    q.append(start)
    while q:
        c = q.popleft()
        for i in range(len(adjs[c])):
            if check[adjs[c][i]] == 0:
                check[adjs[c][i]] = id
                q.append(adjs[c][i])

n, m = map(int, input().split())
adjs = [[] for i in range(n+1)]
check = [0 for i in range(n+1)]
id = 1
for i in range(m):
    s, e = map(int, input().split())
    adjs[s].append(e)
    adjs[e].append(s)
for i in range(1,n+1):
    if check[i] == 0:
        bfs(i, id)
        id += 1
print(id-1)