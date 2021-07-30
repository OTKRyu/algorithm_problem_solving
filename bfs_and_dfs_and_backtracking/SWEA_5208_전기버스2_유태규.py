def dfs(p, cl):
    global minimum, n
    if p >= n-1:
        if minimum > cl:
            minimum = cl
    else:
        e = batterys[p]
        if cl > minimum:
            return
        else:
            for i in range(p + e, p, -1):
                dfs(i, cl + 1)


for tc in range(1, 1 + int(input())):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    batterys = tmp[1:]
    minimum = n
    dfs(0, 0)
    print('#{} {}'.format(tc, minimum-1))
