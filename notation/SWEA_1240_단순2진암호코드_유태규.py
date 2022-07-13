for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    codes = []
    for i in range(n):
        codes.append(input())
    flag = 0
    for i in range(n):
        for j in range(n):
            if codes[i][j] == '1':
                target_line = codes[i]
                flag = 1
                break
        if flag:
            break
    patterns = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
                '0110111': 8, '0001011': 9}
    t = len(target_line) - 1
    while 1:
        if target_line[t] == '1':
            break
        else:
            t -= 1
    ks = []
    secrets = target_line[t-55:t+1]
    for i in range(8):
        ks.append(secrets[i*7:(i+1)*7])
    results = []
    for k in ks:
        results.append(patterns.get(k))
    tmp = 0
    for i in range(8):
        if i%2:
            tmp += results[i]
        else:
            tmp += results[i]*3
    if tmp%10:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, sum(results)))
