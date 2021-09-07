for tc in range(1, 1 + int(input())):
    wons = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8
    n = int(input())
    for i in range(len(wons)):
        if (n // wons[i]) > 0:
            cnt[i] = n // wons[i]
            n = n % wons[i]
    print('#{}'.format(tc))
    print(*cnt)
