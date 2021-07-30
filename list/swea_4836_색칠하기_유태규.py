tcs = int(input())

for tc in range(1, tcs + 1):
    actual = [[set() for i in range(10)] for j in range(10)]
    n = int(input())
    for r in range(n):
        tmp = list(map(int, input().split()))
        sp = [tmp[0], tmp[1]]
        ep = [tmp[2], tmp[3]]
        cn = tmp[4]
        for i in range(sp[0], ep[0] + 1):
            for j in range(sp[1], ep[1] + 1):
                actual[i][j].add(cn)
    count = 0
    for i in range(10):
        for j in range(10):
            if actual[i][j] == {1, 2}:
                count += 1
    print('#{} {}'.format(tc, count))
