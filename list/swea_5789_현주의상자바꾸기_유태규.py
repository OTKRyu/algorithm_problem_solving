tcs = int(input())
for tc in range(1, tcs+1):
    n, q = tuple(map(int, input().split()))
    hj_boxs = [0 for i in range(n)]
    for i in range(q):
        l, r = tuple(map(int, input().split()))
        for j in range(l-1, r):
            hj_boxs[j] = i+1
    hj_strs = map(str, hj_boxs)
    result = ' '.join(hj_strs)
    print("#{} {}".format(tc, result))
