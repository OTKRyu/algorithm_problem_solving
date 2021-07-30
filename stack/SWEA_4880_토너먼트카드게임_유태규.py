def rsp(d_f):
    if len(d_f) == 1:
        return d_f[0]
    elif len(d_f) == 2:
        if d_f[0][1] == 1 and d_f[1][1] == 2:
            return d_f[1]
        elif d_f[0][1] == 1 and d_f[1][1] == 3:
            return d_f[0]
        elif d_f[0][1] == 2 and d_f[1][1] == 1:
            return d_f[0]
        elif d_f[0][1] == 2 and d_f[1][1] == 3:
            return d_f[1]
        elif d_f[0][1] == 3 and d_f[1][1] == 1:
            return d_f[1]
        elif d_f[0][1] == 3 and d_f[1][1] == 2:
            return d_f[0]
        else:
            if d_f[0][0] < d_f[1][0]:
                return d_f[0]
            else:
                return d_f[1]
    else:
        return rsp([rsp(d_f[:(len(d_f)-1) // 2 + 1]), rsp(d_f[(len(d_f)-1) // 2 + 1:])])


for tc in range(1, int(input()) + 1):
    n = int(input())
    rsps = list(map(int, input().split()))
    true_form = []
    for i in range(n):
        true_form.append([i + 1, rsps[i]])
    print('#{} {}'.format(tc, rsp(true_form)[0]))
