def combination(idx, sidx):
    global result, b, flag
    if sidx == r:
        if b <= sum(comb):
            flag = 1
            if result > sum(comb)-b:
                result = sum(comb)-b
        return
    if idx == n:
        return
    comb[sidx] = heights[idx]
    combination(idx + 1, sidx + 1)
    combination(idx + 1, sidx)


for tc in range(1, 1 + int(input())):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    result = b
    heights.sort(reverse=True)
    total = 0
    flag = 1
    for i in range(n):
        total += heights[i]
        if total >= b:
            idx = i
            break
    for i in range(idx, n + 1):
        if flag:
            comb = [0] * i
            r = i
            combination(0, 0)
        else:
            break
    print('#{} {}'.format(tc, result))
