from collections import deque
n, k = map(int, input().split())
result = []
q = deque()
for i in range(1, n+1):
    q.append(i)
cnt = 0
while q:
    c = q.popleft()
    cnt += 1
    if cnt % k == 0:
        result.append(c)
    else:
        q.append(c)
print('<',end='')
for i in range(n-1):
    print(result[i], end=', ')
print(result[n-1], end='>')


