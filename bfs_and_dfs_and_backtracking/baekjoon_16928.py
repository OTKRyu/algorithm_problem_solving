from collections import deque

def bfs():
    q = deque()
    q.append(1)
    check[1] = 0
    while q:
        c = q.popleft()
        for i in range(1,7):
            next = c+i
            if 0 < next <= 100:
                if snakes[next] == 0:
                    if check[next] == -1:
                        check[next] = check[c] + 1
                        q.append(next)
                else:
                    if check[snakes[next]] == -1:
                        next = snakes[next]
                        check[next] = check[c] + 1
                        q.append(next)


n, m = map(int, input().split())
snakes = [0 for i in range(101)]
for i in range(n+m):
    a,b = map(int, input().split())
    snakes[a] = b
check = [-1 for i in range(101)]
bfs()
print(check[100])