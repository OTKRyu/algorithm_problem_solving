def dfs(p, n, cl):
    if cl == 7:
        result.add(n)
    else:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        n += nums[p[0]][p[1]]
        for i in range(4):
            np = [p[0] + dy[i], p[1] + dx[i]]
            if 0 <= np[0] < 4 and 0 <= np[1] < 4:
                dfs(np, n, cl + 1)


for tc in range(1, 1 + int(input())):
    nums = [input().split() for i in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs([i, j], '', 0)
    print('#{} {}'.format(tc, len(result)))
