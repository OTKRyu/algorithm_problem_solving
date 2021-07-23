def reverse(chars):
    result = []
    for i in range(len(chars) - 1, -1, -1):
        result.append(chars[i])
    return ''.join(result)


for _ in range(10):
    tc = int(input())
    two_d = []
    n = 100
    result = 0
    for i in range(n):
        two_d.append(input())
    for m in range(2, 101):
        for i in range(n):
            for j in range(n - m + 1):
                if two_d[i][j:j + m] == reverse(two_d[i][j:j + m]):
                    result = m
        for j in range(n):
            for i in range(n - m + 1):
                tmp = []
                for k in range(m):
                    tmp.append(two_d[i + k][j])
                if ''.join(tmp) == reverse(tmp):
                    result = m
    print('#{} {}'.format(tc, result))
