def check(g):
    xc = x_check(g)
    yc = y_check(g)
    bc = box_check(g)
    if xc == yc == bc == 1:
        return 1
    else:
        return 0

def x_check(g):
    for i in range(9):
        tmp = set()
        for j in range(9):
            tmp.add(g[i][j])
        if tmp != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return 0
    else:
        return 1


def y_check(g):
    for j in range(9):
        tmp = set()
        for i in range(9):
            tmp.add(g[i][j])
        if tmp != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return 0
    else:
        return 1


def box_check(g):
    c_ps = [[0, 0],[0, 3], [6, 0], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6],]
    for c_p in c_ps:
        tmp = set()
        for i in range(3):
            for j in range(3):
                tmp.add(g[c_p[0] + i][c_p[1] + j])
        if tmp != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return 0
    else:
        return 1


for tc in range(1, int(input()) + 1):
    sdoku = []
    for i in range(9):
        sdoku.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, check(sdoku)))

