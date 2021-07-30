tcs = int(input())
for tc in range(1, tcs+1):
    alen, blen = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if alen > blen:
        a, b = b, a
        alen, blen = blen, alen
    maximum = 0
    for i in range(blen-alen+1):
        tmp = 0
        if i == 0:
            for j in range(alen):
                maximum += b[i+j] * a[j]
        else:
            for j in range(alen):
                tmp += b[i+j] * a[j]
            if maximum < tmp:
                maximum = tmp
    print("#{} {}".format(tc, maximum))
