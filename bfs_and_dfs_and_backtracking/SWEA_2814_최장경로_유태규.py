def dfs(p, cl):
    global maximum, n
    check[p] = 1
    possibles = []
    for i in range(n+1):
        if edges[p][i] == 1 and check[i] == 0:
            possibles.append(i)
    if possibles:
        for possible in possibles:
            dfs(possible, cl + 1)
    else:
        if maximum < cl:
            maximum = cl
    check[p] = 0


for tc in range(1, 1 + int(input())):
    n, m = map(int, (input().split()))
    edges = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        s,e  = map(int, input().split())
        edges[s][e] = 1
        edges[e][s] = 1
    check = [0] * (n + 1)
    maximum = 0
    for i in range(1, n + 1):
        dfs(i, 1)
    print('#{} {}'.format(tc, maximum))
