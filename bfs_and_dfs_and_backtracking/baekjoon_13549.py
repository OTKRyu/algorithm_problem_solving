from collections import deque

n, k = map(int, input().split())
check = [-1 for i in range(100100)]
q = deque()
q.append(n)
check[n] = 0
while q:
    c = q.popleft()
    step = check[c]
    if c == k:
        print(check[c])
        break
    if c + 1 < 100001 and (check[c+1] == -1 or check[c+1] > step + 1):
        q.append(c + 1)
        check[c + 1] = step + 1
    if c * 2 < 100001 and (check[c*2] == -1 or check[c*2] > step):
        tmp = 1
        while c * (2 ** tmp) < 100001:
            q.appendleft(c * (2 ** tmp))
            check[c * (2 ** tmp)] = step
            tmp += 1
    if c - 1 > -1 and (check[c-1] == -1 or check[c-1] > step + 1):
        q.append(c - 1)
        check[c - 1] = step + 1