def reverse(chars):
    result = []
    for i in range(len(chars) - 1, -1, -1):
        result.append(chars[i])
    return ''.join(result)


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    two_d = []
    for i in range(n):
        two_d.append(input())
    for i in range(n):
        for j in range(n - m + 1):
            if two_d[i][j:j + m] == reverse(two_d[i][j:j + m]):
                print('#{} {}'.format(tc, two_d[i][j:j + m]))
                break
        if two_d[i][j:j + m] == reverse(two_d[i][j:j + m]):
            break
    for j in range(n):
        for i in range(n - m + 1):
            tmp = []
            for k in range(m):
                tmp.append(two_d[i + k][j])
            if ''.join(tmp) == reverse(tmp):
                print('#{} {}'.format(tc, ''.join(tmp)))
                break
        if tmp == reverse(tmp):
            break
