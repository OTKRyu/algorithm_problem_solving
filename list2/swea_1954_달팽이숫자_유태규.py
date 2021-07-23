tcs = int(input())

for tc in range(1, tcs + 1):
    n = int(input())
    result = [[0 for i in range(n)] for j in range(n)]
    xs = 0
    xe = n - 1
    ys = 0
    ye = n - 1
    count = 1
    while xe - xs >= 0:
        if xe - xs == 0:
            result[xs][ys] = count
            break
        for i in range(ys, ye + 1):
            result[xs][i] = count
            count += 1
        for j in range(xs + 1, xe + 1):
            result[j][ye] = count
            count += 1
        for i in range(ye - 1, ys - 1, -1):
            result[xe][i] = count
            count += 1
        for j in range(xe - 1, xs, -1):
            result[j][ys] = count
            count += 1
        xs += 1
        xe -= 1
        ys += 1
        ye -= 1
    print("#{}".format(tc))
    for i in range(n):
        tmp = map(str, result[i])
        print(' '.join(tmp))
