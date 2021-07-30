def bfs(p):
    global t
    queue = [0] * 2000002
    front = -1
    rear = -1
    rear += 1
    queue[rear] = p
    check[p] = 0
    while rear - front:
        front += 1
        cl = queue[front]
        idx = check[cl] + 1
        if cl + 1 < 1000001 and check[cl + 1] == -1:
            rear += 1
            queue[rear] = cl + 1
            check[cl + 1] = idx
        if cl - 1 > 0 and check[cl - 1] == -1:
            rear += 1
            queue[rear] = cl - 1
            check[cl - 1] = idx
        if cl * 2 <= 1000000 and check[cl * 2] == -1:
            rear += 1
            queue[rear] = cl * 2
            check[cl * 2] = idx
        if cl - 10 > 0 and check[cl - 10] == -1:
            rear += 1
            queue[rear] = cl - 10
            check[cl - 10] = idx
        if check[t] != -1:
            return check[t]



for tc in range(1, 1 + int(input())):
    s, t = map(int, input().split())
    if s == t:
        print('#{} {}'.format(tc, 0))
    else:
        check = [-1] * 1000001
        result = bfs(s)
        print('#{} {}'.format(tc, result))