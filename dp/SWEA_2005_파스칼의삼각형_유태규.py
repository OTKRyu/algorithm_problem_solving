def pascal(n):
    result = []
    if n == 1:
        return [1]
    else:
        tmp = [1]
        for i in range(n - 2):
            tmp.append(pascal(n - 1)[i] + pascal(n - 1)[i + 1])
        tmp.append(1)
        return tmp


for tc in range(1, int(input()) + 1):
    num = int(input())
    print('#{}'.format(tc))
    for i in range(1, num + 1):
        print(' '.join(map(str, pascal(i))))
