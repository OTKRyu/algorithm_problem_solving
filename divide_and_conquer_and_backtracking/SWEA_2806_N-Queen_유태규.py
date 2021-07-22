def diagfor(g, j, i):
    dl = [1, -1]
    dr = [1, 1]
    while j + dl[1] > -1 and i + dl[0] < n:
        g[i + dl[0]][j + dl[1]] += 1
        dl[0] += 1
        dl[1] -= 1
    while j + dr[1] < n and i + dr[0] < n:
        g[i + dr[0]][j + dr[1]] += 1
        dr[0] += 1
        dr[1] += 1


def diagback(g, j, i):
    dl = [1, -1]
    dr = [1, 1]
    while j + dl[1] > -1 and i + dl[0] < n:
        g[i + dl[0]][j + dl[1]] -= 1
        dl[0] += 1
        dl[1] -= 1
    while j + dr[1] < n and i + dr[0] < n:
        g[i + dr[0]][j + dr[1]] -= 1
        dr[0] += 1
        dr[1] += 1


def n_queen(g, i, n):
    global cnt
    if n == 1:
        cnt += 1
        return
    else:
        if i == n:
            cnt += 1
            return
        else:
            for j in range(n):
                if g[i][j] == 0:
                    for y in range(n):
                        g[y][j] += 1
                    diagfor(g, j, i)
                    result.append((i, j))
                    if i + 1 < n - 1:
                        if 0 in g[i + 1]:
                            n_queen(g, i + 1, n)
                    else:
                        n_queen(g, i + 1, n)
                    result.pop()
                    diagback(g, j, i)
                    for y in range(n):
                        g[y][j] -= 1


for tc in range(1, 1 + int(input())):
    n = int(input())
    g = [[0 for i in range(n)] for j in range(n)]
    result = []
    cnt = 0
    n_queen(g, 0, n)
    print('#{} {}'.format(tc, cnt))
