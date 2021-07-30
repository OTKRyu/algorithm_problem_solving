def dir_check(two_d, tmp_x, tmp_y):
    if tmp_x == 0:
        if two_d[tmp_y][tmp_x + 1] == 1:
            return "right"
        else:
            return "up"
    elif tmp_x == 99:
        if two_d[tmp_y][tmp_x - 1] == 1:
            return "left"
        else:
            return "up"
    else:
        if two_d[tmp_y][tmp_x + 1] == 1:
            return "right"
        elif two_d[tmp_y][tmp_x - 1] == 1:
            return "left"
        else:
            return "up"


def move(two_d, direction, tmp_x, tmp_y):
    if direction == "right":
        while 0 <= tmp_x + 1 <= 99 and two_d[tmp_y][tmp_x + 1] != 0:
            two_d[tmp_y][tmp_x] = 0
            tmp_x += 1
        return tmp_x, tmp_y
    elif direction == "left":
        while 0 <= tmp_x - 1 <= 99 and two_d[tmp_y][tmp_x - 1] != 0:
            two_d[tmp_y][tmp_x] = 0
            tmp_x -= 1
        return tmp_x, tmp_y
    else:
        return tmp_x, tmp_y - 1


for tcs in range(10):
    tc = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                y = i
                x = j
    while y != 0:
        cur_dir = dir_check(ladder, x, y)
        x, y = move(ladder, cur_dir, x, y)
    print('#{} {}'.format(tc, x))
