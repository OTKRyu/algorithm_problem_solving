tcs = int(input())
for tc in range(1, tcs+1):
    k, n, m = tuple(map(int, input().split()))
    stops = list(map(int, input().split()))
    result = 0
    point = n
    for i in range(n, -1, -1):
        if point == i:
            if i-k <= 0:
                print("#{} {}".format(tc, result))
                break
            else:
                for j in range(i-k, i):
                    if j in stops:
                        result += 1
                        point = j
                        break
    else:
        print("#{} {}".format(tc, 0))
