for tc in range(1, int(input()) + 1):
    actual = []
    n = int(input())
    if n == 1:
        m = int(input())
        print('#{} {}'.format(tc, m))
    else:
        for i in range(n):
            actual.append(list(map(int, list(input()))))
        center = n // 2
        result = 0
        for i in range(n):
            if i <= center:
                for j in range(center - i, center + 1 + i):
                    result += actual[i][j]
            else:
                for j in range(center - (n - i - 1), center + 1 + (n - i - 1)):
                    result += actual[i][j]
        print('#{} {}'.format(tc, result))
