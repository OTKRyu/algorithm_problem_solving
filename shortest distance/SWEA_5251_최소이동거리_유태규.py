for tc in range(int(input())):
    tmp_n, m = map(int, input().split())
    n = tmp_n + 1
    ds = [[(n - 1) * 10 for j in range(n)] for i in range(n)]
    minimums = [(n - 1) * 10 for i in range(n)]
    for i in range(m):
        tmp = list(map(int, input().split()))
        ds[tmp[0]][tmp[1]] = tmp[2]
    s, e = 0, tmp_n
    minimums[s] = 0
    check = [0 for i in range(n)]
    while 0 in check:
        minimum = (n - 1) * 10
        for i in range(n):
            if minimum > minimums[i] and check[i] == 0:
                idx = i
                minimum = minimums[i]
        if idx == e:
            break
        else:
            check[idx] = 1
            for i in range(n):
                if ds[idx][i] != (n - 1) * 10 and check[i] == 0:
                    minimums[i] = min(minimums[i], minimums[idx] + ds[idx][i])
            short = (n - 1) * 10
            for i in range(n):
                if short > ds[idx][i] and check[i] == 0:
                    s_idx = i
                    short = ds[idx][i]
            minimums[s_idx] = min(minimums[s_idx], minimums[idx] + short)
            for i in range(n):
                if ds[s_idx][i] != (n - 1) * 10 and check[i] == 0:
                    minimums[i] = min(minimums[i],
                                      min(minimums[idx] + ds[idx][s_idx] + ds[s_idx][i], minimums[idx] + ds[idx][i]))
    print('#{} {}'.format(tc + 1, minimums[e]))
