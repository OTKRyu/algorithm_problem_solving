possible_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


def solve(g):
    for y in range(9):
        for x in range(9):
            if g[y][x] == 0:
                break
        if g[y][x] == 0:
            break
    else:
        return check(g)
    for y in range(9):
        for x in range(9):
            if g[y][x] == 0:
                if 0 <= x < 3 and 0 <= y < 3:
                    s_x = 0
                    s_y = 0
                elif 3 <= x < 6 and 0 <= y < 3:
                    s_x = 3
                    s_y = 0
                elif 6 <= x < 9 and 0 <= y < 3:
                    s_x = 6
                    s_y = 0
                elif 0 <= x < 3 and 3 <= y < 6:
                    s_x = 0
                    s_y = 3
                elif 3 <= x < 6 and 3 <= y < 6:
                    s_x = 3
                    s_y = 3
                elif 6 <= x < 9 and 3 <= y < 6:
                    s_x = 6
                    s_y = 3
                elif 0 <= x < 3 and 6 <= y < 9:
                    s_x = 0
                    s_y = 6
                elif 3 <= x < 6 and 6 <= y < 9:
                    s_x = 3
                    s_y = 6
                else:
                    s_x = 6
                    s_y = 6
                ps = list(x_p(g,x,y).intersection(y_p(g,x,y)).intersection(box_p(g,s_x,s_y)))
                if len(ps) == 0:
                    return 0
                else:
                    for p in ps:
                        g[y][x] = p
                        if solve(g):
                            return 1
                    else:
                        g[y][x] = 0
                        return 0

def x_p(g, x, y):
    tmpset = set()
    for j in range(9):
        tmpset.add(g[y][j])
    return possible_set.difference(tmpset)


def y_p(g, x, y):
    target = []
    for i in range(9):
        target.append(g[i][x])
    return possible_set.difference(set(target))


def box_p(g, s_x, s_y):
    target = []
    for i in range(3):
        for j in range(3):
            target.append(g[s_y + i][s_x + j])
    return possible_set.difference(set(target))

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
sdoku= []
for i in range(9):
    sdoku.append(list(map(int, input().split())))
solve(sdoku)
for i in range(9):
    print(*sdoku[i])
