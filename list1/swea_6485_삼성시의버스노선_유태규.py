tcs = int(input())
for tc in range(1, tcs+1):
    lines = int(input())
    stops = [0 for i in range(5000)]
    for line in range(lines):
        a, b = tuple(map(int, input().split()))
        for i in range(a-1, b):
            stops[i] += 1
    checknum = int(input())
    idxs = []
    for i in range(checknum):
        idxs.append(int(input()))
    tmp = []
    for idx in idxs:
        tmp.append(stops[idx-1])
    result = " ".join(list(map(str, tmp)))
    print("#{} {}".format(tc, result))
