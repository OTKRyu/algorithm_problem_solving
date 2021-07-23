def per(n, cl, total):
    global minimum
    if cl == n:
        if total < minimum:
            minimum = total
        return
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                total += arrays[cl][i]
                if total < minimum:
                    per(n, cl + 1, total)
                total -= arrays[cl][i]
                check[i] = 0
        else:
            return


for tc in range(1, int(input()) + 1):
    n = int(input())
    arrays = []
    for i in range(n):
        arrays.append(list(map(int, input().split())))
    check = [0] * n
    results = []
    minimum = 10000000000000000
    per(n, 0, 0)
    print('#{} {}'.format(tc, minimum))
