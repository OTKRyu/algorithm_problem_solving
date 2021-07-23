for _ in range(1, 11):
    tc = int(input())
    n = input()
    m = input()
    cnt = 0

    for i in range(len(m)-len(n)+1):
        tmp_cnt = 0
        for j in range(len(n)):
            if m[i + j] == n[j]:
                tmp_cnt += 1
        if tmp_cnt == len(n):
            cnt += 1
    print('#{} {}'.format(tc, cnt))
