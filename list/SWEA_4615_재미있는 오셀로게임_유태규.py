def othello(g, n, x, y, c):
    g[y][x] = c
    if c == 1:
        ac = 2
    else:
        ac = 1
    u = [0, -1]
    d = [0, 1]
    l = [-1, 0]
    r = [1, 0]
    ul = [-1, -1]
    ur = [1, -1]
    dl = [-1, 1]
    dr = [1, 1]
    search(g, n, x, y, u,d, c, ac)
    search(g, n, x, y, d,u, c, ac)
    search(g, n, x, y, l,r, c, ac)
    search(g, n, x, y, r,l, c, ac)
    search(g, n, x, y, ul,dr, c, ac)
    search(g, n, x, y, ur,dl, c, ac)
    search(g, n, x, y, dl,ur, c, ac)
    search(g, n, x, y, dr,ul, c, ac)


def search(g, n, x, y, direction, counterd, c, ac):
    cnt = 0
    while -1 < x + direction[0] < n and -1 < y + direction[1] < n and g[y + direction[1]][x + direction[0]] == ac:
        x += direction[0]
        y += direction[1]
        cnt += 1
    if cnt!=0:
        if -1 < x + direction[0] < n and -1 < y + direction[1] < n:
            if g[y + direction[1]][x + direction[0]] == c:
                while cnt != 0:
                    g[y][x] = c
                    x += counterd[0]
                    y += counterd[1]
                    cnt -= 1
            else:
                return


for tc in range(1, int(input())+1):
    result1 = 0
    result2 = 0
    n, m = map(int, input().split())
    board = [[0 for i in range(n)] for j in range(n)]
    center = n//2
    board[center-1][center-1] = 2
    board[center][center - 1] = 1
    board[center - 1][center] = 1
    board[center][center] = 2
    for i in range(m):
        tmp_x, tmp_y, c = map(int, input().split())
        x = tmp_x-1
        y = tmp_y-1
        othello(board, n, x, y, c)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                result1 += 1
            elif board[i][j] == 2:
                result2 += 1
    print('#{} {} {}'.format(tc, result1, result2))
