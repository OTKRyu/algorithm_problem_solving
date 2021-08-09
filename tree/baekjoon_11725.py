import sys

input = sys.stdin.readline


def bfs(start):
    global n
    queue = [0] * n * 2
    front = -1
    rear = -1
    rear += 1
    queue[rear] = start
    pars[start] = start
    while rear - front:
        front += 1
        c = queue[front]
        for i in range(len(edges[c])):
            if pars[edges[c][i]] == 0:
                pars[edges[c][i]] = c
                rear += 1
                queue[rear] = edges[c][i]


n = int(input())
pars = [0] * (n + 1)
edges = [[] for i in range(n + 1)]
for i in range(n - 1):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)
bfs(1)
for i in range(2, n + 1):
    print(pars[i])
