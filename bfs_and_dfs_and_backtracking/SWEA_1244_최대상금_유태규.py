def perm(n, k, cl):
    global m
    if k == n:
        tmp = ''.join(ns)
        tmp = int(tmp)
        ms.append(tmp)
        cls.append(cl)
    elif cl == m:
        tmp = ''.join(ns)
        tmp = int(tmp)
        ms.append(tmp)
        cls.append(cl)
    else:
        for i in range(k, n):
            if i == k:
                ns[k], ns[i] = ns[i], ns[k]
                perm(n, k + 1, cl)
                ns[k], ns[i] = ns[i], ns[k]
            else:
                ns[k], ns[i] = ns[i], ns[k]
                perm(n, k + 1, cl + 1)
                ns[k], ns[i] = ns[i], ns[k]


for tc in range(1, 1 + int(input())):
    ns, m = input().split()
    m = int(m)
    ns = list(ns)
    n = len(ns)
    ms = []
    cls = []
    perm(n, 0, 0)
    maximum = 0
    for i in range(len(ms)):
        if maximum < ms[i]:
            if m == cls[i] or (cls[i] < m and (m - cls[i]) % 2 == 0):
                maximum = ms[i]
    print('#{} {}'.format(tc, maximum))
