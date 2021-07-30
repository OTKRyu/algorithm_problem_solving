tcs = int(input())
for tc in range(1, tcs+1):
    two_d = []
    tmp = list(map(int, input().split()))
    n = tmp[0]
    m = tmp[1]
    max_flies = 0
    for i in range(n):
        two_d.append(list(map(int, input().split())))
    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp_sum = 0
            for x in range(m):
                for y in range(m):
                    tmp_sum += two_d[i+x][j+y]
            if tmp_sum > max_flies:
                max_flies = tmp_sum
    print('#{} {}'.format(tc, max_flies))

